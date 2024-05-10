import pandas as pd

class Load():

	def __init__(self, df, new_file_name):
		self.df = df
		self.new_file_name = new_file_name

	def load_file(self):
		self.df.to_csv(self.new_file_name, index=False)
		return print(f'Archivo CSV {self.new_file_name} creado con éxito')