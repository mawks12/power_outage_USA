"""
Library of custom functions and classes for the analysis
(may or may not end up being used).
"""
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class ThresholdFilter(BaseEstimator, TransformerMixin):
    def __init__(self, column, threshold):
        self.column = column
        self.threshold = threshold

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X[X[self.column] > self.threshold]

class PercentileFilter(BaseEstimator, TransformerMixin):
    """
    Transformer to filter out values that are not
    the intended training interval.
    """

    def __init__(self, column, threshold: tuple):
        """
        Initialize the ThresholdFilter.

        Parameters:
            threshold: The threshold to filter out. Should
            be a tuple of the form (min, max), incluseive,
            where min and max are both percentile values.
        """
        self.threshold = threshold
        self.column = column

    def fit(self, X, y=None):
        """
        Fits the model to the training data.

        Parameters:
        X (array-like): The input features.
        y (array-like, optional): The target values.

        Returns:
        self: The fitted model.
        """
        return self

    def transform(self, X, y=None):
        """
        Apply a transformation to the input data.

        Parameters:
        - X: pandas DataFrame
            The input data to be transformed.
        - y: None, optional
            The target variable (not used in this method).

        Returns:
        - transformed_X: pandas DataFrame
            The transformed data.

        """
        X[f'{self.column}_cut'] = pd.qcut(X[self.column], np.linspace(
            0, 1, 101), labels=np.linspace(0.01, 1, 100)).astype(float)
        return X[X[f'{self.column}_cut'] >= self.threshold[0]
                 & X[f'{self.column}_cut'] <= self.threshold[1]].drop(columns=[f'{self.column}_cut'])
