# Level Up! Climbing
A climbing coaching platform where users can book and pay for climbing courses with Level Up climbing coaches. Read articles about climbing and be part of the community.

*Developed and designed for Code Institue, Milestone Project 4: Full Stack Frameworks with Django

[Please view the live project here](https://level-up-climbing.herokuapp.com/)

[Main README.md file]()

## Table of contents

1. [User Stories Testing](#user-stories-testing)
2. [Code Validation](#code-validation)
3. [Functionality Testing](#functionality-testing)
4. [Performance Testing](#performance-testing)
5. [Encountered Issues](#encountered-issues)

## User Stories Testing

### Visitor Stories

1. As a site visitor, I would like to easily register for an account so that I can have a personal account to view a profile with personalised information.
    -
2. As a site visitor, I would like to easily login and logout so that I can access my personal account information.
    -
3. As a site visitor, I would like to easily recover my password in case I forget it so that I can recover access to my account.
    -
4. As a site visitor, I would like to receive an email confirmation after registering so that I can verify that my account registration was successful.
    -
5. As a site visitor, I would like to have a personalised user profile so that I can view my personal coaching history/upcoming schedule and update my personal information.
    -
6. As a site visitor, I would like to view a list of coaching options so that I can select some to book/purchase.
    -
7. As a site visitor, I would like to view coaching course session details so that I can identify the level of climbing aimed at, times, dates, venue, number of sessions in course, price and coach.
    -
8. As a site visitor, I would like to be able to be able to book or enquire about 1:1 coaching options so that I can find out about  price per session, available times, dates and coaches.
    -
9. As a site visitor, I would like to review the course I am booking at checkout so that I can ensure I am booking the correct course and can review important information. 
    -
10. As a site visitor, I would like to easily enter my payment information so that I can check out quickly and with no hassles.
    -
11. As a site visitor, I would like to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
    -
12. As a site visitor, I would like to view a booking confirmation after checkout, with a unique booking reference, so that I can verify that I havent made any mistakes.
    -
13. As a site visitor, I would like to view articles about climbing so that I can learn more about certain climbing topics
    -
14. As a site visitor, I would like to comment on the articles as well as edit and delete my own comments if needs be.
    -
15. As a site visitor, I would like a site that is easy to navigate and gives messages to confirm actions have been completed.


### Business Stories

Coaches
1. As a coach, I would like to have a personalised coach profile so that I can identify what courses I am running and the course information.
    -
2. As a coach, I would like to be able to update my personal information and coach information so users can learn more about me.
    -

Site owner/Superuser
1. As a site owner and as a superuser, I would like to be able to add a coaching course to the site but also edit it to be able to provide coaching options for the site users. (For safety I will not delete courses in case users have paid for a slot but can edit time/venue/coach if the situation calls for it.)
    -
2. As a site owner and as a superuser, I would like to mark a course as completed so that they no longer appear on the courses page for users to book.
    -
3. As a site owner and as a superuser, I would like to have a page where I can view and enquiries from users, whether general or requests for 1:1 coaching.
    -
4. As a site owner and as a superuser, I would like to be able to view the enquiries with the visitors contact information and mark the enquiry as complete when its been resolved.
    -
5. As a site owner and as a superuser, I would like to add articles, as well as edit and delete them if needs be.
    -
6. As a site owner, I would like an error page directing the user back to a safe page if there are any broken links/404 errors on the website.
    -

[Back to table of contents](#table-of-contents)

## Code Validation

Every page of the project was validated by the [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input) to ensure there were no syntax errors or issues.

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate CSS code.

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

Using lighthouse on Google Chrome developer tools - reports generated scores of

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



[Back to table of contents](#table-of-contents)