import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass 
from src.utils import get_sql_data
from sklearn.model_selection import train_test_split

@dataclass 
class DataIngestionConfig():
    raw_data_path:str = os.path.join("artifacts","raw.csv")
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")

class DataIngestion():
    '''def __init__(self):
        self.get_data_paths = DataIngestionConfig()
'''
    def initiate_data_ingestion(self):
        try:
            
            logging.info("Initiating Data Ingestion.")
           
            df = get_sql_data()
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            df.to_csv(DataIngestionConfig.raw_data_path,header = True,index = False)
            train_set.to_csv(DataIngestionConfig.train_data_path,header = True,index = False)
            test_set.to_csv(DataIngestionConfig.test_data_path,header = True,index = False)
            
            logging.info("Data Ingestion has been done.")
            
            return(
                DataIngestionConfig.raw_data_path,
                DataIngestionConfig.train_data_path,
                DataIngestionConfig.raw_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)


