# GymBag

## Introduction
GymBag is a fictional e-commerce fashion retailer based in Ireland.
Founded in September 2022, GymBag specializes in buying clearance stock from manufacturers and selling at discounted prices online.

That this website is for educational purposes only and the credit card payment functionality is not set up to accept real payments.
If testing interactively, feel free to use card details below. Further information can be viewed via [Stripe documentation test page](https://stripe.com/docs/testing)
* 4242424242424242 (Visa)
* Expiration date = Any future date (Example: 12/24)
* CVN = any 3 digits (Example: 132)
* Postcode = any 5 digits (Example: 12345)


![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/test_credentials.JPG)

## Showcase
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/gymbag_amiresponsive.JPG)

### Live Website
A deployed link to the website can be found [here](https://sherryrich-gymbag.herokuapp.com/)

### QR Code

 <details>
  <summary>Click here to see QR Code</summary>

  ![](docs/qrcode_sherryrich-gymbag.herokuapp.com.png)

  </details>


# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [UX](#ux-user-experience)
- [Architecture](#architecture)
- [Design](#design)
- [Features](#features)
- [Web Marketing](#web-marketing)
- [Social Media](#social-media)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)




## UX User Experience
### User Stories
Agile Development Process, The MoSCoW method was adopted to approach to prioritizing which project requirements for must have, should have, could have and will not have. Please view [GitHub Issues](https://github.com/sherryrich/gymbag/issues) as well as the [KANBAN board](https://github.com/users/sherryrich/projects/13) used for this project.


#### As the site creator/admin:
* As the website Administrator I would like to be able to access the Django admin to view orders, comments etc
* As the website Administrator I would like to be able to add, view, edit and delete products
* As the website Administrator I would like to be able to add, view, edit and delete blog posts
* As the website Administrator I want to be able to view / reject pending posts from users before publication
* As the website Administrator I want to be able to view newsletter signups
* As the website Administrator I want users to be able to view the business social media


####  As the site user:
* As a website user I want to be able to instantly understand the main purpose of the site and learn more about the business and products on offer
* As a website user I want to be able to register an account
* As a website user I want to be able to update details on my account
* As a website user I want to be able to register for newsletter
* As a website user I want to be able to add products to my shopping bag and update / purchase items easily
* As a website user I want to be able to checkout securely
* As a website user I want to be able to leave comments on all news / blog posts
* As a website user I want to be able to Like & unlike on all news / blog posts
* As a website user I want to be able to search all products by using the search functionality
* As a website user I want to be able to view my order history / my profile
* As a website user I want to be able to send messages via the contact form
* As a website user I want to be able to send messages via the installation form




### Overall Goals
* Create an e-commerce cloud-hosted Full-Stack web application to sell Gym related products online.
* Allow superusers access to full CRUD (create, read, update and deleted) functionality on blog posts / articles and products respectively.
* To provide users with a targeted product selection and smooth customer experience when shopping on GymBag.

### Strategy
* GymBag primarily is focused on selling B2C products to end users. Habits of the consumers have changed recently and many more consumers than ever before have turned to online shopping versus traditional brick-and-mortar store purchases. This is where GymBag aims to benefit consumers by offering large discounts off the manufacturer’s products for home and commercial exercises equipment.

### Site User / Target Audience / Demographic
* Target market is aimed at anyone in the 20 - 35 years old
* Gym enthusiasts who like to post about their gym routines, lifestyle and diet online
* People looking to be part of the community by posting, sharing & liking articles

### Site Goals
* The site's main purpose is immediately clear
* Simple navigation that allows the user to find information and resources intuitively
* User authentication
* CRUD functionality for superuser(s)


## Architecture
### Database Schema

I created 8 tables for the website. Post, Comment, Contact, installation, order, OrderLineItem, Product and UserProfile tables. 

A relational database was created. SQLite was used in development of the website and Postgres via Heroku in production.

The Post table is used by SuperUsers to post blog posts  to the website. It has a Primary Key of ID & a ForeignKey relationship to the Comment table. 
The table also has the following fields, a title, slug (short summary the subject of a post), content, excerpt (short extract), Updated On (date post was updated), Created On (date post was created), status (draft or published) and Likes.

The Comment table is used by users to comment on blog posts. It has the following fields a Primary Key of ID, name, email, body, created on, approved and a ForeignKey to the Post table.

The Contact table is used by users to submit the contact form. It has the following fields a Primary Key of ID, name, email, body & created on (date contact form was submitted) and contact_reason.

The Installation table is used by users to submit the installation query form. It has the following fields a Primary Key of ID, name, email, body & created on (date contact form was submitted) and installation_type.

The Product model contains information about all products listed on the website. It has the following fields a Primary Key of ID, a ForeignKey of category, sku, name, description, has_sizes, price, rating, image_url & image.

The UserProfile table contains information about the user's profile. It has the following fields Primary Key of ID, user, default_phone_number, default_street_address1, default_street_address2, default_town_or_city, default_county, default_postcode & default_country.

The Order model contains all information relating to a customer's order. It has the following fields a Primary Key of ID, order_number, a ForeignKey to the user_profile, full_name, email, phone_number, country, postcode, town_or_city, street_address1, street_address2, county, date, delivery_cost, order_total, grand_total, original_bag, stripe_pid &order_status.

The OrderLineItem table contains information about an order. It has the following fields a Primary Key of ID, a ForeignKey to the order table, product_size, quantity and lineitem_total.

<details>
  <summary>Click here to view Database Schema:</summary>

  ![](docs/database.PNG)

  </details>



## Design
### Wireframes
 <details>
  <summary>Click here to view all wireframes both Desktop & mobile:</summary>

  ![](docs/homepage.JPG)
  ![](docs/products.JPG)
  ![](docs/about.JPG)
  ![](docs/contact.JPG)
  ![](docs/installation.JPG)
  ![](docs/news.JPG)

  ![](docs/homepage_mobile.JPG)
  ![](docs/products_mobile.JPG)
  ![](docs/about_mobile.JPG)
  ![](docs/contact_mobile.JPG)
  ![](docs/installation_mobile.JPG)
  ![](docs/news_mobile.JPG)

  </details>

### Navigation
I created a logic flowchart to help organise the site structure. The ERD (entity relationship diagram) helped visually to confirm user roles and the permissions and website structure.

<details>
  <summary>Click here to view website navigation:</summary>

  ![](docs/gymbag.drawio.png)

  </details>

### Color Palette
<details>
  <summary>Click here to view Color Palette:</summary>

  ![](docs/color_palette.JPG)

  </details>

### Typography
Roboto Condensed is the primary font taken from Google Fonts this font was chosen for its largely geometric font which features friendly and open curves. Fall back fonts are Lato, Arial & sans-serif.

## Features
### Existing Features

### Home page
Homepage displays the logo on the left top, search bar in the middle, then my account and card details on the right hand side.
Below that is the main navigation links. There is a H1 heading with "No 1 for gym gear" along with a large background image of weights bar and plates informing users so that the website's purpose is immediately evident to a new user.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/homepage_features.JPG)

### Navigation Bar
The navigation bar has links to all products, clothing, nutrition, equipment, special offers and more. Included in the dropdown for more are the links to About us, gum installation, news / blog and contact us pages.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/navigation_bar.JPG)

### All Products page
The All products page displays all products available. Users can sort by price, rating, name or category. There is a back to top button if users wish to get back to the top easily.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/all_products.JPG)

### Product Category pages
Users can search via each category in the various dropdown options for quick navigation.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/all_equipment.JPG)

### Individual Product pages - shopping bag
Individual product pages provides a name, description, price, the quantity selected and update and delete options if superuser is logged in.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/shopping_bag.JPG)

### About Us
The about us page informs the user(s) to find brief information on hen the website was formed and what the website sells.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/about_page.JPG)

### Gym Installation page
The Installation page allows potential users contact GymBag regarding potential gym installation queries.  Once the form is successfully sent a message is shown to the user to inform the user.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/gym_installation_page.JPG)

### News / Blog
This feature is used by admin users to display latest news articles and stories to generate inbound traffic to the website organically.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/blog.JPG)

