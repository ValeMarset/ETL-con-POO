import pandas as pd

class Extraction():

	def __init__(self, file_path, encoding):
		self.file = file_path
		self.encoding = encoding

	def extract_info(self):
		df = pd.read_csv(self.file, encoding=self.encoding, nrows=20)
		return df