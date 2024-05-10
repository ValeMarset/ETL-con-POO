import pandas as pd
from datetime import datetime

class Transform():

	def __init__(self, df):
		self.df = df

	def transform_df(self):
		extraction_datetime = datetime.now()
		self.df['date_extraction'] = extraction_datetime
		return self.df