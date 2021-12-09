# Level Up! Climbing
A climbing coaching platform where users can book and pay for climbing courses with Level Up climbing coaches. Read articles about climbing and be part of the community.

*Developed and designed for Code Institue, Milestone Project 4: Full Stack Frameworks with Django

[Please view the live project here](https://level-up-climbing.herokuapp.com/)

![Mockups](/README/images/mockup.png) 

## Table of Contents

1. [Overview](#overview)
2. [User Experience](#ux-(user-experience))
    - [User Stories](#user-stories)
        - Visitor Stories
        - Business Stories
    - [Structure](#structure)
    - [Skeleton](#skeleton)
        - Wireframes
    - [Design](#design)
        - Colour Scheme
        - Fonts
        - Imagery
3. [Features](#features)
    - Current Features
    - Future Implementation
4. [Technologies](#technologies)
    - Languages
    - Frameworks, Libraries and Tools
    - Validation
5. [Testing](#testing)
6. [Deployment](#deployment)
    - GitHub pages
7. [Credits](#credits)
    - Code
    - Media
    - Content
8. [Acknowledgements](#acknowledgements)
9. [Disclaimer](#disclaimer)

## Overview

My MS4, Full Stack Frameworks with Django project, for my Code Institute course. I decided to base my project on climbing as this is one of my hobbies.

I came up with the name Level Up! Climbing as it is aimed at climbers at all levels improving their climbing grade through the coaching courses provided.

The purpose of this site is to be a community for climbers and for the company to offer their coaching services around the Greater Manchester area at various gyms. I've based the idea loosely on Catalyst Climbing who offer a similar idea of 1:1 coaching in the London area. 

A registered user has access to their own profile page that contains an overview of courses they have booked through the website and can also leave comments on articles that are available to read.

[Back to table of contents](#table-of-contents)

## UX (User Experience)

The user types for this website would be for climbers who want to improve their knowledge either through the coaching courses or through the articles available

### Visitor Stories
1. As a site visitor, I would like to easily register for an account so that I can have a personal account to view a profile with personalised information.
2. As a site visitor, I would like to easily login and logout so that I can access my personal account information.
3. As a site visitor, I would like to easily recover my password in case I forget it so that I can recover access to my account.
4. As a site visitor, I would like to receive an email confirmation after registering so that I can verify that my account registration was successful.
5. As a site visitor, I would like to have a personalised user profile so that I can view my personal coaching history/upcoming schedule and update my personal information.
6. As a site visitor, I would like to view a list of coaching options so that I can select some to book/purchase.
7. As a site visitor, I would like to view coaching course session details so that I can identify the level of climbing aimed at, times, dates, venue, number of sessions in course, price and coach.
8. As a site visitor, I would like to be able to be able to book or enquire about 1:1 coaching options so that I can find out about  price per session, available times, dates and coaches.
9. As a site visitor, I would like to review the course I am booking at checkout so that I can ensure I am booking the correct course and can review important information. 
10. As a site visitor, I would like to easily enter my payment information so that I can check out quickly and with no hassles.
11. As a site visitor, I would like to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
12. As a site visitor, I would like to view a booking confirmation after checkout, with a unique booking reference, so that I can verify that I havent made any mistakes.
13. As a site visitor, I would like to view articles about climbing so that I can learn more about certain climbing topics
14. As a site visitor, I would like to comment on the articles as well as edit and delete my own comments if needs be.
15. As a site visitor, I would like a site that is easy to navigate and gives messages to confirm actions have been completed.

### Business Stories

Coaches
1. As a coach, I would like to have a personalised coach profile so that I can identify what courses I am running and the course information.
2. As a coach, I would like to be able to update my personal information and coach information so users can learn more about me.

Site owner/Superuser
1. As a site owner and as a superuser, I would like to be able to add a coaching course to the site but also edit it to be able to provide coaching options for the site users. (For safety I will not delete courses in case users have paid for a slot but can edit time/venue/coach if the situation calls for it.)
2. As a site owner and as a superuser, I would like to mark a course as completed so that they no longer appear on the courses page for users to book.
3. As a site owner and as a superuser, I would like to have a page where I can view enquiries from users, whether general or requests for 1:1 coaching.
4. As a site owner and as a superuser, I would like to be able to view the enquiries with the visitors contact information and mark the enquiry as complete when its been resolved.
5. As a site owner and as a superuser, I would like to add articles, as well as edit and delete them if needs be.
6. As a site owner, I would like an error page directing the user back to a safe page if there are any broken links/404 errors on the website.

[Back to table of contents](#table-of-contents)

## Structure

Level Up! Climbing website is designed to be effective, consistent and user friendly.
- Interaction Design
    - Consistent design will be used throughout the website to maintain a good UX.
    - The simple navigation bar will be consistent across all pages.
    - Buttons when hovered over and clicked will provide a visual indication to the site visitors what they are selecting.
    - Consistent colour scheme will be used throughout the site.
    - Links to external pages, if applicable, will open in a new tab so the user is not taken away from the website.

- Information Architecture (IA)

    Website:
    - Non logged in users:
        - Can view the home page and about pages to learn more about the company.
        - Can use the contact forms, both for general enquiries and 1:1 coaching.
        - Can view an overview of courses that are on offer however will be prompted to register for an account/login to be able to book one or to view more details.
        - Can view an overview of articles that are on offer to read however will be prompted to register for an account/login to be able to read the full article.
    - Logged in users (in addition to the above) including coaches:
        - Can view the full course details and see if their is availability or if they have already booked.
        - Can proceed to booking a course with a secure checkout page.
        - Can update their profile information and update this
        - Can view the full article and leave a comment if they wished to.
        - Can edit and delete their own comments left on the articles
    - Site owener/Superuser
        - In addition to the above...
            - can add and edit a course.
            - can add, edit and delete an article.
            - can view enquiries sent from contact forms and can mark them as complete.
            - can view the django admin page.
    
    - There are 7 apps on the website (not including the project level app): Articles, checkout, contact, courses, home,
    profiles and venues.

    Database:
    
    ![Database schema](/README/images/database_schema.png) 

[Back to table of contents](#table-of-contents)

## Skeleton

The initial webpage layouts were sketched on the paper. The wireframes were then created in Balsamiq. Please view the wireframes for desktop, tablet and mobile screens on the following images. These are rough design ideas and will have changed and developed into what the website is now.

Desktop

![Wireframe - Desktop](/README/images/Desktop_wireframes.png)

Tablet

![Wireframe - Tablet](/README/images/Tablet_wireframes.png)

Mobile

![Wireframe - Mobile](/README/images/Mobile_wireframes.png)


[Back to table of contents](#table-of-contents)

## Design

### Colour Scheme

- After sourcing the image that I used for my home page, the color scheme developed from there. I enjoyed the bright green colour climbing holds that stood out and decided to use green and whites to provide a good contrast but sleek design.
- I use two main green colors #10bc6c and #127245. the former being a bright green similar to the color of the climbing hold in my main cover image. The second being a darker green that will add more depth and increase readability on certain webpages.
- I use a green and white linear transparent gradient overlay over the main cover image on other pages to keep the theme consistent on the website. On pages where there is a lot of content/text I have removed the transparency.
- According to a colour pyschology website [very well mind](https://www.verywellmind.com/color-psychology-green-2795817), green is calming and can remind people of nature and growth.

### Fonts

- I used just the one font through this project, Lato in order to keep the text clean and consistent.
- Both fonts were imported from [Google Fonts](https://fonts.google.com/)

### Imagery

- All imagery have been sources from [Unsplash](https://unsplash.com/) with the exception of:
    - the no image placeholder image from [free icon spng](https://www.freeiconspng.com/img/23485)
    - the icon used in my favicom which was made by Freepick from [flaticon](www.flaticon.com)
- All images are climbing themed and were chosen due to their bright colors and fun appearance.

[Back to table of contents](#table-of-contents)

## Features

### Current Features
- Navigation bar with dropdowns (consistant on all pages):
    - an easy way to navigate through the website to specific sections.
    - The navigation bar is different depending on whether a user is logged in or not. (More options are availible to users that are logged in)
    - The navigation bar is fully responsive and it collapses to navbar-toggler-icon (hamburger menu) on smaller devices, bringing up the link options a side navigation bar.
- Responsive
    - Side navigation bar on smaller devices.
    - Size and layout differences to be more aesthetically pleasing on medium and small devices, which is discussed in the specific pages below.
- Pagination
    - Pagination is used on the courses, articles and article detail (on the comments) to limit results to a certain number per page. Allowing the user to not have to scroll a lot on 1 page.
- Filter on courses
    - Users can filter courses by their 'level' to make their course search easier and more applicable to their needs.
- 404 page
    - If an error occurs, I have built a 404 page to help direct users and visitors back to safety.
- login required
    - I have restricted access to pages that should only be accessed when logged in using a decorator.
- contact forms
    - for the user to get in touch with the company.
- secure checkout using Stripe.
- secure register and login process using django all auth.
- admin page for the superuser.
- google maps to show users where the venues are.
- Messages to confirm to the user when actions have been taken or if there is an error on something that happened.

### Future Implementation

More developed features for the 1:1 coaching aspect.
    - A calendar system so that it is easier for the superuser/coach to schedule individual sessions.
    - Feedback forms from coaching sessions so that the user has more interaction from the coach on the website and it can aid their learning.

Shop with company branded apparrel to add more economic opportunities to this website

[Back to table of contents](#table-of-contents)

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5) was used as the main language to complete the structure of the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) was used to style the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for responsive aspects within bootstrap but also my own JavaScript code to add interactivity to the website.
- [JQuery](https://en.wikipedia.org/wiki/JQuery) was used for responsive aspects within bootstrap but also custom Jquery code to add interactivity to the website.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was used for back end data centric work and connecting to the database.
- [Markdown](https://en.wikipedia.org/wiki/Markdown) - used for the readme documnetation.

### Webframwork

- [Django](https://en.wikipedia.org/wiki/Django_(web_framework))

### Database

- [SQLite](https://en.wikipedia.org/wiki/SQLite) was used in local development environment
- [Postgre](https://en.wikipedia.org/wiki/PostgreSQL) was used when the site had been deployed to heroku

### Frameworks, Libraries and Tools

- [django](https://www.djangoproject.com/) 
- [Bootstrap](https://getbootstrap.com/) for styling.
- [Google Fonts](https://fonts.google.com/) was used to import the fonts to the website.
- [Unspash](https://unsplash.com/) for images.
- [Favicon generator](https://realfavicongenerator.net/)
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes for the website.
- [CSS Tricks](https://css-tricks.com/) was used as a general source.
- [W3Schools](https://www.w3schools.com/) was used as a general source.
- [StackOverflow](https://stackoverflow.com/) was used as a general source.
- [GitHub](https://github.com/) was used for repository hosting and for storing the source code.
- [Gitpod](https://gitpod.io/) was used as the development environment for writing the code.
- [Git](https://git-scm.com/) was used as version control system to add, commit and push code to GitHub.
- [Techsini](https://techsini.com/multi-mockup/) was used to create the responsive mockup image.
- [W3C Spell checker](https://www.w3.org/2002/01/spellchecker) was used to check the spelling of the webpage.
- [Markdown guide](https://www.markdownguide.org/basic-syntax/)
- [Heroku](heroku.com/home) for deployment
- [Google Developers](https://developers.google.com/) for the maps API
- [Amazon Web Services](https://aws.amazon.com/) for hosting static and media files for deployed site.

### Validation

- [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) was used for Markup validation.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) was used for CSS code validation.
- [jshint.com](https://jshint.com/) was used to check JS code.

See further information on results found during validation on the separate [Testing document]().

## Testing

Testing process was written in a separate document [Testing document](/README/testing_README.md)

[Back to table of contents](#table-of-contents)

## Deployment

### Clone 
To clone this project from its [GitHub repository](https://github.com/Vivioli87/level_up_climbing):

1. From the repository, click **Code**
2. In the **Clone >> HTTPS** section, copy the clone URL for the repository
3. In your local IDE open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made
5. Type `git clone`, and then paste the URL you copied in Step 2
6. Press Enter. Your local clone will be created
7. Create a file called env.py to hold your app's environment variables, which should contain the following:
 - os.environ.setdefault("IP", "0.0.0.0")
 - os.environ.setdefault("PORT", "5000")
 - os.environ.setdefault("SECRET_KEY", "<app secret key>")
 - link to local sqlite database.

### How to deploy to Heroku

To deploy the app to Heroku from its [GitHub repository](https://github.com/Vivioli87/meeple_finder), the following steps were taken:

1. From the GitPod terminal, create **requirements.txt** and **Procfile** using these commands in your console:
- pip3 freeze --local > requirements.txt
- echo web: python app.py > Procfile

2. **Push** these files to GitHub
3. **Log In** to [Heroku](https://id.heroku.com/login)
4. Select **Create new app** from the dropdown in the Heroku dashboard
5. Choose a unique name ('level-up-climbing') for the app and the location nearest to you
6. Go to the **Deploy** tab and under **Deployment method** choose GitHub
7. In **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**
8. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**
9. Enter the following keys (values not shown as personal to the app).
        - SECRET KEY
        - DATABASE_URL = (postgres key)
    - For AWS access
        AWS_ACCESS_KEY-ID = *
        AWS_SECRET_ACCESS_KEY = *
        USE_AWS = True
    - For gmail services to allow confirmation emails to be sent
        EMAIL_HOST_PASS = *
        EMAIL_HOST_USER = (your gmail email address)
    - For stripe
        STRIPE_PUBLIC_KEY = *
        STRIPE_SECRET_KEY = *
        STRIPE_WH_SECRET = *

10. Go back to the **Deploy** tab and under **Automatic deploys** choose **Enable Automatic Deploys**
11. Under **Manual deploy**, select **master** and click **Deploy Branch**
12. Once the app has finished building, click **Open app** from the header row of the dashboard

[Back to table of contents](#table-of-contents)

## Credits

### Code/knowledge

- Resource used to help with adding django pagination to the site.
    [Pagination with django](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html)

- Hex codes for transparent colors.
    [Transparent Hex Codes](https://gist.github.com/lopspower/03fb1cc0ac9f32ef38f4 )

- Line breaks on django template tags.
    [stackoverflow](https://stackoverflow.com/questions/10270891/newline-in-models-textfield-not-rendered-in-template)

- Django documnentation for many things such as how to override the 404 page, help on models, forms, template tags.
    [django docs](https://docs.djangoproject.com/en/3.2/)

- Resource for sending emails with django (used as well as django docs) [django send mail](https://simpleisbetterthancomplex.com/tutorial/2016/06/13/how-to-send-email.html)

- Tutor support - Johann who helped me figure out how to autofill the datetime input with existing values.

- Boutique Ado walk through project from code institue.

### Media

- Climbing wall photo (main home page image) - Photo by [yns plt](https://unsplash.com/@ynsplt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on Unsplash
- Image of coach 'Dave' - Photo by [LOGAN WEAVER](https://unsplash.com/@lgnwvr?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on Unsplash
- Image of coach 'Sarah' - Photo by [Elijah M. Henderson](https://unsplash.com/@elijahhenderson?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on Unsplash
- Hands pic on articles - Photo by [Brook Anderson](https://unsplash.com/@brookanderson?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on Unsplash
- Shoes pic on articles - Photo by [Elahe Motamedi](https://unsplash.com/@elahemotamedi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on Unsplash
- Other articles pics:
    - Photo by [bady abboas](https://unsplash.com/@bady?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on Unsplash 
    - Photo by [Markus Spiske](https://unsplash.com/@markusspiske?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

- ['no image' image](https://www.freeiconspng.com/img/23485)
- [favicon](https://www.flaticon.com/authors/freepik) - made by Freepick from www.flaticon.com


[Back to table of contents](#table-of-contents)

## Acknowledgements

- My mentor, Mr. Victor Miclovich, for the helpful feedback and guidance.
- [Code Institute](learn.codeinstitute.net) for all course materials, wlakthrough project and ongoing support.
- Johann, Code Institute tutor support.
- Fellow Code Institute students for their feedback, suggestions and resource links.
- My family and friends for testing and useful feedback.

[Back to table of contents](#table-of-contents)

## Disclaimer

The information provided and images used on this website are for educational purposes only.

[Back to table of contents](#table-of-contents)