### Contact Us
Feedback and suggestions can be submitted via a form with name, email and body of message and dropdown option, the options available are Returns, Availability, Pricing, Feedback and Other. Once the form is successfully sent a message is shown to the user to inform the user.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/contact_us.JPG)

### Newsletter sign-up
Newsletter signup form encouraging users to enter email address on the homepage for the purposes gathering email addresses for digital marketing campaigns.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/newsletter_signup.JPG)

### Shopping Cart and Checkout
The Shopping Cart updates with the total value spent and displays a success message along with incentive to increase spend to avail of free delivery over $50.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/cart.JPG)

### User Profile Page
The user profile page displays users contact information along with order history including current order status. This can be edited by the superuser in the admin. Once the status is changed this is reflected in real time for the user. The 3 status options are "Confirmed", "Shipped" and "Cancelled", the default status is "Confirmed" once an order is completed.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/my_profile.JPG)

Status is changed in admin.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/order_status.JPG)

## Admin CRUD pages for Products
### Adding a product as a superuser
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/create.JPG)
### Adding a product - success message
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/create_success.JPG)
### Reading / viewing the product listed
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/read_product.JPG)
### Update - product details
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/update_product.JPG)
### Update - product details - confirmation message
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/update_message.JPG)
### Delete - product details
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/delete.JPG)

