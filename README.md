# django + django ninja + factory boy + pipenv setup
An example django RESTapi setup.

### Install
You'll need python3.8 installed to do the below.

```bash
git clone https://github.com/mrJeppard/django_ninja_factoryboy_pipenv.git

cd django_ninja_factoryboy_pipenv && pipenv install
```

### Run the server
`pipenv run python manage.py runserver`


#### Interact with the swagger docs
```pipenv run python manage.py create_user test@test.com password```
Login via localhost:8000/accounts/login and enter the above credentials.


### Run the tests
`pipenv run python manage.py test`



