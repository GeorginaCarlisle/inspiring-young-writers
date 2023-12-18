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
| 2 | As a **new user** I can read work written by another child | When first landing on the site I can read a piece of published writing from the platform | PASS | |
| | | The writing is displayed directly under the platform title and call to action, so that I don't miss it | PASS | |
| | | Only writing specifically chosen to be featured is displayed | PASS | |
| | | The writing is referenced under a heading 'This week's featured article:' | PASS | |
| | | The writing includes title, author, author's age and the writing | PASS | |
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
| 13 | As a **registered user** (with the help of my parent) I can reset my password using a link sent to my parent’s email | The login page has a clear link for 'Forgotten Password' | PASS | |
| | | Clicking on 'Forgotten Password' takes me to a 'Password reset' page where I can enter the email address linked to my account | PASS | |
| | | On submitting I am taken to a success message | PASS | |
| | | I also receive an email with a link to reset my password | PASS | |
| | | Clicking on the link takes me to the platform and a form to reset my password | PASS | |
| | | On reseting my password I receive a success message with a link to login | PASS | |
| 14 | As a **signed-in user** I can edit my profile | | | |
| | | | | |
| 15 | As a **signed-in user** I can delete my account | | | |
| | | | | |
| 16 | As the **parent of a registered user** I am informed of any profile changes my child makes and my consent to any changes is required | | | |
| | | | | |
| 17 | As the **site admin** I can remove accounts | As a site admin I can log in to the admin side of the site | PASS | |
| | | I can click to bring up a list of all registered users | PASS | |
| | | I can click to delete a selected user | PASS | |
| | | I am asked to confirm this action before it will be carried out | PASS | |
| 18 | As the **parent of a registered user** I am informed via email if my child’s account has been removed including the reason why | As site Admin I can handle this manually | PASS | |
| | | When deleting a user account I can see all the details I need: email address, first name and last name of the parent or guardian | PASS | |
| 19 | As a **signed-in user** user once logged in I am taken to a home page for my account | The top left of the nav bar lets me know I am signed in to my account with wording unique to me "Pen name's inspiring writing" | PASS | |
| | | The navigation bar provides links to all the registered user features |  PASS | |
| | | It is easy and intuitive to navigate through the available features | PASS | |
| | | A clear title welcomes me to my account | PASS | |
| | | There are clear buttons to take me straight to important areas of the site | PASS | |
| | | The page cannot be accessed unless logged in | PASS | |
| 20 | As a **signed-in user** I am provided with tips on how I can use the platform when I first log in to my account | | | |
| | | | | |
| 21 | As a **signed-in user** I am informed when page link errors occur and provided with a link straight back to my account home page | When I am logged in the link from the 404 page takes me back to my account_home page | PASS | |
| 22 | As the **parent of a signed-in user** I can also access the information for parents when my child is logged in | | | |
| | | | | |
| 23 | As the **parent of a signed-in user** I can also contact the site admin when my child is logged in | | | |
| | | | | |
| 24 | As a **signed-in user** I can navigate to a page where all my work is listed by status | I can navigate to my work from the navigation bar | PASS | |
| | | I can navigate to my work from a call to action button on my account home page | PASS | |
| | | A title shows me that I am in the 'My Work' section of the platform | PASS | |
| | | I am shown a list of all my saved work | PASS | |
| | | The list is categorised by published work, work awaiting approval and drafts | PASS | |
| | | There is a clear button that takes me to the create writing page | PASS | |
| | | The page cannot be accessed unless logged in | PASS | |
| | | Users cannot accidentally access someone else's work | PASS | |
| 25 | As a **signed-in user** I am provided with tips and ideas for the sort of work I could create | | | |
| | | | | |
| 26 | As a **signed-in user** I can write and submit a piece of work with title | From the account home page there is a clear button I can click that will take me directly to a page for inputting new work | PASS | |
| | | The design of the page is pleasing to the eye and doesn't distract | PASS | |
| | | The title and placeholder text help me to navigate the process of submitting my work | PASS | |
| | | The button to submit my work for publishing is clear | PASS | |
| | | I am given feedback to ensure that I am filling in the form correctly | PASS | |
| | | On clicking the submit button, I am asked to confirm that I would like to submit my work to be published. This includes a quick explanation of the process | PASS | |
| | | I am given clear feedback to let me know I have successfully submitted my work to be published on the site | PASS | |
| | | On submission I am redirected to the account_home page | PASS | |
| 27 | As a **signed-in user** my writing is passed through validation tests before it is saved | An error message is raised when a swear word is entered in the pen-name field | PASS | |
| | | An error message is raised when a swear word is entered in the title field both during writing creation and editing | PASS | |
| | | An error message is raised when a swear word is entered in the body field both during writing creation and editing | PASS | |
| 28 | As a **signed-in user** I can write a blurb for my writing | | | |
| | | | | |
| 29 | As a **signed-in user** I can attach a picture to my writing | | | |
| | | | | |
| 30 | As a **signed-in user** I can save a draft of my work | When creating new work I have the option to save a draft version of my work | PASS | |
| | | The button to save as a draft is clear | PASS | |
| | | I am given feedback to ensure that I am filling in the form correctly | PASS | |
| | | I am given clear feedback to let me know I have successfully saved my work as a draft | PASS | |
| | | On submission I am redirected to the account_home page | PASS | |
| 31 | As a **signed-in user** I can view my published work | When in 'My Work' clicking on the title of a piece of writing listed under 'My Published Work' will take me to a view_work page | PASS | |
| | | The design of the page is pleasing to the eye and doesn't distract | PASS | |
| | | 'title', 'date published' and 'writing' all displayed and easy to read | PASS | |
| | | A back button (x) to return to 'My Work' | PASS | |
| | | There are two clear options - edit writing and delete writing | PASS | |
| | | Clicking 'edit writing' takes me to the edit_writing page with a message unique to editing published work | PASS | |
| | | Clicking to 'delete' my writing passes all user story USER STORY #34 criteria | PASS | |
| 32 | As a **signed-in user** I can view and edit any work pending approval | When in 'My Work' clicking on the title of a piece of writing listed under 'My Work Awaiting Approval' will take me to a view page | PASS | |
| | | The design of the page is pleasing to the eye and doesn't distract | PASS | |
| | | The view work page displays the 'title', 'date submitted', 'writing' and a message | PASS | |
| | | An x in the top right of the container takes me back to 'My Work' | PASS | |
| | | The view work page has two buttons 'edit writing' and 'delete writing' | PASS | |
| | | Clicking to 'edit writing' takes me into the edit view with a message specific to work pending approval | PASS | |
| | | Editing my work passes all user story #33 criteria | PASS | |
| | | Clicking to 'delete' my writing passes all user story USER STORY #34 criteria | PASS | |
| 33 | As a **signed-in user** I can view and edit my draft work | When in 'My Work' clicking on the title of a piece of writing listed under 'My Drafts' will take me to an edit page | PASS | |
| | | The design of the page is pleasing to the eye and doesn't distract | PASS | |
| | | The draft work is displayed in a form allowing me to edit the title and or the writing | PASS | |
| | | The form title and introduction help me to navigate the process of editing my work | PASS | |
| | | There are three clear options - save draft, submit for publishing, delete writing | PASS | |
| | | Save draft and submit for publishing function as per user stories #26 and #30 | PASS | |
| | | Delete writing as per user story #34 | PASS | |
| | | An x in the top right of the container takes me back to 'My Work' | PASS | |
| | | On clicking the x I am asked to confirm that there are no changes I wish to save | PASS | |
| 34 | As a **signed-in user** I can delete my writing | Delete is an option I can access when editing or viewing my writing | PASS | |
| | | I am reminded that once deleted I cannot get my writing back | PASS | |
| | | I can confirm to delete or choose to keep | PASS | |
| | | On choosing to delete my writing is deleted and I am returned to 'My work' with a success message | PASS | |
| | | On choosing to keep I am return to editing or viewing my writing | | |
| 35 | As the **site admin** all stories need to be validated by me before they are posted to the page | I can view all instances of writing through the admin page | PASS | |
| | | I can filter writing by pending_approval | PASS | |
| | | I can read the title, body and author of each instance of writing | PASS | |
| | | I can checkbox to change approved to True (default is False) and input the date | PASS | |
| | | Only writing with approved True will be displayed in the library | PASS| |
| | | I can also checkbox to change featured to True (default is false) | PASS | |
| | | Only writing with approved True and featured True will be displayed on the landing page for all visitors to read | PASS | |
| 36 | As the **site admin** I am informed when a child submits their writing for approval | | | |
| | | | | |
| 37 | As the **site admin** I can send a message to the user should their writing fail to meet approval guidelines | When reviewing writing pending approval I can check the failed_approval box should the writing not meet requirements and add the date and time to date_failed | PASS | |
| | | I can add details to the reason_failed field to be passed back to the user | PASS | |
| | | Any writing failing approval is listed in the users "My Work page" under the heading "Submitted work that does not meet publishing requirements" | PASS | |
| | | Message from reason_failed field is displayed under the title and date reviewed on | PASS | |
| 38 | As the **site admin** I can send parents an email sharing the submitted story and the reason why it failed to meet approval | As site Admin I can handle this manually | PASS | |
| | | When failing a submission I can see the author name for the writing being failed | PASS | |
| | | I can locate the details for the author and find the information I need: email, first_name and last_name of parent/guardian | PASS | |
| 39 | As the **site admin** I can remove approved status from previously approved work | I can view all instances of writing through the admin page | PASS | |
| | | I can filter writing by approved | PASS | |
| | | I can checkbox to change approved to False | PASS | |
| | | Only writing with approved True will be displayed in the library | PASS | |
| | | I can checkbox to change failed_approval to True (default is False) and add a date to date_failed | PASS | |
| 40 | As a **signed-in user** I can view work from other users | I can navigate to the library of inspiration from the navigation bar | PASS | |
| | | I can navigate to the library from a call to action button on my account home page | PASS | |
| | | The design of the page is pleasing to the eye and doesn't distract | PASS | |
| | | A title shows me that I am in the 'Library of inspiration' section of the platform | PASS | |
| | | I am shown a list of all published work | PASS | |
| | | For each piece of work I can read the 'title', 'author', 'age of author' and 'date published' | PASS | |
| | | The list is ordered by most recent first | PASS | |
| | | Clicking on the title brings the writing up so that I can read it | PASS | |
| | | In the read view I can click an x to take me back to the library | PASS | |
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
| 53 | As a **signed-in user** I can edit my published work | When viewing my published work I can click a button to 'Edit writing' | PASS | |
| | | Clicking to 'Edit writing' takes me to the Edit Writing page | PASS | |
| | | I am given a message specific to editing published work | PASS | |
| | | Editing my work passes all user story #33 criteria | PASS | |
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

