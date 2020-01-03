## Regression Analysis

<p>
    This is the process of forming a relationship between a dependent target variable y and independent variables (x). It does so by measuring the strength of impact of the independent variables 
</p>
Some common types of Regression methods are as follows:
<br>
<p>
    <ul>
        <table>
            <tr>
                <td>
                    <li>Linear Regression</li>
                    <li>Polynomial Regression</li>
                    <li>Gaussian Basis Regression</li>
                    <li>Stepwise Regression</li>
                </td>
                <td>
                    <li>Lasso Regression</li>
                    <li>Ridge Regression</li>
                    <li>ElasticNet Regression</li>
                    <li>Stepwise Regression</li>
                </td>
            </tr>
        </table>
    </ul>
</p>
<p>
    ElasticNet Regression
    <br>
    <p>
    ElasticNet is hybrid of Lasso and Ridge Regression techniques. It is trained with L1 and L2 prior as regularizer. Elastic-net is useful when there are multiple features which are correlated. Lasso is likely to pick one of these at random, while elastic-net is likely to pick both. A practical advantage of trading-off between Lasso and Ridge is that, it allows Elastic-Net to inherit some of Ridge’s stability under rotation.
    </p>
</p>
<p>
    Bias Variance Tradeoff - Need for Regularization
    <br>
    <p>
    Bias represents the distance between the mean of the estimates and the actual value. Variance represents the spread of the estimates. For a clean model, both the bias and the variance should be low. This is done using the process known as regularization. The error comprises of the following. By applying regularization, we tend to reduce the variance considerably giving a slight increase in bias.
    <br>
<p>
  Let <img src="https://latex.codecogs.com/svg.latex?f&space;=&space;f(x)&space;\hat{f}&space;=&space;\hat{f}(x)" title="f = f(x) \hat{f} = \hat{f}(x)" /> be the actual and the predicted values of the function.<br>Then, <img src="https://latex.codecogs.com/svg.latex?E[(y-\hat{f})^{2}]&space;=&space;Bias[\hat{f}^{2}]&space;&plus;&space;\sigma^{2}&space;&plus;&space;Var[\hat{f}]" title="E[(y-\hat{f})^{2}] = Bias[\hat{f}^{2}] + \sigma^{2} + Var[\hat{f}]" /> is the value of the error and the contribution of bias, variance and the irreducible factor to it.
</p>
