# GymBag

## Introduction
GymBag is a fictional e-commerce fashion retailer based in Ireland.
Founded in September 2022, GymBag specializes in buying clearance stock from manufacturers and selling at discounted prices online.

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
#### As the site creator/admin:
####  As the site user:
### Overall Goals
### Strategy

## Architecture
### Database Schema

## Design
### Wireframes
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
The naviation bar has links to all products, clothing, nutrition, equipment, special offers and more. Included in the dropdown for more are the links to About us, gum instatiion, news / blog and ccontact us pages.

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
The about us page informs the user(s) to find brieft information on hen the website was formed and what the website sells.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/about_page.JPG)

### Gym Installation page
The Installation page allows potential users contact GymBag regarding potential gym instaallation queries.  Once the form is successfully sent a message is shown to the user to inform the user.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/gym_installation_page.JPG)

### News / Blog
This feature is used by admin users to display latest news articles and stories to generate inbound traffic to the website organically.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/blog.JPG)

### Contact Us
Feedback and suggestions can be submitted via a form with name, email and body of message and dropdown option, the options available are Retuns, Availabilty, Pricing, Feedback and Other. Once the form is successfully sent a message is shown to the user to inform the user.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/contact_us.JPG)

### Newsletter sign-up
Newsletter signup form encourging users to enter email address on the homepage for the purposes gathering email addresses for digital marketing campaigns.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/order_status.JPG)

### Shopping Cart and Checkout
The Shopping Cart updates with the total value spent and displays a success message along with incentive to increase spend to avail of free delivery over $50.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/cart.JPG)

### User Profile Page
The user profile page displays users contact information along with order history includeing current oder status. This can be edited by the superuser in the admin. Once tthe status is changed this is reflected in realtime for the user. The 3 status options are "Confirmed", "Shipped" and "Cancelled", the default status is "Confirmed" once an order is completed.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/my_profile.JPG)
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/order_status.JPG)

### Admin CRUD pages for Products, News / Blog
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/product_management.JPG)
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/read.JPG)
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/update.JPG)
![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/delete.JPG)

### Admin
Admin - Superuser Access

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/admin.JPG)

### Footer
The footer contains links to Privacy Policy Terms & Conditions Returns Policy as well as social network links (Facebook, Twitter, Instagram and YouTube) and Copyright information.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/footer.JPG)

### Privacy Policy
GDPR compliant privacy policy informs users about how their data is being collected and processed. It is transparent, concise and easily accessible.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/footer.JPG)

### Returns
A clear returns policy is alos displayed to encourge fist time and repeat customers purchasing.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/privacy_policy.JPG)

### Terms & Conditions
Personalized terms and conditions created for GymBag.

![Preview](https://github.com/sherryrich/gymbag/blob/main/docs/terms_conditions.JPGG)

### 404 Page
A 404 page was created to handle user navigational errors and give user a quick ink to direct them back to shopping.

![Preview](https://github.com/sherryrich/gymbag/blob/docs/404.JPG)

### Future Features
### Gift Cards
### Customer Reviews

## Web Marketing

## Social Media

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
* [Heroku](https://www.heroku.com/) used to deploy this app, a cloud platform as a service supporting several programming languages.
* [Pexels](https://www.pexels.com/) Images for this project were sourced from Pexels.
* [Privacy Policy Generator](https://www.privacypolicygenerator.info/) Free Privacy Policy Generator.
* [Stripe]() Integrated with Stripe to faciliate online payments.
* [SQLite](https://www.sqlite.org/index.html) database used in local development was a SQLLite database.
* [Terms and Conditions Generator](https://www.termsandconditionsgenerator.com/) Free terms and conditions generator.
* [Unsplash](https://unsplash.com/) Images for this project were sourced from Unsplash.
* [WAVE](https://wave.webaim.org/extension/) Browser Extension testing.
* [a11y](https://color.a11y.com/) Color Contrast Accessibility Validator.

## Testing
### Validation Testing
### Lighthouse Report
### The W3C Markup Validator
### W3C CSS Validator
### W3C CSS Validator
### PEP8 online
### JSHint
### Color Contrast Accessibility Validator
### Manual Testing

## Bugs / Errors encountered during development

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