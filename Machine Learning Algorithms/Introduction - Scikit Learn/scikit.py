import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

iris =  sns.load_dataset('iris')

# Print the dataframe
print(iris.head())

# Display a pairplot
sns.pairplot(iris, hue='species', height=1.5)
plt.show()

# Features
X_iris = iris.drop('species', axis=1)
print(f"Shape of Feature Matrix: {X_iris.shape}")

# Target
y_iris = iris['species']
print(f"Shape of Target Matrix: {y_iris.shape}")
