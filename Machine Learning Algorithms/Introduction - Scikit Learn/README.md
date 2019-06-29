Introduction to **Scikit-Learn**

It is a tool for Data Mining and Data Analysis. Built on **Numpy, Scipy and matplotlib**.
Its online documentation is a good read [here](https://scikit-learn.org/stable/documentation.html). 

The usage of Scikit-Learn can be seen as a combination of 2 API's namely
- Data Representation API
Here the data can be thought of as a table/ dataframe to be exact. Each row can be thought of as an observation with the number of rows being denoted as `n_samples`. Samples can be a flower, person, object, image, document or something which can be described quantitatively.

Likewise, the column in the dataframe can be thought of as a piece of information that describes each sample. In general, we will refer to the columns as the features. The number of features is denoted as `n_features`. The features are generally real-valued, but can be boolean and discrete too!

    - Feature Matrix
        The feature matrix is assumed to be 2-dimensional, with shape `[n_samples, n_features]` and is stored as a dataframe.
        The **Target array** is the quantity that we want to predict. It is the dependant variable. 
        
- Estimator API
The guiding principles behind the design of the Scikit-Learn API can be found in this [paper](https://arxiv.org/abs/1309.0238).
The main factors are as follows:
- Consistency
- Inspection
- Limited Object Hierarchy
- Composition
- Sensible defaults

        - Steps Used in Estimator API
         
             1. Choose a class of model by importing the appropriate estimator class
             2. Choose model hyperparameters by instantiating the calss with desired values
             3. Arrange the data into feature and target matrix/vector.
             4. Fit the model to the data by calling the `.fit()` method. 
             5. Apply the model to the new data. 
                 - Supervised Learning: Predict the labels using `.predict()` method
                 - Unsupervised Learning: We can transform or infer properties of the data using `.transform()` or `.predict()` method.