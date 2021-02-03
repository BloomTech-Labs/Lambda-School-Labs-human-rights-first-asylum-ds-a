# Labs DS template
# Asylum Decision Database -- Human Rights First
An application to assist immigration advocates in winning asylum cases

[Docs](https://docs.labs.lambdaschool.com/data-science/)

## Description
We built an application for human rights first, a 501(c)3 organization. Our application uses optical character recognition to scan input court decisions for such values as the name of the presiding judge, the decision, and the asylum seeker's country of origin, and inserts these values into a database. The hope is that advocates for asylum seekers can use these data to better tailor their arguments before a particular judge and maximize their client's chances of receiving asylum. To use the application offline, follow the steps under Installation.


## Process
* We received some foundation documents from Human Rights First to start building the database and then scraped more pdf documents of asylum cases of the internet.

* Each pdf document was read in through optical character recognition (OCR), and converted the corresponding text to plain text which will allow us to search through each document and retrieve the judge’s name.

* Create an API connecting the database to the front end with the result that uploaded case files can be inserted into the database

* After converting the uploaded PDF to text, we will extract relvant entities from the text to store relevant features in a DB to facilitate data recall and analysis


## Tools

 * [Pytesseract](https://github.com/madmaze/pytesseract)
 * [FastAPI](https://github.com/tiangolo/fastapi)
 * [SQLAlchemy](https://www.sqlalchemy.org/)
 * [PDF2Image](https://pypi.org/project/pdf2image/)
 * [Pillow](https://pillow.readthedocs.io/en/stable/)
 * [Pandas](https://pandas.pydata.org/)


## Installation

 After cloning the repository, in your command line run the following commands:
 ```
 cd Lambda-School-Labs-human-rights-first-asylum-ds-a/
 pipenv install --dev
 pipenv shell
 uvicorn app.main:app --reload
 ```
 Then open localhost:8000 in your browser. The application should be running. 

 ## Contributors

 [Steven Lee](https://github.com/StevenBryceLee)

 [Tristan Brown](https://github.com/Tristan-Brown1096)

 [Liam Cloud Hogan](https://github.com/liam-cloud-hogan)

 [Edwina Palmer](https://github.com/edwinapalmer)

 [Jeremy Spradlin](https://github.com/JeremySpradlin)
 
 [Mahmoud Fansha](https://github.com/fansha1994)

## Future Work | State of Repo

The DS team A repo is light on functionality at present, as much of our project time was spent troubleshooting issues and cleaning existing code and correcting/adding to documentation.  Hopefully, you guys will have less confusion at the start than we did, and be able to start digging into, and adding to code much faster than we were.  What little is in the app is currently working, and below is the current state of the code repo:

OCR.py - Optical Character Recognition.  This file currently contains the packages and API hook for uploading a PDF, converting it to text, and returning the text wrapped in JSON.
- TODO: Continue research from the notebooks on entity recognition to create the next part of the pipeline, extracting out the relevant entity information from the text, inserting it into the relevant db object, and sending it to the db

DB.py - Database file.  This file contains the function that returns a database connection that can be used for sending SQL to the database.  It also contains the database class objects for DS.

ROUTES.py - Currently there are only two API hooks here;
- /test
Returns all saved entries in the ‘case’ table (currently only 1 test entry)

- /dbtest
Returns a list of the database table names

Notebooks/ - Contains the working notebooks we have been using to experiment and test with.  Messy, but worth looking through to see what we’ve been working with for entity recognition.
Also contains a folder with a design doc showing the basic API diagram as designed so far.

Next Steps: The biggest chunk of work right now probably lies in figuring out the heuristics for entity extraction from the text.  You’ll see in other portions the issues with getting proper PDFs that contain the information we’re supposed to scrape from other portions which only make this more difficult, as any heuristics that might work on extracting relevant information from the appellate cases may not be sufficient for the IC cases.  

We also ran into a lot of issues with attempting to deploy to beanstalk.  We’ve cleaned out most of the repo that was causing issues with deployment, however beanstalk still didn’t like it and it might be worth trying to deploy to Heroku instead. Recommended tutorial for deploying to Heroku can be found [here](https://docs.labs.lambdaschool.com/ds-bw/units-3-and-4/plotly-dash).

As I said, this is a challenging project for DS.  Doing stuff we’ve never done with data we never get:).  The entity recognition stuff is very interesting however.  Good luck!

 ## License

 This project is licensed under the terms of the MIT license.
