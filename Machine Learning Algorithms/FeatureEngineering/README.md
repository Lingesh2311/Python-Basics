<h3> Feature Engineering Basics </h3>

## Categorical Features

<p>
    <ol>
        <li> Convert the dataframe to dictionary</li>
        <li> Use the <code>DictVectorizer</code> from <code>sklearn.feature_extraction</code></li>
        <li>Use <code>.get_feature_names()</code> to have a look into the code</li>
    </ol>
</p>
<p>
    Some other tools in the scikit-learn package are the <code>sklearn.preprocessing.OneHotEncoder</code> and <code>sklearn.feature_extraction.FeatureHasher</code>.
</p>
<br>

## Text Features

<p>
    <ol>
    <li>Use the <code>sklearn.feature_extraction.text.CountVectorizer</code></li>
    <li>Apply <code>.fit_transform()</code> to generate a sparse matrix representation</li>
    </ol>
    <br>
    The disadvantage with the generation of raw word counts is overcome using the Term frequency inverse document frequency technique.
    <ul>
        <li>Use the <code>sklearn.feature_extraction.text.TfidfVectorizer</code></li>
    </ul>
</p>
<br>

## Image Features

<p>
    Check <a href="https://jakevdp.github.io/PythonDataScienceHandbook/05.04-feature-engineering.html#Image-Features">here</a> for more details.
</p>
<br>

## Derived Features

<p>
    We can create new features from the existing features. This is done in the simple case of Linear regression where the features are converted to Polynomial features.
    <ol>
    <li>Use the <code>sklearn.preprocessing.PolynomialFeatures</code></li>
    <li>Follow it with <code>fit_transform()</code></li>
    </ol>
</p>
<br>

## Imputation - Filling the the Missing

<p>
    <p>
    <li>Use the <code>sklearn.impute.SimpleImputer</code></li>
    <li>Follow it with <code>.fit_transform()</code>
    </p>
    <p>
    More <a href="https://towardsdatascience.com/practical-strategies-to-handle-missing-values-626f9c43870b">here</a> on handling missing values.
    </p>
</p>
<br>

## Feature Pipelines

<p>
Adding pipelines is an important part for a ML model. This will include all the transformations that are responsible for changing the data from start to ML model ready.
<ol>
    <li> Use the <code>sklearn.pipeline.make_pipeline</code> for creating a pipeline</li>
</ol>
</p>
