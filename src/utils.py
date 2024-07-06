# Some common utility functions.
import os
import pymysql
import sys
import pandas as pd
from dotenv import load_dotenv
from src.exception import CustomException
from src.logger import logging

# Reading data from MySQL Database.
def get_sql_data():
        
        try:
            logging.info("Initiating reading MySQL data.")
            load_dotenv 
            my_db = pymysql.connect(
                host = os.getenv("host"),
                user = os.getenv("user"),
                password = os.getenv("password"),
                db  = os.getenv("db")
            )

            logging.info("Connection Established.",my_db)
            
            df = pd.read_sql_query("SELECT * FROM data",my_db)
            return df
            
            
       
        except Exception as e:
              raise CustomException(e,sys)


