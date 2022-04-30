from sklearn.preprocessing import StandardScaler
from sklearn.piepeline import Piepline, FeatureUnion
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin




# Module to separate columns and pass only seletec columns to next pipeline
class ColSeparator():
	
	def __init__(self, req_cols = 'category'):

		self.oper = oper
		self.req_cols = req_cols


	def filter_criteria(self, keep_cols = None):

		return keep_cols


	def __call__(self, X=None):


		cols = [ col for col in X.columns if col in filter_creteria + [self.req_cols] ]

		return X[cols]



# Module to filter out certain type of features and pass rest of the features to the next pipeline module
class SkipFormer(BaseEstimator, TransformerMixin):

	def __init__(self, skip_feats):

		self.skip_feats = skip_feats


	def fit(self, X, y=None):

		return self


	def get_feature_names(self):


		return self.skip_feats


	def transform(self, X, y=None):

		return X[self.skip_feats]



# Module to apply capping and flooring to treat outliers, Either feature wise capping flooring or single value for all features can be defined
class CapFloor(BaseEstimator, TransformerMixin):

	def __init__(self, feature_names=None, q = {'all' : [.99, .01]}):

		self.feature_names = feature_names
		self.q = q


	def get_feature_names(self):

		return self.feature_names


	def fit(self, X, y=None):

		if q.get('all',[]) == []:

			self._qtiles_cap = pd.concat([X[[col]].quantile(n[0]) for col,n in self.q.items()], axis=0)
			self._qtiles_floor = pd.concat([X[[col]].quantile(n[1]) for col,n in self.q.items()], axis=0)

		else:

			self._qtiles_cap = X.quantile(self.q[0])
			self._qtiles_floor = X.quantile(self.q[1])

		return self


	def transform(self, X, y=None):


		self.feature_names = X.columns.tolist()
		X.update(X.clip(self._qtiles_cap,self._qtiles_floor))

		return X

