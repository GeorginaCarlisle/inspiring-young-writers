# Testing and Validation

## Contents

[Code Validation](#code-validation)

[User Story Testing](#user-story-testing)

[Form validation Testing](#form-validation-testing)

[Accessibility Testing](#accessibility-testing)

[Lighthouse](#lighthouse)

[Responsive Testing](#responsive-testing)

[Compatibility Testing](#compatibility-testing)


## Code Validation

[Return to contents list](#contents)

## User Story Testing

The acceptance criteria for each user story has been checked on completion (1st Check) and then re-checked during the final testing stage.

| # | User Story | Acceptance Criteria | 1st Check | Final Check |
| -- | ---- | ---- | -- | -- |
| 1 | As a **new user** the website is clearly geared towards children age 8 - 12 and sharing writing | I am drawn to a clear title "Inspiring Young Writers aged 8 - 12" | PASS | |
| | | A hero image shows children at laptops creating stories and poems | PASS | | 
| | | The platform name "Inspiring young writers" is clearly displayed on the left of the nav bar | PASS | |
| | | A short introduction tells me exactly what the platform is for. | PASS | |
| 2 | As a **new user** I can read work written by another child | | | |
| 3 | As a **new user** I am given clear information on what registered users can do | | | |
| | | | | |
| 4 | As the **parent of a new user** I am provided with information which details how the site works | | | |
| | | | | |
| 5 | As the **parent of a new user** I can contact the site admin | I can navigate intuitively and easily to the contact page | PASS | |
| | | The design of the page is pleasing to the eye and doesn't distract | PASS | |
| | | The title and introduction reassure me as to what the form is for | PASS | |
| | | Clear labels indicate the information to be added to each input field | PASS | |
| | | The button to submit is clear | PASS | |
| | | When entering the wrong information I am prompted and informed what needs to be entered | PASS | |
| | | I am given clear success feedback on submission of the form | PASS | |
| 6 | As the **site admin** user's question and concerns along with their contact details are passed to me | Submitted contact us data emailed to the site owner | PASS | |
| 7 | As a **new user** I am provided with the name and contact links for the developer who created this platform | The name of the developer and year platform created are clearly visible at the bottom of every page. | PASS | |
| | | On larger screens extra info is given to say that the platform was created for 'educational purposes only'. | PASS | |
| | | Clear and easy to access links to take the user to the developer's LinkedIn and GitHub. | PASS | |
| | | Clicking on links open relevant page in new tab. | PASS | |
| 8 | As a **new user** I am informed when page link errors occur and provided with a link straight back to the landing page | Attempting to access a webpage that does not exist, has been moved, or has a dead or broken link takes me to a 404 page | PASS | |
| | | I am taken to an error 500 page if the server encounters an unexpected condition that prevented it from fulfilling the request | PASS | |
| | | Both pages provide links back to the platform | PASS | |
| 9 | As a **new user** I can easily set up an account | I can navigate intuitively and easily to the sign-up page | PASS | |
| | | The landing page contains a call to action providing a direct and clear link to sign-up | PASS | |
| | | The design of the page is pleasing to the eye and doesn't distract | PASS | |
| | | The title and clear instructions help me to navigate the sign-up process | PASS | |
| | | It is clear which part of the form is for the child and which is for the parent | PASS | |
| | | Clear labels indicate the information to be added to each input field | PASS | |
| | | The button to sign-up is clear | PASS | |
| | | When entering the wrong information I am prompted and informed what needs to be entered | PASS | |
| | | I am given clear feedback to let me know I have successfully signed up | PASS | |
| | | On signing-up I am redirected to the account_home page | PASS | |
| 10 | As the **parent of a new user** I am asked to input my name and email address and give consent for my child joining the site | When signing up to the platform, my child is informed that they will need me to sign up | PASS | |
| | | I am asked to provide my name, email address and consent before my child can sign up | PASS | |
| 11 | As a **registered user** I can use my pen-name and password to login to my account | I can navigate intuitively and easily to the login page | PASS | |
| | | The design of the page is pleasing to the eye and doesn't distract | PASS | |
| | | The title and clear instructions help me to navigate the login process | PASS | |
| | | Clear labels indicate the information to be added to each input field | PASS | |
| | | The button to login is clear | PASS | |
| | | When entering the wrong information I am prompted and informed what needs to be entered | PASS | |
| | | I receive a clear message to let me know I have successfully logged in | PASS | |
| | | On logging in I am redirected to the account_home page | PASS | |
| 12 | As a **signed-in user** I can easily logout of my account | I can logout out easily and intuitively | PASS | |
| | | I am given clear success feedback on logging out of my account | PASS | |
| | | On logging out I am redirected to the home page | PASS | |
| 13 | As a **registered user** (with the help of my parent) I can reset my password using a link sent to my parent’s email | | | |
| | | | | |
| 14 | As a **signed-in user** I can edit my profile | | | |
| | | | | |
| 15 | As a **signed-in user** I can delete my account | | | |
| | | | | |
| 16 | As the **parent of a registered user** I am informed of any profile changes my child makes and my consent to any changes is required | | | |
| | | | | |
| 17 | As the **site admin** I can remove accounts | As a site admin I can log in to the admin side of the site | | |
| | | I can click to bring up a list of all registered users | | |
| | | I can click to delete a selected user | | |
| | | I am asked to confirm this action before it will be carried out | | |
| 18 | As the **parent of a registered user** I am informed via email if my child’s account has been removed including the reason why | | | |
| | | | | |
| 19 | As a **signed-in user** user once logged in I am taken to a home page for my account | The top left of the nav bar lets me know I am signed in to my account with wording unique to me "Pen name's inspiring writing" | PASS | |
| | | The navigation bar provides links to all the registered user features |  PASS | |
| | | It is easy and intuitive to navigate through the available features | PASS | |
| | | A clear title welcomes me to my account | PASS | |
| | | There are clear buttons to take me straight to important areas of the site | PASS | |
| | | The page cannot be accessed unless logged in | PASS | |
| 20 | As a **signed-in user** I am provided with tips on how I can use the platform when I first log in to my account | | | |
| | | | | |
| 21 | As a **signed-in user** I am informed when page link errors occur and provided with a link straight back to my account home page | | | |
| | | | | |
| 22 | As the **parent of a signed-in user** I can also access the information for parents when my child is logged in | | | |
| | | | | |
| 23 | As the **parent of a signed-in user** I can also contact the site admin when my child is logged in | | | |
| | | | | |
| 24 | As a **signed-in user** I can navigate to a page where all my work is listed by status | | | |
| | | | | |
| 25 | As a **signed-in user** I am provided with tips and ideas for the sort of work I could create | | | |
| | | | | |
| 26 | As a **signed-in user** I can write and submit a piece of work with title | | | |
| | | | | |
| 27 | As a **signed-in user** my writing is passed through validation tests before it is saved | | | |
| | | | | |
| 28 | As a **signed-in user** I can write a blurb for my writing | | | |
| | | | | |
| 29 | As a **signed-in user** I can attach a picture to my writing | | | |
| | | | | |
| 30 | As a **signed-in user** I can save a draft of my work | | | |
| | | | | |
| 31 | As a **signed-in user** I can view my published work | | | |
| | | | | |
| 32 | As a **signed-in user** I can view and edit any work pending approval | | | |
| | | | | |
| 33 | As a **signed-in user** I can view and edit my draft work | | | |
| | | | | |
| 34 | As a **signed-in user** I can delete my writing | | | |
| | | | | |
| 35 | As the **site admin** all stories need to be validated by me before they are posted to the page | | | |
| | | | | |
| 36 | As the **site admin** I am informed when a child submits their writing for approval | | | |
| | | | | |
| 37 | As the **site admin** I can send a message to the user should their writing fail to meet approval guidelines, | | | |
| | | | | |
| 38 | As the **site admin** I can send parents an email sharing the submitted story and the reason why it failed to meet approval | | | |
| | | | | |
| 39 | As the **site admin** I can remove approved status from previously approved work | | | |
| | | | | |
| 40 | As a **signed-in user** I can view work from other users | | | |
| | | | | |
| 41 | As a **signed-in user** I can filter work | | | |
| | | | | |
| 42 | As a **signed-in user** I can click a help button should I see/read something I don’t like | | | |
| | | | | |
| 43 | As the **parent of a signed-in user** my child is prompted to seek out my guidance should they see/read something they don’t like | | | |
| | | | | |
| 44 | As the **parent of a signed-in user** I can raise concern about a specific piece of writing | | | |
| | | | | |
| 45 | As the **site admin** I am alerted immediately to any raised concerns | | | |
| | | | | |
| 46 | As a **signed-in user** I can give feedback to other users | | | |
| | | | | |
| 47 | As a **signed-in user** I can view all feedback associated with a piece of work | | | |
| | | | | |
| 48 | As a **signed-in user** my feedback is passed through validation tests | | | |
| | | | | |
| 49 | As a **signed-in user** I can edit my feedback | | | |
| | | | | |
| 50 | As a **signed-in user** I can delete my feedback | | | |
| | | | | |
| 51 | As a **signed-in user** I am alerted to any new feedback on my published work | | | |
| | | | | |
| 52 | As a **signed-in user** I can view feedback given to me by other users | | | |
| | | | | |
| 53 | As a **signed-in user** I can edit my published work | | | |
| | | | | |
| 54 | As a **signed-in user** I can delete feedback given to me by other users | | | |
| | | | | |
| 55 | As a **signed-in user** I can click a help button should I see something in the feedback that worries me | | | |
| | | | | |
| 56 | As the **parent of a signed-in user** my child is prompted to seek out my guidance should they see/read something in the feedback that worries them | | | |
| | | | | |
| 57 | As the **parent of a signed-in user** I can raise concern about a specific piece of feedback | | | |
| | | | | |
| 58 | As the **site admin** I am alerted immediately to any raised concerns about feedback | | | |
| | | | | |
| 59 | As the **site admin** I can remove inappropriate feedback | | | |
| | | | | |
| 60 | As the **site admin** I can send parents an email sharing posted feedback and the reason it has been removed  | | | |
| | | | | |
| 64 | As a **user** I can navigate intuitively through the site | The navigation links display clearly across the top of the page for larger screens. | PASS | |
| | | The navigation links display clearly in a dropdown menu on smaller screens. | PASS | |
| | | On smaller screens I can click a hamburger icon allowing me to open the mobile nav. | PASS | |
| | | On smaller screens I can click on an x to close the mobile nav. | PASS | |
| | | The platform name "Inspiring young writers" is clearly displayed on the left of the nav bar. This directs back to the home page. | PASS | |
| | | When hovering over a link there is clear visual feedback. | PASS | |
| | | All navigation links take you to the correct destination when clicked. | PASS | |

[Return to contents list](#contents)

## Form validation Testing

### Sign-up form

| Input Field | Requirement | Error caught | Final check |
| --- | ----- | ---- | -- |
| Pen name | Required field | "Please fill in this field" notification pointed at input box | |
| | Unique name required | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "User with this Username already exists." | |
| | Text only no numbers | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "Only letters and spaces are allowed in your Pen name" | |
| | Maximum length 20 | Cannot physically enter more than 20 characters | |
| Age | Required field | "Please fill in this field" notification pointed at input box | |
| | Age must be between and including 8 and 12 | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "Ensure this value is greater than or equal to 8." | |
| | | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "Ensure this value is less than or equal to 12." | |
| First name | Required field | "Please fill in this field" notification pointed at input box | |
| | Text only no numbers | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "Only letters and spaces are allowed in your First name" | |
| | Maximum length 12 | Cannot physically enter more than 12 characters | |
| Second name | Required field | "Please fill in this field" notification pointed at input box | |
| | Text only no numbers | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "Only letters and spaces are allowed in your Second name" | |
| | Maximum length 20 | Cannot physically enter more than 20 characters | |
| Email | Recognisable as a real email address | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "Enter a valid email address." | |
| | | "Please include an @ in the email address" notification pointed at input box | |
| | | "Please enter a part following the @" notification pointed at input box | |
| | | "Please enter a part followed by @" notification pointed at input box | |
| | Maximum length 320 | Cannot physically enter more than 320 characters | |
| Consent | Must be checked | "Please tick this box if you want to proceed" notification pointed at input box | |
| Password1 | Required field | "Please fill in this field" notification pointed at input box | |
| | Can't be too similar to other personal information | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "The password is too similar to the username." | |
| | Must contain at least 8 characters | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "This password is too short. It must contain at least 8 characters." | |
| | Can't be a commonly used password | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "This password is too common." | |
| | Can't be entirely numeric | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "This password is entirely numeric." | |
| Password2 | Required field | "Please fill in this field" notification pointed at input box | |
| | Must match password1 | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "The two password fields didn’t match." | |


### Login form

| Input Field | Requirement | Error caught | Final check |
| --- | ----- | ---- | -- |
| Pen name | Required field | "Please fill in this field" notification pointed at input box | |
| | Pen name matches a registered username | Message displayed under login title: "Details given do not match a registered user" | |
| Password | Required field | "Please fill in this field" notification pointed at input box | |
| | Password matches password for pen name given | Message displayed under login title: "Details given do not match a registered user" | |


### Contact us (New User Experience)

| Input Field | Requirement | Error caught | Final check |
| --- | ----- | ---- | -- |
| First Name | Required field | "Please fill in this field" notification pointed at input box | |
| | Maximum length 12 | Cannot physically enter more than 12 characters | |
| Last Name | Required field | "Please fill in this field" notification pointed at input box | |
| | Maximum length 20 | Cannot physically enter more than 20 characters | |
| Email | Recognisable as an email address | "Please include an @ in the email address" notification pointed at input box | |
| | | "Please enter a part following the @" notification pointed at input box | |
| | | "Please enter a part followed by @" notification pointed at input box | |
| | Maximum length 320 | Cannot physically enter more than 320 characters | |
| Message | Required field | "Please fill in this field" notification pointed at input box | |
| | Maximum length 1500 | Cannot physically enter more than 1500 characters | |


## Accessibility Testing

[Return to contents list](#contents)

## Lighthouse

[Return to contents list](#contents)

## Responsive Testing

[Return to contents list](#contents)

## Compatibility Testing

[Return to contents list](#contents)