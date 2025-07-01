# Flask Portfolio Website for Malyavantham Naresh

## Project Description
A personal portfolio website built with Flask that showcases my skills, education, experience, projects, and contact information. The website features responsive design and navigation between different sections.

## Features
- Responsive design that works on all devices
- Multiple sections (About, Education, Skills, Experience, Projects, Contact)
- Functional contact form
- Clean, professional layout
- Easy navigation

## Technologies Used
- Python 3.x
- Flask web framework
- HTML5
- CSS3

## Installation Instructions

1. Clone the repository:
   
   git clone [repository-url]
   cd portfolio
   

2. Create a virtual environment (recommended):
   
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   

3. Install dependencies:
   
   pip install -r requirements.txt
   

4. Run the application:
   
   python app.py
   

5. Open your browser and visit:
   
   http://localhost:5000
   

## Project Structure

1-07-2025/
├── portfoilo.py                # Main Flask application
├── static/
│   └── style.css         # CSS stylesheet
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── about.html        # About me page
│   ├── education.html    # Education page
│   ├── skills.html       # Skills page
│   ├── experience.html   # Experience page
│   ├── projects.html     # Projects page
│   └── contact.html      # Contact page
└── requirements.txt      # Python dependencies

## Customization
To customize this portfolio:
1. Update the content in the HTML templates
2. Modify the CSS in static/style.css
3. Add your own images to the static folder if needed
4. Update the contact form handler in app.py if you want to implement email functionality

## Contact
Malyavantham Naresh
Email: mailyavanthamnaresh15@gmail.com
Phone: 9392813045

This README file provides all the essential information about your project, including how to install and run it, the project structure, and customization options. You can place this file in the root directory of your project alongside the `portfoilo.py` file.