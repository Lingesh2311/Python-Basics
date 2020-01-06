clear
export TRAINING_DATA=C://Users//lkanniap//Desktop//GITHUB//Python-Basics//MLFramework//input//train_folds.csv
echo "Set Training data path - Done"
export FOLD=0
echo "Set Folds value - Done"

python train.py -ne 100
