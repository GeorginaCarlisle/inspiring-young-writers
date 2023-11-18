# Inspiring Young Writers

Developer: Georgina Carlisle

Image showing deployed project to go here.

Inspiring Young Writers is a platform specifically designed for children aged 8 - 12 to share their writing and give and gain feedback.

Project currently under development and no live link available.


## Contents

[Design](#design)

- [The Strategy Plane](#the-strategy-plane)

- [The Scope Plane](#the-scope-plane)

- [The Structure Plane](#the-structure-plane)

- [The Skeleton Plane](#the-skeleton-plane)

- [The Surface Plane](#the-surface-plane)

[Agile Methodology](#agile-methodology)

[Features](#features)

- [Existing Features](#existing-features)

- [Future Features](#future-features)

[Languages](#languages)

[Tools and Technologies](#tools-and-technologies)

[Testing and Validation](#testing-and-validation)

[Bugs and Fixes](#bugs-and-fixes)

[Deployment](#deployment)

[Credits](#credits)

[Acknowledgements](#acknowledgements)

---

## Design

### The Strategy Plane

#### Target User Group

Children who can write and specifically children aged 8 – 12.

They can:

- Use a keyboard to type.
- Spell words, put together sentences and build a larger piece of writing.
- Articulate simple concepts or ideas through the written word.

However, they are still developing the skills needed to:

-	Articulate clearly more complex thoughts, ideas and concepts through the written word.
-	Write for the reader and include details that will allow the reader to fully understand the story/concept etc.
-	Build narratives that flow, with the story they are telling working together as a whole.


#### Problem Background

Becoming an articulate writer and being able to tell a story (whether fiction or non-fiction) for an audience is a complex skill that takes time and practice to master. As with any skill, it is practice, exposure and feedback that leads to progress. 

Primary schools do an amazing job of helping children to progress with their writing. However, while children get plenty of chance to practice writing at school, their writing is usually accompanied by restriction (a theme, writing style, time limit, particular language construct to be focused on) and even the environment of a classroom can provide further restriction. 

Where then can children build in this practice of writing for an audience in a less restricted way? Where can they share their writing and gain feedback, motivation, inspiration, and exposure to stories written by those at a similar skill level to them?

There are plenty of writing competitions for children and magazines where they can send stories. However, these again often come with restrictions (theme, word count, deadline) and often don’t lend themselves to a child being able to continually share new stores and quickly gain feedback.


#### Problem Statement

“I am a child who has the potential to become a fantastic writer, however a lack of opportunity to share and gain feedback from writing created purely for pleasure means I have less motivation and reason to write. I therefore write less and gain less feedback which ultimately means my progression is less than it could be.”


#### Project Aim

This project aims to provide children aged 8 - 12 with a safe space where they can share their writing - created for pleasure without restriction - and gain feedback.


#### Safety Considerations

As this project is aimed at children, extra thought needs to be given to making sure the space provided for them to share their writing in is safe. 

Two main areas of danger will be considered throughout this project:

-	The danger of children being exposed to material or comments that are inappropriate or may cause harm.
-	The danger of someone being able to contact and connect with a child (whether in the space or outside via the gaining of contact information) which then leaves them vulnerable to abuse.

[Return to contents list](#contents)

---

### The Scope Plane

The scope of this project is provided by user stories, organised below by epic and then role.


#### EPIC - New User Experience

<details>
<summary>
View User Stories
</summary>

As a **new user** the website is clearly geared towards children age 8 - 12 and sharing writing, so that I know what the website is about and that it is suitable for me. (1)

As a **new user** I can read work written by another child so that I am inspired to write and share my writing. (2)

As a **new user** I am given clear information on what registered users can do, so that I know what signing up will allow me to see and do. (3)

As the **parent of a new user** I am provided with information which details how the site works, the steps in place to protect my child and what me and my child can do to increase safety, so that I am fully aware of how the site works. (4)

As the **parent of a new user** I can contact the site admin, so that I can raise any concerns or ask any questions about the site. (5)

As the **site admin** user's question and concerns along with their contact details are passed to me, so that I can then respond. (6)

As a **new user** I am provided with the name and contact links for the developer who created this platform, so that I know who created the platform and how to get in touch with them. (7)

As a **new user** I am informed when page link errors occur and provided with a link straight back to the landing page, so that my experience is disrupted as little as possible and I understand what has happened. (8)

</details>


#### EPIC - Authentication

<details>
<summary>
View User Stories
</summary>

As a **new user** I can easily set up an account, so that I can access registered user only content and share my stories. (9)

As the **parent of a new user** I am asked to input my name and email address and give consent for my child joining the site so I can take a full role in my child’s participation on the platform. (10)

As a **registered user** I can use my pen-name and password to login to my account, so that my account remains secure and only I can login. (11)

As a **signed-in user** I can easily logout of my account, so that I can keep my account secure. (12)

As a **registered user** (with the help of my parent) I can reset my password using a link sent to my parent’s email, so that if I forget my password I can still login to my account. (13)

</details>


#### EPIC - Profile Management

<details>
<summary>
View User Stories
</summary>

As a **signed-in user** I can edit my profile so that I can update my details. (14)

As a **signed-in user** I can delete my account, so that I can remove all my contributions and details from the platform should I wish. (15)

As the **parent of a registered user** I am informed of any profile changes my child makes and my consent to any changes is required, so that I can continue to support my child. (16)

As the **site admin** I can remove accounts, so that I can prevent unsuitable users from accessing and using the platform. (17)

As the **parent of a registered user** I am informed via email if my child’s account has been removed including the reason why, so that I can support my child to understand what has happened. (18)

</details>


#### EPIC - Account Home

<details>
<summary>
View User Stories
</summary>

As a **signed-in user** user once logged in I am taken to a home page for my account, so that I have access to all the registered user features and it is clear I am logged in to my account. (19)

As a **signed-in user** I am provided with tips on how I can use the platform when I first log in to my account, so that I understand how to use the platform. (20)

As a **signed-in user** I am informed when page link errors occur and provided with a link straight back to my account home page, so that my experience is disrupted as little as possible and I understand what has happened. (21)

As the **parent of a signed-in user** I can also access the information for parents when my child is logged in, so that I can always access that information should I need it. (22)

As the **parent of a signed-in user** I can also contact the site admin when my child is logged in, so that there is always an easy to access way to contact the site admin. (23)

</details>


#### EPIC - My Work

<details>
<summary>
View User Stories
</summary>

As a **signed-in user** I can navigate to a page where all my work is listed by status, so that I can quickly view all my work and see its current status. (24)

As a **signed-in user** I am provided with tips and ideas for the sort of work I could create, so that I know I am not restricted and can submit a wide range of genres and text types. (25)

As a **signed-in user** I can write and submit a piece of work with title, so that I can share my writing with others. (26)

As a **signed-in user** my writing is passed through validation tests before it is saved, so that any text that may cause harm is prevented from entering the platform. (27)

As a **signed-in user** I can write a blurb for my writing, so that I can entice other readers to read my work. (28)

As a **signed-in user** I can attach a picture to my writing, so that I can entice other readers to read my work by giving them a quick glimpse of what it might be about. (29)

As a **signed-in user** I can save a draft of my work so that I can continue to work on it another time. (30)

As a **signed-in user** I can view my published work, so that I can re-read my writing. (31)

As a **signed-in user** I can view and edit any work pending approval, so that I can re-read and edit should I wish. (32)

As a **signed-in user** I can view and edit my draft work, so that I can continue building on my writing. (33)

As a **signed-in user** I can delete my writing, so that I can remove any of my writing that is saved on the platform should I wish. (34)

</details>


#### EPIC - Approval of writing

<details>
<summary>
View User Stories
</summary>

As the **site admin** all stories need to be validated by me before they are posted to the page, so that I can ensure no inappropriate material is posted to the site. (35)

As the **site admin** I am informed when a child submits their writing for approval, so that I can respond to the request in a timely fashion. (36)

As the **site admin** I can send a message to the user should their writing fail to meet approval guidelines, so that I can keep users informed. (37)

As the **site admin** I can send parents an email sharing the submitted story and the reason why it failed to meet approval, so that I can keep parents informed and provide them with the information needed to support their child to keep other users on the site safe. (38)

As the **site admin** I can remove approved status from previously approved work, so that I can respond to any concerns raised post approval. (39)

</details>


#### EPIC - Library of Published work

<details>
<summary>
View User Stories
</summary>

As a **signed-in user** I can view work from other users, so that I can gain inspiration and tips for my own writing. (40)

As a **signed-in user** I can filter work, so that I can more easily find stories that I am interested in. (41)

As a **signed-in user** I can click a help button should I see/read something I don’t like, so that I can keep myself safe. (42)

As the **parent of a signed-in user** my child is prompted to seek out my guidance should they see/read something they don’t like, so that I can support them and then proceed as appropriate. (43)

As the **parent of a signed-in user** I can raise concern about a specific piece of writing, so that I can help keep my child and others safe. (44)

As the **site admin** I am alerted immediately to any raised concerns, so that I can respond swiftly. (45)

</details>


#### EPIC - Feedback

<details>
<summary>
View User Stories
</summary>

As a **signed-in user** I can give feedback to other users, so that I can support my peers. (46)

As a **signed-in user** I can view all feedback associated with a piece of work, so that I can gain tips to improve my own writing. (47)

As a **signed-in user** my feedback is passed through validation tests, so that I don’t cause harm to another user. (48)

As a **signed-in user** I can edit my feedback, so that I can resolve a mistake should I make one. (49)

As a **signed-in user** I can delete my feedback, so that I can remove my comments should I wish to. (50)

As a **signed-in user** I am alerted to any new feedback on my published work, so that I don’t miss any feedback. (51)

As a **signed-in user** I can view feedback given to me by other users, so that I can grow in confidence and improve as a writer. (52)

As a **signed-in user** I can edit my published work, so that I can make changes in response to feedback should I wish. (53)

As a **signed-in user** I can delete feedback given to me by other users, so that I can control the feedback that is associated with my work. (54)

As a **signed-in user** I can click a help button should I see something in the feedback that worries me, so that I can keep myself safe. (55)

As the **parent of a signed-in user** my child is prompted to seek out my guidance should they see/read something in the feedback that worries them, so that I can support them and then proceed as appropriate. (56)

As the **parent of a signed-in user** I can raise concern about a specific piece of feedback, so that I can help keep my child and others safe. (57)

As the **site admin** I am alerted immediately to any raised concerns about feedback, so that I can respond swiftly. (58)

As the **site admin** I can remove inappropriate feedback, so that I can keep users safe. (59)

As the **site admin** I can send parents an email sharing posted feedback and the reason it has been removed, so that I can keep parents informed and provide them with the information needed to support their child to keep other users on the site safe. (60)

</details>


[Return to contents list](#contents)

---

### The Structure Plane

[Return to contents list](#contents)


### The Skeleton Plane

[Return to contents list](#contents)


### The Surface Plane

[Return to contents list](#contents)


## Agile Methodology

[Return to contents list](#contents)


## Features

### Existing Features

[Return to contents list](#contents)


### Future Features

[Return to contents list](#contents)


## Languages

[Return to contents list](#contents)


## Tools and Technologies

Tools and technologies are listed in order of use during the development of this project.

[Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template) - Provided me with a familiar base from which to build my project.

[GitHub](https://github.com/) - Stores the repository for this project so that it can be viewed by others.

[git](https://git-scm.com/) - Controlled the building of this project in a series of versions which can be tracked.

[Visual Studio Code](https://code.visualstudio.com/) - The editor in which this project has been built. The following extentions were installed and used: Markdown Preview Enhanced

[Return to contents list](#contents)


## Testing and Validation

[Return to contents list](#contents)


## Bugs and Fixes

[Return to contents list](#contents)


## Deployment

[Return to contents list](#contents)


## Credits

[Return to contents list](#contents)


## Acknowledgements

[Code Institue](https://codeinstitute.net) - The majority of the coding skills, knowledge and understanding showcased in this project have been learnt through the 'Diploma of Full stack software development' that I am completing with Code Institute.

### Websites, articles and tutorials

The following websites, articles and tutorials are listed in order of use during the development of this project.

[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) - I followed the structure given in this article for my commit messages.

[Return to contents list](#contents)
