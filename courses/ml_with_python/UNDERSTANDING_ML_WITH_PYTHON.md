## Machine Learning Technique Comparison
___
* `Supervised`: 
  * Value prediction
  * Needs training data containing value being predicted
  * Trained model predicts value in new data
* `Unsupervised`: 
  * Identify clusters of like data
  * Data does not contain cluster membership
  * Model provides access to data by cluster

### Python Libraries for Machine Learning using this course:
___
* `numpy` - scientific computing
* `pandas` - data frames
* `matplotlib` - 2D plotting
* `scikit-learn`
  * Algorithms
  * Pre-processing
  * Performance evaluation
  * And more...

### Machine Learning Workflow
___
* Asking the right question
* Preparing data
* Selecting the algorithm
* Training the model
* Testing the model

## Preparing Your Data
___
1. Closer the data is to what your predicting, the better -  Data Rule #1 
2. Data will never be in the format you need  - Data Rule #2  
3. Accurately predicting rate events is difficult  - Data Rule #3  
4. Track how you manipulate data - Data Rule #4

#### Columns to Eliminate from the data table
* Not used
* No values
* Duplicates
* Correlated Columns
  * `Same information in a different format`
    * ID and value associated with ID
  * Add little information
  * Can cause algorithms to get confused

## Selecting Your Algorithm
___
#### Algorithm Selection:
* Compare factors
* Difference of opinions about which factors are important
* You will develop your own factors.

#### Algorithm Decision Factors (Part of them...):
____
* Learning Type
* Result Type
* Complexity
* Basic vs enhanced

#### Result Type
* `Regression`
  * Continuous values
  * price = A * # bedroom + B * size + ...
* `Classification`
  * Discrete values
  * small, medium, large
  * 1-100, 101-200, 201-300
  * true or false

#### Complexity
* Keep it Simple
* Eliminate "ensemble" algorithms
  * Container algorithm
  * Multiple child algorithm
  * Boost performance
  * Can be difficult to debug

#### Enhanced vs. Basic
* `Enhanced`
  * Variation of Basic
  * Performance improvements
  * Additional functionality
  * More complex
* `Basic`
  * Simpler
  * Easier to understand

#### Candidate Algorithms
* `Naive Bayes` 
  * Based on likelihood and probability
  * Every feature has the same weight
  * Requires smaller amount of data
* `Logistic Regression`
  * Confusing name, binary result
  * Relationship between features are weighted
* `Decision Tree`
  * Binary Tree
  * Node contains decision
  * Requires enough data to determine nodes and splits

#### Our Selected Algorithm for Diabetic Prediction: Naive Bayes
____
* Simple - easy to understand
* Fast - up to 100X faster
* Stable to data changes


## Training the Model
___
* `ML Training`: Letting **specific** data teach a ML algorithm to create **specific** prediction model.

### Training Overview
___
1. `Split Data`:
  * Prepared Data:
    * Training (70% of the data)
      * Test (30% of the data)
2. `Train Model`
3. `Evaluate Model`

#### Selecting Training Features
* We want minimum features (columns)
* Selected features
  * '#' of Pregnancies
  * Glucose Concentration
  * Blood Pressure
  * Skin Thickness
  * Insulin Level
  * Body Mass Index (BMI)
  * Diabetes Predisposition
  * Age


#### Scikit-learn library
* Designed to work with `NumPy`, `SciPy` and `Pandas`
* Toolset for training and evaluation tasks
  * Data splitting
  * Pre-processing
  * Feature selection
  * Model tuning
* Common interface across algorithms

#### Missing Data
___
* Common Problem
* Options
  * Ignore
  * Drop observations (rows)
  * Replace values (Impute)
* Data numbers

* `Imputing Options`
  * Replace with mean, median
  * Replace with Expert knowledge derived value
  * Using mean imputing

## Testing Your Model's Accuracy
___

### Performance Improvement Options, Take 1
* Adjust current algorithm
* Get more data or improve data
* Improve training
* Switch algorithms

#### Random Forest
* Ensemble Algorithm
* Fits multiple trees with subsets of data
* Averages tree results to improve performance and control over-fitting

#### Fixing Over-fitting
* Regularization hyperparameter
* Cross validation
* Bias - variance trade-off
* Sacrifice some perfection for better overall performance.

#### Unbalanced Classes
* More of one class than the others
* Our Data - 65% No Diabetes, 35% Diabetes
* Can be causing biases estimation yielding poor predication results. 

### Cross Validation
* `Tuning Hyperparameters with Cross Validation`
```md
For each fold

Determine the best hyperparameter value

Next

Set model hyperparameter value to average best

```

#### Algorithm CV Variants
* Algorithm + Cross Validation  = AlgorithmCV
* Ends in "CV"
* Exposes fit(), predict(),...
* Runs the algorithm K times
* Can be used like normal algorithm
