# Required Libraries
import sys
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# Implementing a perceptron learning algorithm in Python
class Perceptron:
    """
    A Perceptron classifier.

    The perceptron is a simple supervised machine learning algorithm
    and one of the earliest neural network architectures. It's used
    for binary classification tasks.

    Parameters
    ----------
    eta : float, default=0.01
        The learning rate, a value between 0.0 and 1.0.

    n_iter : int, default=50
        The number of passes over the training dataset (epochs).

    random_state : int, default=1
        Seed for random weight initialization.

    Attributes
    ----------
    w_ : 1d-array
        Weights after training.

    b_ : float
        Bias unit after training. Represents the y-intercept.

    errors_ : list
        List of the number of misclassifications (updates) in each epoch.
    """

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """
        Fit the training data.

        Trains the perceptron on the provided data.

        Parameters
        ----------
        X : array-like, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples
            and n_features is the number of features.

        y : array-like, shape = [n_samples]
            Target values, corresponding to the input samples.

        Returns
        -------
        self : object
            The trained perceptron model.
        """

        # Initialize weights and bias
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.b_ = 0.
        self.errors_ = []

        # Iteratively refine the model
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                # Weight update rule
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0.0)
            self.errors_.append(errors)

        return self

    def net_input(self, X):
        """
        Calculate the net input.

        Computes the weighted sum of the inputs.

        Parameters
        ----------
        X : array-like
            Input data.

        Returns
        -------
        float
            The net input value.
        """

        return np.dot(X, self.w_) + self.b_

    def predict(self, X):
        """
        Predict class labels.

        Determines the class label based on the unit step function.

        Parameters
        ----------
        X : array-like
            Input data.

        Returns
        -------
        int
            Predicted class label (either 0 or 1).
        """

        return np.where(self.net_input(X) >= 0.0, 1, -1)
