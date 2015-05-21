To install locally, start at the root directory of the cloned repo and:

    virtualenv venv
    ./venv/bin/pip install -r requirements.txt
    ./venv/bin/python manage.py migrate

Then, to run the server locally:

    ./venv/bin/python manage.py runserver

And check out the admin at

    localhost:8000/admin/

Run the tests with

    ./venv/bin/python manage.py test
