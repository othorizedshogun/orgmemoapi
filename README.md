# OrgMemoAPI

### Your Organisation Memo Api.

This is a Django Project

## How to run locally
1. Clone this Repository.
2. Open your terminal and create a Python Virtual Environment. (Make sure you have python installed on your computer)
3. Activate the virtual environment and run command: pip install -r requirements.txt.
4. Move to the cloned repo directory.
5. Run commands in this order:
    - python manage.py makemigrations
    - python mange.py migrate
    - python manage.py runserver
6. I would advise you have Postman installed for api requests.
    - GET http://localhost:8000/memos/ returns the memo list
    - POST http://localhost:8000/memos/ creates a new memo
        - id, slug, date fields do not have to be filled  as they are generated automaticallly upon new memo creation.
    - GET http://localhost:8000/memos/detail/slug returns the memo detail of the memo with the slug in the url 
        - slug is the memo's slug
    - PUT http://localhost:8000/memos/detail/slug/ updates the memo
    - DELETE http://localhost:8000/memos/detail/slug/ deletes the memo
7. Enjoy.

P.S: This is my second django project and I suck at HTML and CSS; please don't judge me.
Okay, I abandoned HTMl & CSS and created an API. 

