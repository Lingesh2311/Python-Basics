## Manifold Learning


PCA is used for dimensionality reduction and to represent the data in a lower dimensional subspace without loss in variance. This is fast, easy and interpretable in case of linearly dependent features in the dataset. When it comes to a non-linear relationship between the features then PCA fails.

To overcome this difficulty, Manifold learning is used to represent data in a lower dimensional subspace by creating manifolds.

In other words, it <b>describes the dataset as low dimensional manifolds embedded in higher dimensional space</b>. 


- Imagine a sheet of paper: this is a two-dimensional object that lives in our familiar three-dimensional world, and can be bent or rolled in that two dimensions. In the parlance of manifold learning, we can think of this sheet as a two-dimensional manifold embedded in three-dimensional space.

- Rotating, re-orienting, or stretching the piece of paper in three-dimensional space doesn't change the flat geometry of the paper: such operations are akin to linear embeddings. If you bend, curl, or crumple the paper, it is still a two-dimensional manifold, but the embedding into the three-dimensional space is no longer linear. Manifold learning algorithms would seek to learn about the fundamental two-dimensional nature of the paper, even as it is contorted to fill the three-dimensional space.

Structure
- [`NB1.ipynb`](./NB1.ipynb): Hello world of Manifold Learning
- [`NB2.ipynb`](./NB2.ipynb): Multidimensional Scaling(MDS)
- [`NB3.ipynb`](./NB3.ipynb): MDS as Manifold Learnign
- [`NB4.ipynb`](./NB4.ipynb): Non-linear Embeddings: Where MDS fails
- [`NB5.ipynb`](./NB5.ipynb): Non-linear Manifolds: Locally linear Embedding
