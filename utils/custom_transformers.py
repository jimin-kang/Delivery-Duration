import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class DropHighlyCorrelatedFeatures(BaseEstimator, TransformerMixin):
    '''
    Custom data transformer to drop highly correlated features in feature dataframe prior to prediction.
    Among sets of correlated features, this transformer will drop all but one of the features.
    The default threshold for determining high correlation is 0.8.
    '''
    def __init__(self, threshold=0.8):
        self.threshold = threshold
        self.features_to_drop = None
        self.columns_ = None  # To store column names after transformation
    
    def fit(self, X, y=None):
        # Check if input is a DataFrame or ndarray
        if isinstance(X, pd.DataFrame):
            self.columns_ = X.columns  # Store column names for DataFrame
            corr_matrix = X.corr().abs()  # Use pandas .corr() method for DataFrame
        else:
            self.columns_ = np.arange(X.shape[1])  # For ndarray, create index-based columns
            corr_matrix = np.corrcoef(X, rowvar=False)  # Use np.corrcoef for ndarray

        # Track columns to drop
        self.features_to_drop = set()
        
        # Iterate through the upper triangle of the correlation matrix
        for i in range(len(corr_matrix)):
            for j in range(i + 1, len(corr_matrix)):
                if corr_matrix[i, j] > self.threshold:
                    # Add the later column (j) to the drop list
                    self.features_to_drop.add(self.columns_[j])
        
        return self
    
    def transform(self, X):
        # If input is a DataFrame, drop the identified columns using column names
        if isinstance(X, pd.DataFrame):
            return X.drop(columns=self.features_to_drop)
        # If input is ndarray, drop columns by index
        else:
            return np.delete(X, list(self.features_to_drop), axis=1)
    
    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)
    
    def get_feature_names_out(self, input_features=None):
        # print(f"Input features: {input_features}") # real column names
        # print(f"self.columns_: {self.columns_}") # column indexes
        # print(f"Features to drop: {self.features_to_drop}") # column indexes to drop
        
        # Get the remaining feature names after dropping correlated features
        if input_features is None:
            input_features = self.columns_
        
        # Return the columns that were not dropped
        return [input_features[col_index] for col_index in self.columns_ if col_index not in self.features_to_drop]