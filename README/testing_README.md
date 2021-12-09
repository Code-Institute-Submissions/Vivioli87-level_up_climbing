# Level Up! Climbing
A climbing coaching platform where users can book and pay for climbing courses with Level Up climbing coaches. Read articles about climbing and be part of the community.

*Developed and designed for Code Institue, Milestone Project 4: Full Stack Frameworks with Django

[Please view the live project here](https://level-up-climbing.herokuapp.com/)

[Main README.md file](/README/README.md)

## Table of contents

1. [User Stories Testing](#user-stories-testing)
2. [Code Validation](#code-validation)
3. [Functionality Testing](#functionality-testing)
4. [Performance Testing](#performance-testing)
5. [Encountered Issues](#encountered-issues)

## User Stories Testing

### Visitor Stories

1. As a site visitor, I would like to easily register for an account so that I can have a personal account to view a profile with personalised information.
    - With the use django all auth, registering for an account is simple, there are many calls to sign up on various different pages as well as the home page.
2. As a site visitor, I would like to easily login and logout so that I can access my personal account information.
    - With the use django all auth, logging in and out is simple. This can be done through the log in logout options on the nav bar under account. There are also many 
3. As a site visitor, I would like to easily recover my password in case I forget it so that I can recover access to my account.
    - With the use django all auth, recoving a password is easy. There is a forgotten password link on the login page which will send an email to the user in order to recover their account.
4. As a site visitor, I would like to receive an email confirmation after registering so that I can verify that my account registration was successful.
    - When registering an account an email will be sent to ther user with a link for them to confirm their email address.
5. As a site visitor, I would like to have a personalised user profile so that I can view my personal coaching history/upcoming schedule and update my personal information.
    - On login the user is directed to their personalized profile page, this shows the customer their saved personal information. Which can be updated simply on the form. It will also show the user their course bookings.
6. As a site visitor, I would like to view a list of coaching options so that I can select some to book/purchase.
    - On the courses page, this shows all courses available to book. There is also a filter dropdown so that the user can filter by level. 
7. As a site visitor, I would like to view coaching course session details so that I can identify the level of climbing aimed at, times, dates, venue, number of sessions in course, price and coach.
    - On each Course on the courses list, a logged in user can click to view more in depth information about the course, with lesson detail in a handy popover container.
8. As a site visitor, I would like to be able to be able to book or enquire about 1:1 coaching options so that I can find out about  price per session, available times, dates and coaches.
    - On the 1:1 coaching dropdown, there is an enquiry form for 1:1 coaching. There are a few details about potential cost/price but the site owner would contact the user to further talk to them about their coaching needs and confirm availability price etc.
9. As a site visitor, I would like to review the course I am booking at checkout so that I can ensure I am booking the correct course and can review important information. 
    -On the checkout/booking page the key course details are confirmed on this page so the user can ensure they are booking the correct course.
10. As a site visitor, I would like to easily enter my payment information so that I can check out quickly and with no hassles.
    - With stripe this is easy, card entry fields are easy to use and error messages will appear if the card details fields have been entered inaccurately.
11. As a site visitor, I would like to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
    - With stripe this is completely secure.
12. As a site visitor, I would like to view a booking confirmation after checkout, with a unique booking reference, so that I can verify that I havent made any mistakes.
    - All booking information is saved on the profile page. Once checkout is a success there is a page that confirms the booking details and the reference number but also prompts the user to go to their profile for this information also. button to profile provided.
13. As a site visitor, I would like to view articles about climbing so that I can learn more about certain climbing topics
    - There is an articles page on the nav bar. Logged in users can into each article overview on the main articles page and this will take them to be able to read the full article.
14. As a site visitor, I would like to comment on the articles as well as edit and delete my own comments if needs be.
    - On the article detail page, logged in users can comment on the article and can only edit/delete their own article.
15. As a site visitor, I would like a site that is easy to navigate and gives messages to confirm actions have been completed.
    - The site is easy to navigate using the nav bar and the various buttons or links that are provided throughout the site. Failed or successful actions also result in a toast appearing in the top right hand corner.


### Business Stories

Coaches
1. As a coach, I would like to have a personalised coach profile so that I can identify what courses I am running and the course information.
    - On login the coach is directed to their personalized coach's profile page, this shows the customer their saved personal information and coach information which is displayed on the about page. Both can be updated simply on the forms. It will also show the coach the courses they are coaching/due to coach.
2. As a coach, I would like to be able to update my personal information and coach information so users can learn more about me.
    - On login the coach is directed to their personalized coach's profile page, this shows the customer their saved personal information and coach information which is displayed on the about page. Both can be updated simply on the forms.

Site owner/Superuser
1. As a site owner and as a superuser, I would like to be able to add a coaching course to the site but also edit it to be able to provide coaching options for the site users. (For safety I will not delete courses in case users have paid for a slot but can edit time/venue/coach if the situation calls for it.)
    - On the account page there is a add course dropdown where a new course can be added simply through the use of a form
2. As a site owner and as a superuser, I would like to mark a course as completed so that they no longer appear on the courses page for users to book.
    - Super users can edit a course and update to mark the course as completed. Once updated the course detail page shows up and warns that the course is marked as completed and prompts the superuser to re-edit the course if this was an error.
3. As a site owner and as a superuser, I would like to have a page where I can view enquiries from users, whether general or requests for 1:1 coaching.
    - On the account dropdown the super user has an Enquiry manager page this has both responses from the general query form and the 1:1 coaching form.
4. As a site owner and as a superuser, I would like to be able to view the enquiries with the visitors contact information and mark the enquiry as complete when its been resolved.
    - Each query has a button so the supueruser can view the information and contact details of the person sending the information
5. As a site owner and as a superuser, I would like to add articles, as well as edit and delete them if needs be.
    - On the account page the user has an option to add an article. On the article detail page the superuser can edit and delete articles easily.
6. As a site owner, I would like an error page directing the user back to a safe page if there are any broken links/404 errors on the website.
    - There is a personalized working 404 page informs the customer to check the url they used is correct and if it is and the problem persists to use the contact page to let us know the details of the error. All navigations links are present on the page to help the user get back to safety.

[Back to table of contents](#table-of-contents)

## Code Validation

Every page of the project was validated by the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) to ensure there were no syntax errors or issues.

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate CSS code. No issues found

[jshint.com](https://jshint.com/) was used to check JS code.

[Python syntax checker](https://extendsclass.com/python-tester.html)

### W3C Markup Validation Service

Checked using validate by URI options.

### W3C CSS Validation Service

Checked using direct input.

### jshint.com

When using jshint ensue to enable the "New JavaScript features (ES6)" in the configure tab. 

### Python syntax checker

checked syntax using [Python syntax checker](https://extendsclass.com/python-tester.html) as well as the "Problems" tab in gitpod. No Pep8 issues seen in final code, these have been fixed along the way.

Some flake 8 issues I cannot fix as they would break up lines of code that cannot be broken up.

# Functionality Testing

- Feature testing on each page in turn and for all screen sizes using the developer tools, my own personal devices and got friends/family to test also.
    - Checked for broken links
    - Checked 404 page works if there is a broken link/an incorrect url is used.
    - Checked stripe webhooks perform as expected
    - Checked filter function work as expected.
    - Checked all prepulated information works on edit pages.
    - All django modals, forms and views perform and function as they should
    - Checked responsiveness of website so that no elements are hidden or have not formatted correctly.

### Browser Testing

The website was tested on the following browser types. All browser versions were up to date.
- **Google chrome** - best performance with all cookies allowed.
- Firefox
- Safari
- Edge
- Samsung Internet
- Google chrome for Android 

The website does not work as well on Internet Explorer, please use Edge if you need to use a microsoft browser.

The website is functioning and fully responsive on all above mentioned browsers.

### Device Testing

The website was tested on the following devices of mine:
- Windows laptop
- Samsung Galaxy A70

The site has been tested on friend's devices also. These include:

I have tested other devices using the chrome developer tools including:
- Moto G4
- Galaxy S5
- Pixel 2 / Pixel 2 XL
- iPhone 5 / SE / 6 / 7 / 8 (incl Plus options) / X
- iPad / iPad Pro
- Surface duo
- Laptop

The website is platform-cross compatible and has a consistant result.

[Back to table of contents](#table-of-contents)

## Performance Testing

Using lighthouse on Google Chrome developer tools - reports generated scores of 80s-100s

Some issues that hamper the performance score meaning that score can be in the 80-90 range are due to bootstrap css, javascript/jquery scripts and links taking a longer time to load. 
I tested adding async or defer to these and although it vastly improved the performance score, it resulted in console errors due to key jquery scripts not loading quickly enough.
Therefore I have left this as it was.

I did amend the main cover image to a next-gen format which decreased the time it took to load that and improved my performance scores.

Lighthouse also pointed out various issues such as a missing link on the mobile header page, missing meta description, a typo in the id/arialabelids on the nav dropdowns causing 2 not to be unique.
These issues have all been corrected.

[Back to table of contents](#table-of-contents)

## Encountered Issues

- Most issues I have had have been of my own doing and are regarding simple syntax errors or forgetting key aspects of the django framework process as I was still getting to grips with this on the project.

- Some of these simple issues have occasionally taken a while to spot and have caused various commits trying to test debugging the issue. e.g. the correct url/placement for favicons to work on heroku.

- I had assistance with autofilling a datetime field with a value from the model/instance of the model. Johann from the tutor support helped me determine the correct formatting of the template tag to be able to render this correctly.

- The performance issues as mentioned in the above section.

- I had added 'async' to the stripe javascript link to improve performance scores on lighthouse however this caused intermittent issues with the card field loading on the checkout page and therefore a user was able to book a class without putting any payment information in. I have since removed async to avoid this issue and ensure the card field (and its validation) loads properly every time. I checked that my logic for the initial issue was correct with tutor support and this could be the only reason for this occurring

-There were some html validation issues from using the |linebreaks in a template tag. I have fixed this by changing the enclosing element tag from a paragraph to a div. Now the linebreaks show inside the div and not outside the previously used p tag.

- One issue from html validation that I am unable to fix is regarding the syntac on my map image elements. I have not amended this as this syntax was taken from Google maps (static) how to guides.


[Back to table of contents](#table-of-contents)