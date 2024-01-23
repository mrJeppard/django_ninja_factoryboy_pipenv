# django + django ninja + factory boy + poetry setup

An example django REST api setup.

### Installation
You'll need python3 and poetry installed to get going.

```bash
git clone https://github.com/mrJeppard/django_ninja_factoryboy_poetry.git

cd django_ninja_factoryboy_poetry && poetry install
```

### Run the server and interact with the swagger docs
```poetry run python manage.py makemigrations```

```poetry run python manage.py migrate```

```poetry run python manage.py create_user test@test.com password```

```poetry run python manage.py runserver```

Login via [localhost:8000/accounts/login](localhost:8000/accounts/login)

### Run the tests
`poetry run python manage.py test`



