# Profs CS374 Database Project

Project Title: **madiSTEM Workshop Management (MWM)**

Team Name: **The Absent-Minded Professors**

Short Name: **profs**

Team Members: **Mona Rizvi, Chris Mayfield**

# Introduction

**madiSTEM** is an annual outreach event held at JMU for middle school girls (see [madiSTEM 2024](https://www.jmu.edu/mathstat/madistem/)).  During the event, the girls attend multiple STEM workshops organized by JMU faculty and students, as well as listen to presentations by women working in STEM fields.  The event can host up to 250 attendees, 20 workshops, 100+ volunteers, and 50+ organizers, workers, parents and guests.  Certain parts of this event’s management (including registration and scheduling) have already been automated. But the management of the workshops is still done by hand, using multiple spreadsheets and other documents, and several diverse communication tools that do not work together.

We propose to develop “madiSTEM Workshop Management” (MWM), a database application to support the planning and organization of madiSTEM workshops.  MWM will allow the workshop organizer to oversee the planning of workshops.  Workshop leaders will be able to log into the system to submit details about their workshop, including the title and description that will be posted on the madiSTEM website. The system will track the status of each workshop and facilitate scheduling, required materials, and other needs.

If after the design phase, the scope of this project is too small, we will focus on additional features to support madiSTEM, such as managing student volunteers and/or attendees.

# Primary System Entities

| SYSTEM ENTITY | ATTRIBUTES |
| :---- | :---- |
| Workshop | name, description, advertisement, size, space and tools requirements, etc. |
| Person | contact information, t-shirt size, lunch preference, type (e.g., student, faculty, other), role (e.g. leader, co-leader, mentor, assistant, volunteer), etc. |
| Room | location, size, capacity, equipment (e.g., computers, projectors, sink), etc. |

madiSTEM has run for many years, and we have a lot of historical workshop data. One aspect that we might explore for this project involves loading previous workshop descriptions into a library that current workshop leaders may use as a starting point for their workshops. We can also incorporate student feedback about the workshops to track participant interest over time and make recommendations to the conference organizers. The system can help visualize this data and allow users to search for previous and current workshops by keyword or topic.

# Primary System Users

| USER GROUP | ACTIVITIES & PERMISSIONS |
| :---- | :---- |
| Organizers | Administrator access to the system with the permission to edit any data. These are faculty who help run the conference and recruit other faculty to participate. |
| Workshop leaders | Can manage some of the data pertaining to their own workshop. For example, they can edit the title, description, or required materials (but not the room). |
| Other workshop staff | Can manage their personal data, such as how their name should be spelled on their name tag, what times they are available to run the workshop, etc. |

Currently all this information is sent over emails, sometimes at the last minute. We want to have a system where users can see their workshop information, make changes directly to the database (for their workshop only), see the assigned room number, and click a button to confirm the information is correct / ready to be published on the website. Having this database system will eliminate the need for dozens of emails and spreadsheets, simplify version control of the workshop data, and eliminate duplication of documents sent as email attachments.

# System Functionality

## People and Rooms

* Room information is maintained in the system, but only a subset of rooms may be available for a single madiSTEM event.
* Organizer information may remain in the system across years, but specific people have specific roles per madiSTEM event.
* Volunteer information is kept per event, even if the same person serves as a volunteer multiple times.

## Workshop Process

* Workshops are *proposed* for an event year, but a workshop may start as a copy of a previous year’s version of the same workshop.  Proposers may update the workshop attributes.
* A slate of workshops are *selected* for the current year’s madiSTEM, and the proposers agree.  Updates after the selection/acceptance must be made by the organizers.
* Workshops are *assigned* to rooms based on their needs.
* Multiple occurrences of each workshop are *scheduled* to specific time blocks and student attendee cohorts.
* Permanent and/or rotating volunteers are assigned to workshops.
* Workshops are *held* on the day of the event and evaluation data from the attendees is collected (on paper).  A scheduled workshop may not be held (in case of illness or other emergency).
* Survey data is collated and recorded for each workshop.
* Thank you letters are sent out to all workshop personnel, to all volunteers, and to all organizers, and cc’d to their others, depending on the type and role of the person.

# About the Team

**Mona Rizvi** is an Associate Professor of Computer Science at James Madison University. She received a Ph.D. in Computer Science from Old Dominion University. Before entering academia, she worked for nearly 20 years as a software engineer and technical manager. She designed large, complex databases (e.g. USAF Combat Operations database) and designed and developed numerous deployed applications. Her Ph.D. research was in wireless networking, and her later research is in computer science education.

**Chris Mayfield** is a Professor of Computer Science at James Madison University. His research focuses on CS education and faculty development at the undergraduate and high school levels. He currently has two NSF-funded projects: one that studies student engagement in CS1 (2216454) and one that supports high school CTE teachers (2219770). He received a Ph.D. in Computer Science from Purdue University and bachelor’s degrees in CS and German from the University of Utah.
