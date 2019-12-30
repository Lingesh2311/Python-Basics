## Naive Bayes Classification

<p>
    This Classification algorithm is very much suitable for high dimensional datasets. They are <em>quick-and-dirty</em> baseline model for classification.
</p>
<p>
    There are 2 types of NB Classification algorithms which are considered here as follows:
    <li>Gaussian Naive Bayes</li>
    <li>Multinomial Naive Bayes</li>
</p>
<p>
    The assumption for Gaussian Naive Bayes is that the datapoints are assumed to be drawn from a Gaussian distribution. The Naive Bayes model is a generative model which creates a rough approximation for the labels. This is used to create a probability cloud (ellipses) that denotes the mean and standard deviation of the datapoints. The boundary in Gaussian Naive Bayes classification is in general a Quadratic
</p>
<p>
    In the case of the Multinomial Naive Bayes, we model the nature of the data using the best-fit multinomial distribution. This is best suited for observing counts among a number of categories. MNB is used for features that represent the count rates.
</p>
<br>

### When to use Naive Bayes?

<p>
    They are <em>quick-and-dirty</em> and makes stringent assumptions on the data. They do have some advantages such as follows:
    <ul>
        <li>Fast for training and prediction</li>
        <li>Straightforward probabilistic prediction</li>
        <li>Easily Interpretable</li>
        <li>Few tunable parameters</li>
    </ul>
</p>
<br>

### Notebook Structure

<p>
    <code>NB1.ipynb</code>: Gaussian Naive Bayes on Synthetic data
    <br>
    <code>NB2.ipynb</code>: Multinomial Naive Bayes on Text data
</p>
