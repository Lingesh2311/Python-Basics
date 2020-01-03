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
    Bias represents the distance between the mean of the estimates and the actual value. Variance represents the spread of the estimates. For a clean model, both the bias and the variance should be low. This is done using the process known as regularization. The error comprises of the following.
    <br>
<p>
   <img src="https://latex.codecogs.com/svg.latex?a&space;=&space;b&plus;c_{x}" title="a = b+c_{x}" />
</p>
