pip install pipenv
pipenv install
pipenv run python manage.py migrate
pipenv run python manage.py loaddata fixture.json