The following documents all forms and any requirements needed, with details on how requirements are handled. 

### Sign-up form

| Input Field | Requirement | How error caught | Final check |
| --- | ----- | ---- | -- |
| Pen name | Required field | "Please fill in this field" notification pointed at input box | |
| | Unique name required | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "User with this Username already exists." | |
| | Text only no numbers | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "Only letters and spaces are allowed in your Pen name" | |
| | Maximum length 20 | Cannot physically enter more than 20 characters | |
| | No swear words | If swear word entered is on the validation list the following message is displayed "Swear word ' ' is not allowed. Please remove. | |
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


### Create Writing

| Input Field | Requirement | Error caught | Final check |
| --- | ----- | ---- | -- |
| Title | Required field | "Please fill in this field" notification pointed at input box | |
| | Maximum length 50 | Cannot physically enter more than 50 characters | |
| | Minimum length 3 | Message displayed under 'Create Writing' title: "Your title needs to more than 3 characters long to be published. Please add a little more." | |
| | Unique | Message displayed under 'Create Writing' title: "Your title must be unique and there is already work with this title. Please make a change to your title and try again."| |
| | No swear words | If swear word entered is on the validation list the following message is displayed "Swear word ' ' is not allowed. Please remove. | |
| Body | Required field | "Please fill in this field" notification pointed at input box | |
| | Minimum length 50 | Message displayed under 'Create Writing' title: "Your writing needs to more than 50 characters long to be published. Please add a little more." | |
| | No swear words | If swear word entered is on the validation list the following message is displayed "Swear word ' ' is not allowed. Please remove. | |

