pipenv install matplotlib
pipenv install sklearn
pipenv install jupyter
echo "Done installing required packages"
sleep 5
echo "Updating requirements file"
pip freeze >> requirements.txt
echo "Done!"
