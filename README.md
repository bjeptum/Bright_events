## Bright Events 

### Introduction

Bright Events is a platform for event organizers to create and manage different types of events.

### The Context

As a mom, I often find myself juggling the demands of family life while trying to plan events-be it a birthday party, family-get-together and community events. I realized how hard it can be from managing RSVPs, scheduling the events and ensuring you never miss out the nitty gritties,this inspired me to build Bright Events.

The journey began with the motivation of finally building an application on my own from scratch. My goal was centered on being able to complete the application for my learning towards becoming a software engineer for the [ALX -Software Engineering Foundations](https://www.alxafrica.com/learn/programming-development/) program.

### The Team

I worked on this project solely.
Follow me on [LinkedIn](https://www.linkedin.com/in/brenda-jeptum-8bab79120/)

### Usage

The project is entirely for educational purposes with no intention to release it for use by the public. However, in an ideal scenario, it would be used by event organizers as well as attendees  to have a one stop for registration and managing the logistics of an  event/events. Bright Events is open to be used in any locality.

### Product Features

- Users can create an account and log in
- Users can create, view, update and delete an event
- Users can RSVP to an event
- Users can view who will be attending their event
- Users can search for events based on event location or event category

## Installation

The project is not deployed butcan be used locally following the below steps:

    #### Ubuntu Terminal:

1.  Clone the repository

`
    git clone git@github.com:bjeptum/Bright_Events.git
    `
    
2. Navigate to the project directory 

`
    cd Bright_Events/backend
    `
    
3. Setup a virtual environment
   
`
    python3 -m venv myenv
    source myenv/bin/activate
    `

    
    /* Note: to deactivate the environment type deactivate */
   
4. Install dependencies

   `
   pip install -r requirements.txt
   `
   
5. Set Up Environment Variables

   - Create a .env file in the root directory
   - Add required enviroment variables for example:
  
  ` 
  FLASK_APP=backend/app
  FLASK_ENV=development
  DATABASE_URL=sqlite:///app.db
  SECRET_KEY=your_secret_key
  `
  
6. Run the Flask application
   
 `
 python3 run.py
 `
 
7. Navigate to your web browser and have at it
 
`
http://127.0.0.1:5000/
`

### Blog Post

Upon completion of the development phase of Bright Event, I wrote a blog post of my experience.

[........](...)


### Contribution 

Jeptum Brenda is the only contributor at this time.

### Related Projects

- [Alprojectdesign](https://www.alprojectsdesign.com/en/home/)
- [Waridi Events](https://www.waridievents.com/)


### Licensing

Totally free but give me credit.