#### Create writing confirms 'submit to be published'

| Trigger | Expected Response | 1st Check | Final Check |
| --- | --- | --- | --- |
| Click to submit work to be published | Confirmation message and two buttons 'Confirm' 'save as draft' | PASS | |
| Click to confirm | Redirect to 'My Work' with "You have successfully submitted your writing to be published" message displayed. Writing correctly saved with pending_approval = True | PASS | |
| Click to save as draft | Redirect to 'My Work' with "You have successfully saved your writing as a draft" message displayed. Writing correctly saved with pending_approval = False | PASS | |

#### Create writing confirms 'back' button

| Trigger | Expected Response | 1st Check | Final Check |
| --- | --- | --- | --- |
| Clicking the 'x' to come out of the create view | Confirmation message and two buttons 'keep creating' and 'head back' | PASS | |
| Clicking 'keep creating' | In the create view with the confirmation message and associated buttons gone and no changes to writing lost | PASS | |
| Clicking 'Head back' | Returned to the My Work view | PASS | |

### Edit Writing

| Input Field | Requirement | Error caught | Final check |
| --- | ----- | ---- | -- |
| Title | Required field | "Please fill in this field" notification pointed at input box | |
| | Maximum length 50 | Cannot physically enter more than 50 characters | |
| | Minimum length 3 | Message displayed under 'Create Writing' title: "Your title needs to more than 3 characters long to be published. Please add a little more." | |
| | No swear words | If swear word entered is on the validation list the following message is displayed "Swear word ' ' is not allowed. Please remove. | |
| Body | Required field | "Please fill in this field" notification pointed at input box | |
| | Minimum length 50 | Message displayed under 'Create Writing' title: "Your writing needs to more than 50 characters long to be published. Please add a little more." | |
| | No swear words | If swear word entered is on the validation list the following message is displayed "Swear word ' ' is not allowed. Please remove. | |

