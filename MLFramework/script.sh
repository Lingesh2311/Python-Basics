pipenv install -r requirements.txt
pipenv install flake8 --dev
pipenv install autopep8 --dev
pipenv update
pipenv shell
pipenv run pip freeze > requirements.txt
