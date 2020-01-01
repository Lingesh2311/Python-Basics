pipenv install matplotlib
pipenv install seaborn
pipenv install sklearn
pipenv install jupyter
echo "Done installing required packages"
echo "Updating requirements file"
pipenv run pip freeze > requirements.txt
echo "Done!"