### Admin
Admin - Superuser Access

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/admin.JPG)

### Footer
The footer contains links to Privacy Policy Terms & Conditions Returns Policy as well as social network links (Facebook, Twitter, Instagram and YouTube) and Copyright information.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/footer.JPG)

### Privacy Policy
GDPR compliant privacy policy informs users about how their data is being collected and processed. It is transparent, concise and easily accessible.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/privacy_policy.JPG)

### Returns
A clear returns policy is also displayed to encourage fist time and repeat customers purchasing.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/returns.JPG)

### Terms & Conditions
Personalized terms and conditions created for GymBag.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/terms_conditions.JPG)

### 404 Page
A 404 page was created to handle user navigational errors and give user a quick ink to direct them back to shopping.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/404.JPG)

## Future Features
* Gift Cards [#28](https://github.com/sherryrich/gymbag/issues/28)
* Customer Reviews [#29](https://github.com/sherryrich/gymbag/issues/29)

## Web Marketing / Marketing Strategies

### SEO - Search Engine Optimization
Google keyword research was used to optimise web pages and content to increase ranking in search engines. Both short-tail & Long-tail keywords are used. The “People also ask” and “Related searches” was also used to identify keywords used.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/seo_keywords.JPG)

### Content Marketing
A blog post was created so that the website can create and distribute content material to attract and convert audience into first time customers and repeat customers. The main aim of the blog posts is to build trust and loyalty.

### Social Media Marketing
A Facebook business page was set up with the aim of generating growth organically by building a community and encouraging loyalty amongst our target market. The advantage of this is its free and quick to set up and Facebook has a large audience and dempgraphic. The site can connect with customers directly via the Facebook platform and wider global audience. The main aim of the Facebook page iis to build and maintain relationship with target audience. Content created can be spread across different social media platforms. 

I have also included a screen shot below should the Facebook business page be removed by facebook.
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/facebook.JPG)

### Email Marketing
Mailchimp is used to gain new customers and retain existing. Mailchimp enables the business to run and analyse the success of newsletter marketing campaigns. Users who register to receive the newsletter are automatically added to weekly newsletter. This strategy was chosen because its free to set up with the current level of business and can scale quickly as the business grows therefore increase conversions and generate more revenue for the business. The users who sign up have already visited the website and are more likely to become customers and therefore low cost to generate sales.


## Technologies Used

