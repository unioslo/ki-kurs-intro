Episode 2: Machine Learning Fundamentals
==========================================

.. contents::
   :local:
   :depth: 2

Overview
--------

This episode covers the basics of machine learning, a core component of modern AI.

Topics covered
~~~~~~~~~~~~~~

* Supervised vs Unsupervised Learning
* Training and testing data
* Model evaluation metrics
* Common algorithms

Learning objectives
~~~~~~~~~~~~~~~~~~

By the end of this episode, you will be able to:

* Explain the difference between supervised and unsupervised learning
* Understand the importance of data splitting
* Apply basic evaluation metrics
* Recognize common ML algorithms and their use cases

Supervised vs Unsupervised Learning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Machine learning can be broadly categorized into two main approaches:

.. tabs::

   .. tab:: Supervised Learning

      Learning with labeled data where the algorithm learns to map inputs to outputs based on example input-output pairs.

      **Common Tasks:**
      * Classification (categorical output)
      * Regression (continuous output)

      **Examples:**
      * Email spam detection
      * House price prediction
      * Image classification

   .. tab:: Unsupervised Learning

      Learning with unlabeled data where the algorithm tries to find patterns or structure in the data without predefined outputs.

      **Common Tasks:**
      * Clustering
      * Dimensionality reduction
      * Anomaly detection

      **Examples:**
      * Customer segmentation
      * Feature extraction
      * Network intrusion detection

.. code-block:: python

   import numpy as np
   from sklearn.model_selection import train_test_split
   from sklearn.linear_model import LinearRegression
   from sklearn.metrics import mean_squared_error

   # Sample data for supervised learning
   X = np.array([[1], [2], [3], [4], [5]])  # Features
   y = np.array([2, 4, 6, 8, 10])          # Labels

   # Split data into training and testing sets
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   # Create and train a model
   model = LinearRegression()
   model.fit(X_train, y_train)

   # Make predictions
   predictions = model.predict(X_test)
   print(f"Predictions: {predictions}")

   # Evaluate the model
   mse = mean_squared_error(y_test, predictions)
   print(f"Mean Squared Error: {mse}")

Training and Testing Data
~~~~~~~~~~~~~~~~~~~~~~~~~~

Proper data splitting is crucial for model evaluation:

.. tabs::

   .. tab:: Training Set

      The portion of data used to train the model. Typically 70-80% of the total dataset.

   .. tab:: Testing Set

      The portion of data used to evaluate the model's performance on unseen data. Typically 20-30% of the total dataset.

   .. tab:: Validation Set

      Optional set used for hyperparameter tuning and model selection during development.

.. question::

   Why do we need to split data into training and testing sets?

   .. answer::

      To evaluate how well the model generalizes to unseen data. If we test on the same data we trained on, we might get overly optimistic results that don't reflect real-world performance.

Model Evaluation Metrics
~~~~~~~~~~~~~~~~~~~~~~~~~

Different metrics are used depending on the type of machine learning problem:

.. tabs::

   .. tab:: Classification Metrics

      * **Accuracy**: (TP + TN) / (TP + TN + FP + FN)
      * **Precision**: TP / (TP + FP)
      * **Recall**: TP / (TP + FN)
      * **F1-Score**: 2 * (Precision * Recall) / (Precision + Recall)

   .. tab:: Regression Metrics

      * **Mean Absolute Error (MAE)**: Average of absolute errors
      * **Mean Squared Error (MSE)**: Average of squared errors
      * **R-squared**: Proportion of variance explained by the model

.. exercise::

   **Exercise: Calculate Evaluation Metrics**

   Given the following confusion matrix for a binary classification problem:

   .. code-block:: text

              Predicted
               Positive  Negative
      Actual   Positive    45        5
               Negative    10        40

   Calculate:
   1. Accuracy
   2. Precision
   3. Recall
   4. F1-Score

   .. solution::

      1. Accuracy = (45 + 40) / (45 + 5 + 10 + 40) = 85 / 100 = 0.85
      2. Precision = 45 / (45 + 10) = 45 / 55 = 0.818
      3. Recall = 45 / (45 + 5) = 45 / 50 = 0.9
      4. F1-Score = 2 * (0.818 * 0.9) / (0.818 + 0.9) = 2 * 0.736 / 1.718 = 0.857

Common ML Algorithms
~~~~~~~~~~~~~~~~~~~~~

Here are some fundamental machine learning algorithms:

.. tabs::

   .. tab:: Linear Regression

      Simple algorithm for predicting continuous values. Assumes linear relationship between features and target.

      **Use Cases:** Price prediction, trend analysis, forecasting

   .. tab:: Decision Trees

      Tree-like model of decisions. Easy to interpret and visualize.

      **Use Cases:** Classification, regression, feature importance analysis

   .. tab:: Random Forest

      Ensemble method using multiple decision trees. Reduces overfitting.

      **Use Cases:** Classification, regression, feature selection

   .. tab:: Support Vector Machines (SVM)

      Finds optimal hyperplane to separate classes in feature space.

      **Use Cases:** Classification, regression, outlier detection

   .. tab:: K-Means Clustering

      Unsupervised algorithm for grouping similar data points.

      **Use Cases:** Customer segmentation, image compression, anomaly detection

.. code-block:: bash

   # Install common ML libraries
   pip install scikit-learn pandas matplotlib seaborn
   
   # Example of loading and exploring data
   import pandas as pd
   import matplotlib.pyplot as plt
   
   # Load dataset
   data = pd.read_csv('your_dataset.csv')
   
   # Basic exploration
   print(data.head())
   print(data.describe())
   
   # Simple visualization
   plt.scatter(data['feature1'], data['feature2'])
   plt.xlabel('Feature 1')
   plt.ylabel('Feature 2')
   plt.title('Data Distribution')
   plt.show()

.. note::

   Understanding these fundamentals is essential for building effective machine learning models. In the next episode, we'll explore neural networks and deep learning.