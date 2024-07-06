import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass 
from src.utils import get_sql_data
from sklearn.model_selection import train_test_split 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from src.components.data_ingestion import DataIngestion,DataIngestionConfig
from src.utils import save_obj

df = get_sql_data()

@dataclass 
class DataTransformationConfig():
    preprocessor_path  = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation():
    
    def get_transformer_object():
        try:
            logging.info("Getting Transformer Object.")
        
            num_features = list(df.drop("diagnosis",axis=1))
            cat_feature = ["diagnosis"]

            num_pipeline = Pipeline(steps=[
                ("Imputer",SimpleImputer(strategy = "median")),
                ("Scaler",StandardScaler())]
                )
            
            cat_pipeline = Pipeline(steps=[
                ("Imputer",SimpleImputer(strategy = "most_frequent")),
                ("Scaler",OneHotEncoder())]
                )
            
            preprocessor = ColumnTransformer(transformers=[
                ("num",num_pipeline,num_features),
                ("cat",cat_pipeline,cat_feature)
            ])
            
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path):
        try:
            logging.info("Initiating Data Transformation.") 
            
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            preprocessing_object = DataTransformation.get_transformer_object()
            
            train_array = preprocessing_object.fit_transform(train_df)
            test_array = preprocessing_object.transform(test_df)

            save_obj(
                file_path = DataTransformationConfig.preprocessor_path,
                obj = preprocessing_object
            )
            
            return  (
                train_array,
                test_array,
                DataTransformationConfig.preprocessor_path)
        except Exception as e:
            raise CustomException(e,sys)
    