### Languages Used
* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used
* [Amazon S3](https://aws.amazon.com/s3/) service offered by Amazon Web Services that provides object storage through a web service interface.
* [amiresponsive](http://ami.responsivedesign.is/) to see how responsive the site is on different devices.
* [Balsamiq](https://balsamiq.com/) was used to create the Wireframes.
* [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) v4.6 was used to help build responsive, mobile-first design.
* [Color-hex](https://www.color-hex.com/) once I identified the colors I wanted I used color-hex to generate the palette.
* [Django](https://www.djangoproject.com/) free and open-source, Python-based web framework that follows the model–template–views architectural pattern.
* [Font Awesome](https://fontawesome.com/) was used for icons for aesthetic and UX purposes on the buttons.
* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
* [Gitpod](https://www.gitpod.io/) An online IDE linked to the GitHub repository used to write my code.
* [Google Chrome Dev tools](https://developer.chrome.com/docs/devtools/) for debugging.
* [Google Fonts](https://fonts.google.com/about) for typography.
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) used for audits to measure the quality of web pages.
* [Google Keyword Planner](https://ads.google.com/aw/keywordplanner/home?)
* [Heroku](https://www.heroku.com/) used to deploy this app, a cloud platform as a service supporting several programming languages.
* [Pexels](https://www.pexels.com/) Images for this project were sourced from Pexels.
* [Privacy Policy Generator](https://www.privacypolicygenerator.info/) Free Privacy Policy Generator.
* [Stripe]() Integrated with Stripe to facilitate online payments.
* [SQLite](https://www.sqlite.org/index.html) database used in local development was a SQLLite database.
* [Terms and Conditions Generator](https://www.termsandconditionsgenerator.com/) Free terms and conditions generator.
* [Unsplash](https://unsplash.com/) Images for this project were sourced from Unsplash.
* [WAVE](https://wave.webaim.org/extension/) Browser Extension testing.
* [Wordtracker](https://www.wordtracker.com/)
* [a11y](https://color.a11y.com/) Color Contrast Accessibility Validator.


### requirements.txt file
* Python libraries listed in the requirements.txt file

![Preview](docs/python_libraries_requirements.JPG)

## Testing
### Validation Testing
### Lighthouse Report

  <details>
  <summary>Lighthouse Report Results</summary>

  ![](docs/lighthouse_homepage.JPG)
  ![](docs/lighthouse_about.JPG)
  ![](docs/lighthouse_accounts_login.JPG)
  ![](docs/lighthouse_bag.JPG)
  ![](docs/lighthouse_blog.JPG)
  ![](docs/lighthouse_contact.JPG)
  ![](docs/lighthouse_installation.JPG)
  ![](docs/lighthouse_products.JPG)
  ![](docs/lighthouse_privacy.JPG)
  ![](docs/lighthouse_returns.JPG)
  ![](docs/lighthouse_terms.JPG)

  </details> 

### The W3C Markup Validator

  <details>
  <summary>HTML Validator Results</summary>

  ![](docs/html_checker_homepage.JPG)
  ![](docs/html_checker_about.JPG)
  ![](docs/html_checker_accounts_login.JPG)
  ![](docs/html_checker_bag.JPG)
  ![](docs/html_checker_blogs.JPG)
  ![](docs/html_checker_contact.JPG)
  ![](docs/html_checker_installation.JPG)
  ![](docs/html_checker_products.JPG)
  ![](docs/html_checker_returns.JPG)
  ![](docs/html_checker_terms.JPG)

  </details> 

### W3C CSS Validator

  <details>
  <summary>Checked using W3C CSS Validator ensuring there were no errors or warnings present. Click here to see the W3C CSS Validator result: </summary>

  ![](docs/w3c_css_validator_result.JPG)

  </details> 

### flake8

  <details>
  <summary>The website pep8online.com is currently down so flake8 was run in the terminal. Migration and settings errors remain. Click here to see the result: </summary>

  ![](docs/flake8.JPG)

  </details> 

### Color Contrast Accessibility Validator

  <details>
  <summary>Checked color contrast analysis accessibility. Click here to see the W3C CSS Validator result: </summary>

  ![](docs/a11y_result.JPG)

  </details> 

### Manual Testing
### More manual testing scenarios and results
| Feature | Test  | Expected Result | Actual Result |
| -------------| ----- | ----- | :----: |
| GymBag logo  | Selecting GymBag logo on homepage |  directs user back to homepage |  Pass |
| Navigation Links  | Selecting navigation links |  directs user to relevant categories & pages |  Pass |
| All categories  | Selecting All for each category |  directs user to show all relevant categories on the same page |  Pass |
| Sort By  | Selecting the filter Sort by for each category |  successfully alters the search By price, rating, name and category options reflects results accordingly on page |  Pass |
| About Us | Selecting About Us |  directs user to About Us page |  Pass |
| Shop Now | Selecting Shop Now |  directs user to full products list page |  Pass |
| Gym Installation | Selecting Gym Installation |  directs user to Gym Installation page |  Pass |
| Submitting Form | Submitting  details in form on installation page |  successfully sends message to admin and displays success message |  Pass |
| Selecting News / Blog | Selecting News / Blog page |  directs user to /blogs/ page |  Pass |
| Selecting News article(s) | Selecting particular News article(s) |  directs user to particular article page |  Pass |
| User Access | Logged in as user |  I can leave a comment on News / Blog posts |  Pass |
| User Access | Logged in as user |  I can leave a like  on  News / Blog posts |  Pass |
| Pagination |  links "next" and "prev" | links at the bottom of the News / Blog posts returns results of the next page (example /?page=2) and back to the previous page | Pass |
| Contact | Selecting Contact | directs user to /contact page  |  Pass |
| Form Validation Required fields | Filling in form on /contact page | requires name, email and body and contact reason selected to send to Django admin  |  Pass |
| Contact form submission | submit contact form | successfully sends data to Django admin as expected  |  Pass |
| Register | Register for an account | selecting Register in my account directs user to /accounts/signup/ page |  Pass |
| Login | Login to an account | selecting Login in my account directs user to /accounts/Login/ page |  Pass |
| Search | Using the search box | Entering a search returns expected result  |  Pass |
| Back to top | Back to top box | Selecting the back to top box on the products pages brings the user back to the top of the page  |  Pass |
| Search no results | No search | Entering a no results search returns error message and shows all products  |  Pass |
| New User | Registering as a new user | Registering as a new user entering form validation works |  Pass |
| Admin | Loggin in as Logging in as superuser / admin | Logging in as superuser / admin directs user to admin access, shows product management page |  Pass |
| Login Message | log-in Success | "successfully signed in as (user name)" message shown to user|  Pass |
| Add Product | Adding a new product | Adding a new product on the product management page successfully adds product |  Pass |
| News / blog | Create a new news / blog article |  Creating a new blog / news article in Django admin reflects on the front end | Pass |
| News / blog | Read the news / blog article |  As a user I can see the blog / news article on the front end | Pass |
| News / blog  |  Update an existing news / blog article | As admin I can update and edit existing blog / news article |  Pass |
| News / blog  |  Delete an existing news / blog article | As admin I can delete an existing blog / news article |  Pass |
| Leave a comment | Submit comment on an article | Confirmation message that post is "waiting for approval" shown to user |  Pass |
| Add Product | no image is selected | default image is used |  Pass |
| Deleting Product | Deleting selected product | removed product from search |  Pass |
| Deleting Message | Deleting product confirmation | Confirmation message of deletion is shown when successfully deleted |  Pass |
| Deleting Message | Deleting product confirmation | Confirmation message of deletion is shown when successfully deleted |  Pass |
| Defensive Programming | Test for SQL Injection attacks | Users not permitted to access create/update/deleate products or articles if they dont have access permission | Pass |
| Logging out | message shown | Logging out as a user / admin prompts "are you sure" message |  Pass |
| Successfully signed out | signed out message shown | "You have signed out" message shows to user when successfully signed out |  Pass |
| Logging out | Logging out and redirect | Logging out as a user / admin directs user to homepage |  Pass |
| Footer | social media links | Clicking on the social media icons in the footer open the link in a new tab |  Pass |
| Footer | Privacy Policy links | Clicking on the Privacy Policy link in the footer diverts user to the /privacy/ page |  Pass |
| Footer | Terms and Conditions links | Clicking on the Terms and Conditions link in the footer diverts user to the /terms/ page |  Pass |
| Footer | Returns Policy links | Clicking on the Returns Policy link in the footer diverts user to the /returns/ page |  Pass |


## Automated Testing

### Unit testing
I decided to run some limited automated tests for the contact page as a way to demonstrate knowledge and ability to write and view unit tests. For future projects I hope to expand unit testing and aim for 100%.

  <details>
  <summary>Automated tests results - Contact</summary>

  ![](docs/django_auto_testing.JPG)

  </details> 


  <details>
  <summary>Coverage HTML Report - Contact</summary>

  ![](docs/coverage_html_report.JPG)

  </details> 

### Responsiveness Browser Compatibility


|  | Chrome | Firefox | Edge | Safari | Pass/Fail |
| ------------- |-------------| -----|  ---------- |  -----| :----: |
| Expected Appearance   | yes | yes  | yes  | yes | Pass |
| Expected Layout   | yes | yes  | yes  | yes | Pass |

## Bugs / Errors encountered during development
* “can’t open file ‘manage.py’: [Error 2] No such file or directory”. Reason why was there is a character missing character in the command used for starting the project
 [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug1.JPG)
* Incorrectly named the file mobile_top_header.html [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug2.JPG)
* Needed to have pillow installed to use the image field - pip3 install pillow [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug3.JPG)
* Dropdown results were not displaying because I had comma separated when it should have been underscore [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug4.JPG)
* Typo in both dumbbells and kettlebells caused products not to display [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug5.JPG)
* Includes folder in the wrong location [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug6.JPG)
* Gitpod, online resource glitch - always a good idea to push regularly [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug7.JPG)
* Must create app before adding name of app to installed_apps in settings.py [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug8.JPG)
* Missed closing bracket in settings.py [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug9.JPG)
* Webhook wasn’t displaying order in the terminal. resolved by making the port public by clicking on the lock icon. [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug10.JPG) - [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug11.JPG)
* Spotted typo error in checkout - admin.py [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug12.JPG) - [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug13.JPG)
* Updated webhook handler URL in strip to match the change in URL on Girpod locally - then the webhooks started to process stransactions sucesfully again.
* Comments in the code arent allowed in json [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug14.JPG)
* Typo in template literal didn’t display, should be lowercase p {{ products }} [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug15.JPG)
* When I created duplicate of products.html and edited I should have edited it to "product_detail.html" and not products_detail.html"  [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug16.JPG)
* If still logged in as /admin this can cause issues locally. When I logged out and back in I was able to see expected local version.
* didn’t append the webhook URL in Stripe with '/' [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug17.JPG) & [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug18.JPG)
* issues deploying - followed steps advised on slack and worked [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug19.JPG)
* Typo in settings.py [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug20.JPG)
* CSS - back to top was behind fixed bottom footer, initially I used z-index but felt this looked wrong so just moved it up above the footer [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug21.JPG) 
* Needed to run a migration on the Postgres DB just with a Heroku prefix and it will affect the Postgres DB on Heroku instead of local SQLite one.
"heroku run python3 manage.py makemigrations" & "heroku run python3 manage.py migrate" resolved this. [View here](https://github.com/sherryrich/gymbag/blob/main/docs/bug22.JPG)

## Unfixed Bugs
* When running "python3 -m flake8" in the terminal and excluding cscode, migrations & settings there are 2 remaining issues detailed below.
* "./gymbag/urls.py:50:1: F811 redefinition of unused 'handler404' from line 23". This is as per code institute instructions [View here](https://github.com/sherryrich/gymbag/blob/main/docs/404_error.JPG) 
* ./checkout/apps.py:8:9: F401 'checkout.signals' imported but unused. This is as per code institute Boutique Ado instructions 
[Code Institute Solutions](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/250e2c2b8e43cccb56b4721cd8a8bd4de6686546/checkout/apps.py)


## Stripe
* Register for an account at stripe.com
* Go to Developers section once logged in
* Go to API keys section
![Preview](docs/stripe_api.JPG)
* Note both the publishable and secret keys
* In your local environment(env.py) and Heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')
os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')
* Back in the Developers section of your stripe account click on Webhooks
![Preview](docs/stripe_webhook.JPG)

* Create a webhook with the url of your website /checkout/wh/, for example:
 https://sherryrich-gymbag.herokuapp.com/checkout/wh/
* Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
* Note the key created for this webhook
* In your local environment(env.py) and Heroku, create environment variable STRIPE_WH_SECRET with the secret values os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')
* Test the webhook and note the success/fail attempts for troubleshooting, see events and logs for further testing.

## Amazon WebServices
* Create an account at aws.amazon.com
* Open the S3 application and create an S3 bucket named "sherryrich-gymbag2"
* Select AWS Region.
![Preview](docs/aws_bucket.JPG)

* Uncheck the "Block All Public access setting" & acknowledge that the bucket will be public, it will need to be public in order to allow public access to static files.
![Preview](docs/aws_bucket2.JPG)

* In the Properties section, navigate to the "Static Website Hosting" section and click edit
* Under the Properties section, turn on "Static Website Hosting", and set the index.html and the error.html values.
![Preview](docs/aws_bucket3.JPG)

* In the Permissions section, click edit on the CORS configuration and set the below configuration
![Preview](docs/aws_bucket4.JPG)

* Click to edit the bucket policy and generate and set the below configuration:
![Preview](docs/aws_bucket5.JPG)

* Bucket policy
![Preview](docs/aws_bucket6.JPG)

* Go to the Access Control List and set the List objects permission for everyone under the Public Access section.
* Open the IAM application to control access to the bucket and set up a user group called
* Click on Policies, and Create Policy.
* Click on the JSON tab and import a pre-built Amazon policy called AmazonS3FullAccess:
* Set the following settings in the JSON tab:
* Click Review Policy, give it a name and description and click Create Policy.
* To attach the policy to the group, navigate to Groups, then Permissions, and under Add Permissions, select Attach Policy.
* To create a user for the group, click Add User, and create one
* Add the user to the group created, making sure to download the CSV file which contains the user's access credentials.
* Note the following AWS code in Settings.py. An environment variable called USE_AWS must be set to use these settings, otherwise it will use local storage:
![Preview](docs/aws_settings.JPG)


## Deployment

* This project was developed using a GitPod workspace. The code was committed to Git and pushed to GitHub using the terminal.

* Log in to [Heroku](https://id.heroku.com/login) or create an account
* On the main page click New and Create New App
* Note: new app name must be unique
* Next select your region, I chose Europe.
* Click Create App button
* Click in resources and select Heroku Postgres database
* Click Reveal Config Vars and add new config "SECRET_KEY"
* Click Reveal Config Vars and add new config "DISABLE_COLLECTSTATIC = 1"
* The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
* Next, go to Buildpack section click Add Buildpack select python and Save Changes
* Scroll to the top of the page and choose the Deploy tab
* Select Github as the deployment method
* Confirm you want to connect to GitHub
* Search for the repository name and click the connect button
* Scroll to the bottom of the deploy page and select the preferred deployment type
* Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

* As Heroku Student Pack no longer includes free access to the Postgres add-on I had to migrate Postgres databases from Heroku to keep ElephantSQL.
* Navigate to ElephantSQL.com and click “Get a managed database today”
* Select “Try now for FREE” in the TINY TURTLE database plan
* Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account
* In the Create new team form

### Migrating databases
* Create a database
* Log in to ElephantSQL.com to access your dashboard
* Click “Create New Instance”
* Set up your plan
* Select “Select Region” EXAMPLE "EU-West-1 (Ireland)"
* Then click “Review”
* Check your details are correct and then click “Create instance”
* Return to the ElephantSQL dashboard and click on the database instance name for this project

### Migrating your data
* Navigate to the Postgres Migration Tool repo on github in a new browser tab
* Click the Gitpod button to open a new workspace
* Run the script " python3 reel2reel.py" command in the terminal
* In a different browser tab, go to your app in Heroku and select the Settings tab
* Click the “Reveal Config Vars” button
* Copy the value in the DATABASE_URL Config Var. It will start with postgres://
* Return to Gitpod and paste in the URL you just copied into the terminal where prompted to provide your DATABASE_URL and click enter
* In your original browser tab, get your ElephantSQL database URL. Again, it will start with postgres://
* Return to Gitpod and paste in the URL where prompted
* The data will now be downloaded from Heroku and uploaded to your ElephantSQL database
* To test that your database has been moved successfully, return to ElephantSQL and select BROWSER
* Click the “Table queries” button. If you see any options in the dropdown, your tables have been created
* Select a table name you recognise, and then click “Execute”
* You should see your data displayed relating to the table you selected

### Connecting ElephantSQL database to Heroku
* In the Heroku Dashboard for your project, open the Resources tab
* In the Resources tab, remove the existing Postgres add-on:
* Confirm by typing in the name of your Heroku app when prompted.
* Navigate to the Settings tab
* Reveal your existing Config Vars. The original DATABASE_URL should have been deleted when the add-on was removed.
* Add a new config var called DATABASE_URL and paste in the value for your ElephantSQL database, and click Add to save it.
* Check the Activity tab to confirm


### Final Deployment 

* Create a runtime.txt `python-3.8.14`
* Create a Procfile `web: gunicorn gymbag.wsgi:application`
* When development is complete change the debug setting to: `DEBUG = False` in settings.py
* In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

### Forking This Project

* Open [GitHub](https://github.com/sherryrich/gymbag)
* Find the 'Fork' button at the top right of the page
* Once you click the button the fork will be in your repository

### Cloning This Project

* Clone this project by following the steps:

* Open [GitHub](https://github.com/sherryrich/gymbag)
* You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
to copy the URL
* Once you click the button the fork will be in your repository
* Open a new terminal
* Change the current working directory to the location that you want the cloned directory
* Type 'git clone' and paste the URL copied in step 3
* Press 'Enter' and the project is cloned

## Credits

* Code Institute - [Boutique Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/3adff2bf4a78469db72c5330b1afa836/) -  Walkthrough
* Code Institute - [Hello Django](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/121ef050096f4546a1c74327a9113ea6/) -  Walkthrough
* Code Institute - [I think therefore I blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/
) - Django blog project Walkthrough
* Codemy.com Database Tables With Django - [YouTube](https://youtu.be/z5e_8FgKZig)
* Codemy.com Delete a Blog Post - Django - [YouTube](https://youtu.be/8NPOwmtupiI)
* Corey Schafer Python Django Tutorial [YouTube](https://www.youtube.com/c/Coreyms)
* Create A Simple Blog With Python and Django [YouTube](https://youtu.be/B40bteAMM_M)
* The Web Developer Bootcamp 2002 [Udemy](https://www.udemy.com/course/the-web-developer-bootcamp/)
* How to Use GitHub for Automated Kanban Project Management [YouTube](https://www.youtube.com/watch?v=YVFa5VljCDY)
* Style Django Forms With Bootstrap 
 [YouTube](https://www.youtube.com/watch?v=6-XXvUENY_8)
 * More Django Styling  
 [YouTube](https://www.youtube.com/watch?v=uJp4PaDkux0)


## Acknowledgements
* To create this website, I relied on material covered in the Full Stack Development course by Code Institute.
* I also sourced information and help from a variety of sources such as Slack Community Channels, Udemy, W3Schools, MDN and YouTube for Online Web Tutorials and resources.
* Martina Terlevic for reviewing my work and providing valuable feedback and advice.

This project is for educational use only and was created for the Code Institute Module.

Created by Richard Sherry 😊