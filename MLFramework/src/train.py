import pandas as pd
import logging
import os
import argparse
from sklearn import ensemble
from sklearn import preprocessing
from sklearn import metrics

TRAINING_DATA = os.environ.get("TRAINING_DATA")
FOLD = int(os.environ.get("FOLD"))
logger = logging.getLogger('mlframework')
parser = argparse.ArgumentParser()
parser.add_argument('-ne', '--n_estimators', help='Choose the number of\
                                               estimators start(100)',
                    dest='n_estimators', type=int)
args = parser.parse_args()

FOLD_MAPPING = {
    0: [1, 2, 3, 4],  # exclude 0
    1: [0, 2, 3, 4],  # exclude 1
    2: [0, 1, 3, 4],  # exclude 2
    3: [0, 1, 2, 4],  # exclude 3
    4: [0, 1, 2, 3]   # exclude 4
}

if __name__ == "__main__":
    df = pd.read_csv(TRAINING_DATA)
    # training data
    train_df = df[df.kfold.isin(FOLD_MAPPING.get(FOLD))]
    # validation data
    valid_df = df[df.kfold == FOLD]

    # training labels
    ytrain = train_df.target.values
    # validation labels
    yvalid = valid_df.target.values

    train_df = train_df.drop(['id', 'target', 'kfold'], axis=1)
    valid_df = valid_df.drop(['id', 'target', 'kfold'], axis=1)

    valid_df = valid_df[train_df.columns]

    label_encoders = []
    for c in train_df.columns:
        lbl = preprocessing.LabelEncoder()
        lbl.fit(train_df[c].values.tolist() + valid_df[c].values.tolist())
        train_df.loc[:, c] = lbl.transform(train_df[c].values.tolist())
        valid_df.loc[:, c] = lbl.transform(valid_df[c].values.tolist())
        label_encoders.append((c, lbl))

    clf = ensemble.RandomForestClassifier(
        n_estimators=args.n_estimators, n_jobs=-1, verbose=2)
    clf.fit(train_df, ytrain)
    num_estimators = args.n_estimators
    ypred = clf.predict_proba(valid_df)[:, 1]
    print(f'FIRST COL PREDICTION; {ypred}')
    score = metrics.roc_auc_score(yvalid, ypred)
    print(f'ROC_AUC_SCORE: {score}')
    hdlr = logging.FileHandler('./score.log')
    formatter = logging.Formatter('%(num_estimators)s %(score)s')
    msg = str(num_estimators)+' '+str(score) 
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    logger.info(msg)
