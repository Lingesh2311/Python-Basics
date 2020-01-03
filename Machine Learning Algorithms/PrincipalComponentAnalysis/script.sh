pipenv install matplotlib
pipenv install numpy
pipenv install seaborn
pipenv install sklearn
pipenv update
echo "Done"
pipenv run pip freeze > requirements.txt
echo "Done"
