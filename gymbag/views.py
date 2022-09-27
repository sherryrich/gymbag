class about(View):
    """View for displaying the 'About' page."""
    template_name = "about.html"


"""View for searching articles"""


def search_order(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if not searched:
            return redirect("/")
        post_list = Post.objects.filter(
            Q(content__icontains=searched) |
            Q(title__icontains=searched) |
            Q(author__username__icontains=searched)).filter(status=1)

        return render(
            request, 'index.html',
            {'searched': searched, 'post_list': post_list})
    else:
        return render(request, 'index.html', {})