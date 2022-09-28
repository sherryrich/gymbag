from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.forms import Form
from .forms import OrderForm
from django.db.models import Q
from .models import Order, OrderLineItem
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


"""View for searching orders"""


# def search_order(request):
#     if not request.htmx:
#         raise Http404
#     try:
#         order_number = request.GET.get('order_number').upper()
#         order = get_object_or_404(Order, order_number=order_number)
#     except:
#         order = None
#     if order is None:
#         return HttpResponse('No order found')
#     context = {
#         'order_number': order_number,
#     }
#     template = 'checkout/templates/orderstatus.html'
#     return render(request, template, context)


# def search_order(request):
#     print("hi")
#     if "searched" in request.GET:
#         searched = request.GET['searched']
#         print(searched)
#         print("hi")
#         if not searched:
#             return redirect("/")
#         post_list = Order.objects.filter(
#             Q(order_number=searched))
#         print(searched)
#         print(post_list)
#         return render(request, 'orderstatus.html',{'searched': searched, 'post_list': post_list})
#     else:
#         return render(request, 'orderstatus.html')


def search_order(request):
    order_list = Order.objects.all()
    return render(request, 'orderstatus.html', 
        {'order_list' : order_list})


# def search_order(request):
#     if request.method == 'GET':
#         searched = request.GET['searched']
#         if not searched:
#             return redirect("/")
#         search_list = Order.objects.filter(
#             Q(order_number__icontains=searched)).filter(status=1)
#         print(search_order)
#         context = {'order_number': order_number}

#         return render(
#             request, 'orderstatus.html', context)
#     else:
#         return render(request, 'orderstatus.html', {})

# def search_orders(request):

#     context = {}
#     template = 'orderstatus.html'
#     return render(request, template, context)


# def search_order(request):
#     if not request.htmx:
#         raise Http404
#     try:
#         order_number = request.GET.get('order_number').upper()
#         order = get_object_or_404(Order, order_number=order_number)
#     except:
#         order = None
#     if order is None:
#         return HttpResponse('No order found')
#     context = {
#         'order_number': order_number,
#     }
#     template = 'checkout/templates/checkout/snippets/order_status.html'
#     return render(request, template, context)


# def search_order(request):
#     search_order = Order.order_number
#     if "searched" in request.GET:
#          searched = request.GET['searched']
#          print(search_order)
#          if not searched:
#              return redirect("/")
    
#     return render(request, 'orderstatus.html', 
#         {'search_order' : search_order})




# def search_order(request):
#     context = {}
#     template = 'orderstatus.html'
#     return render(request, template, context)