#### Edit writing confirms 'submit to be published'

| Trigger | Expected Response | 1st Check | Final Check |
| --- | --- | --- | --- |
| Click to submit work to be published | Confirmation message and two buttons 'Confirm' 'save as draft' | PASS | |
| Click to confirm | Redirect to 'My Work' with "You have successfully submitted your writing to be published" message displayed. Writing correctly saved with pending_approval = True | PASS | |
| Click to save as draft | Redirect to 'My Work' with "You have successfully saved your writing as a draft" message displayed. Writing correctly saved with pending_approval = False | PASS | |

#### Edit writing confirms 'delete writing'

| Trigger | Expected Response | 1st Check | Final Check |
| --- | --- | --- | --- |
| Click to 'Delete Writing' | Confirmation message and two buttons 'Keep writing' and 'Delete writing' | PASS | |
| Click to 'Delete writing'| Redirect to 'My Work' with "You have successfully deleted your writing" message displayed. Writing has been deleted from the data base | PASS | |
| Click to 'Keep writing' | Redirect back to 'Edit Writing' | PASS | |

#### Edit writing confirms 'back' button

| Trigger | Expected Response | 1st Check | Final Check |
| --- | --- | --- | --- |
| Clicking the 'x' to come out of the edit view | Confirmation message and two buttons 'keep editing' and 'head back' | PASS | |
| Clicking 'keep editing' | In the edit view with the confirmation message and associated buttons gone and no changes to writing lost | PASS | |
| Clicking 'Head back' | Returned to the My Work view | PASS | |

### View writing

#### View writing confirm 'delete writing'

| Trigger | Expected Response | 1st Check | Final Check |
| --- | --- | --- | --- |
| Click to 'Delete Writing' | Confirmation message and two buttons 'Keep writing' and 'Delete writing' | PASS | |
| Click to 'Delete writing'| Redirect to 'My Work' with "You have successfully deleted your writing" message displayed. Writing has been deleted from the data base | PASS | |
| Click to 'Keep writing' | Redirect back to 'View Writing' | PASS | |


### Send password reset email

| Input Field | Requirement | Error caught | Final check |
| --- | ----- | ---- | -- |
| Email | Required field | "Please fill in this field" notification pointed at input box | |

### Reset password

| Input Field | Requirement | Error caught | Final check |
| --- | ----- | ---- | -- |
| Password1 | Required field | "Please fill in this field" notification pointed at input box | |
| | Can't be too similar to other personal information | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "The password is too similar to the username." | |
| | Must contain at least 8 characters | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "This password is too short. It must contain at least 8 characters." | |
| | Can't be a commonly used password | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "This password is too common." | |
| | Can't be entirely numeric | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "This password is entirely numeric." | |
| Password2 | Required field | "Please fill in this field" notification pointed at input box | |
| | Must match password1 | Messages displayed under sign-up title: "Form not valid. Please correct before clicking to signup" and "The two password fields didn’t match." | |

## Accessibility Testing

[Return to contents list](#contents)

## Lighthouse

[Return to contents list](#contents)

## Responsive Testing

[Return to contents list](#contents)

## Compatibility Testing

[Return to contents list](#contents)