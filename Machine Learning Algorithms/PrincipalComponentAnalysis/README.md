## Principal Component Analysis

This is an unsupervised technique that derives the components which signify maximum variance in the dataset. It is used to highlight interesting aspects about the dataset with no labels being used for the purpose.

It is used for **Dimensionality reduction**, **noise filtering**, **feature selection**.

It provides an easy route to gain insight about high dimensional data by giving information about the **explained variance**.

This is done using the determination of the first few **principal components** in the dataset.

### Disadvantages:
- The nature of PCA is to explain the important features that are responsible for most of the variance in the space.
- It can be trouble when there is noise in the dataset.
- This can be overcome using <code>sklearn.decomposition.RandomizedPCA</code> and <code>sklearn.decomposition.SparsePCA</code>.
