### Hyperparameters and Model Validation
1. Choose a class model
2. Choose model hyperparameters
3. Fit the model
4. Use the mdoel to predict labels for new data.

**Wrong way of model validation - Training & evaluating on the same dataset**

**Right way - Holdout sets using** `train_test_split`

Try applying cross validation since we should not miss out the portion of data while training and evaluating using the holdout sets. Check out the cross validation document for more details [here](http://scikit-learn.org/stable/modules/cross_validation.html)

### Selecting the Best Model
Consider the bias variance model [here](https://github.com/Lingesh2311/Python-Basics/blob/master/Machine%20Learning%20Algorithms/Hyperparameters%20and%20Model%20Validation/figures/bias-variance.png).

#### Bias-Variance Tradeoff
- For high-bias model: The performance of the model on the validation and the trainng dataset are similar
- For high-variance model: The performance of the model on the validation set is worse than in the training set. 
