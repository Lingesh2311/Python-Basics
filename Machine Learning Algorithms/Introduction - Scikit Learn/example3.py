'''
Dimensionality Reduction:
Reducing the Dimensionality of the Iris dataset to visualize it.
1. Use PCA to get the 2D representation of the 4D data
2. Use seaborn for visualization
'''
import seaborn as sns
from sklearn.decomposition import PCA # 1. Choose the model class
from example2 import load_data
import matplotlib.pyplot as plt


X, y = load_data()
model = PCA(n_components=2) # 2. Instantiate the model
model.fit(X) # 3. Fit the data

# Get the 2D representation
X_2D = model.transform(X) # 4. Transform the data to 2 dimensions

# Plotting the results
iris = sns.load_dataset('iris')
iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]
sns.lmplot("PCA1", "PCA2", hue='species', data=iris, fit_reg=False)
plt.title('PCA Dimensionality Reduction')
plt.savefig('PCA.png')
plt.show()
