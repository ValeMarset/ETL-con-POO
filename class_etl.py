import pandas as pd
from datetime import datetime

class ETL_Handler:
   
    def __init__(self, file_path, encoding):
        self.file_path = file_path
        self.encoding = encoding

    def extract_info(self):
        df = pd.read_csv(self.file_path, encoding=self.encoding, nrows=20)
        return df

    def transform(self, df):
        extraction_datetime = datetime.now()
        df['date_extraction'] = extraction_datetime
        return df

    def load(self, df, file_name):
        df.to_csv(file_name, index=False)
        return print(f'Archivo CSV {file_name} creado con éxito')

    def result_csv(self):
        df = self.extract_info()
        df = self.transform(df)
        file = self.load(df, 'nom_extracted.csv')
        return


    
        
        
 
        
        


