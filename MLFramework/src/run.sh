clear
export TRAINING_DATA=C://Users//lkanniap//Desktop//GITHUB//Python-Basics//MLFramework//input//train_folds.csv
echo "Set Training data path - Done"
export FOLD=0
echo "Set Folds value - Done"

echo "Using 100 Estimators"
python train.py -ne 100
clear
echo "Using 200 Estimators"
python train.py -ne 200
clear
echo "Using 300 Estimators"
python train.py -ne 300
echo "Done"
