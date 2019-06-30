'''
Exploring Handwritten digits: Optical Character recognition
Using the MNIST Handwritten digits dataset
'''
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

digits = load_digits()
print(f"Dimension of dataset: {digits.shape}")

# Plotting some digits
fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                         subplot_kw={'xticks':[], 'yticks':[]},
                         gridspec_kw=dict(hspace=0.1, wspace=0.1))

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
    ax.text(0.05, 0.05, str(digits.target[i]),
            transform=ax.transAxes, color='green')
plt.savefig('Number.png')
plt.show()

# Feature Matrix
X = digits.data
print(f"Dimension of Feature: {X.shape}")
# target
y = digits.target
print(f"Dimension of Target: {y.shape}") 

# 1797 samples and 64 features
# Visualizing the 64D parameter space in 2D using unsupervised Dimensionality reduction
# Use the IsoMap - Manifold Learning
iso = Isomap(n_components=2)
iso.fit(digits.data)
data_proj = iso.transform(digits.data)
print(f"Dimension of Projected data: {data_proj.shape}")

# Plotting the Projected data
plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target,
            edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('spectral', 10))
plt.colorbar(label='digit label', ticks=range(10))
plt.clim(-0.5, 9.5)
plt.savefig('ProjectedHandWrittenDigit.png')
plt.show()

# Classification of digits
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)
model = GaussianNB()
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)

# Accuracy Calculation
print(f"Accuracy: {accuracy_score(ytest, y_model)*100}%")

# Plotting confusion Matrix
mat = confusion_matrix(ytest, y_model)

# Plotting Heatmap
sns.heatmap(mat, square=True, annot=True, cbar=False)
plt.title('Heatmap')
plt.xlabel('predicted value')
plt.ylabel('true value')
plt.savefig('Heatmap.png')
plt.show()

# Plotting with Predicted labels
fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                         subplot_kw={'xticks':[], 'yticks':[]},
                         gridspec_kw=dict(hspace=0.1, wspace=0.1))

test_images = Xtest.reshape(-1, 8, 8)

for i, ax in enumerate(axes.flat):
    ax.imshow(test_images[i], cmap='binary', interpolation='nearest')
    ax.text(0.05, 0.05, str(y_model[i]),
            transform=ax.transAxes,
            color='green' if (ytest[i] == y_model[i]) else 'red')
plt.savefig('FinalDigits.png')
plt.show()
