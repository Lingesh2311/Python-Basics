'''
Unsupervised Learning: Iris Clustering
A clustering algorithm attempts to find distinct groups of data without
reference to any labels. Here we will use Gaussian Mixture Models(GMM).
A GMM attempts to model the data as a collection of Gaussian blobs
'''
from example2 import load_data
from example3 import iris
from sklearn.mixture import GaussianMixture # 1. Choose model class
import seaborn as sns
import matplotlib.pyplot as plt

X_iris, _ = load_data()
model = GaussianMixture(n_components=3, 
            covariance_type='full')
model.fit(X_iris)
y_gmm = model.predict(X_iris)

# Plotting
iris['cluster'] = y_gmm
sns.lmplot("PCA1", "PCA2", data=iris, hue='species',
            col='cluster', fit_reg=False)
plt.savefig('Cluster.png')
plt.show()
