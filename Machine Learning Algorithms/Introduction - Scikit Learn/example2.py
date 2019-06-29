'''
Supervised Learning using Scikit-Learn and Iris dataset for Classification
Gaussian Naive Bayes is a good model to use as a baseline classification, 
before exploring whether improvements can be found though.
'''
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.naive_bayes import GaussianNB # Choose model class 
from sklearn.metrics import accuracy_score


def load_data():
    iris = sns.load_dataset('iris')
    X = iris.drop('species', axis=1)
    y = iris['species']
    return X, y

def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
    return X_train, X_test, y_train, y_test 

X, y = load_data()
X_train, X_test, y_train, y_test = split_data(X, y)

model = GaussianNB()
model.fit(X_train, y_train)
y_model = model.predict(X_test)
score  = accuracy_score(y_test, y_model)
print(f"The final score is : {score*100}%")
