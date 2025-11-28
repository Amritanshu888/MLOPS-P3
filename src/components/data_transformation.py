import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer  ## For missing values (we can use different different imputation technique)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        ## Why this function ?? --> Just to create pickel files which will be responsible in converting ur categorical features into numerical (like if u perform OneHotEncoder or Standard Scaler)
        try:
            numerical_columns = ["writing_score","reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            ## Now we will do two important things : 1. Create a pipeline 2. There are some missing values so now we handle those missing values
            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")), ## This will be responsible in handling my missing values, in statergies we are using median bcoz there are some outliers(in numerical features).
                    ("scaler",StandardScaler())
                ]
            )
            ## Here we have created a pipeline which is doing two important things : 1. Handling the Missing Values(with statergy like median) 2. Doing the Standard Scaling and this pipeline needs to run on the training dataset. fit_transform on training dataset and just transform on test dataset
            cat_pipeline = Pipeline(
                ## How do we handle missing values in categorical features, handling categorical converting it to numerical values how to do ??
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")), ## That basically means i m going to replace all the missing values with most frequent one i.e. mode
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )

            logging.info(f"Categorical Columns: {categorical_columns}")
            logging.info(f"Numerical Columns: {numerical_columns}")
            ## Now we have to combine this numerical pipeline and categorical pipeline together
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_path,test_path): ## train and test path u are getting from data ingestion
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read Train and Test Data Completed")

            logging.info("Obtaining Preprocessing Object")

            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = "math_score"
            numerical_column = ["writing_score","reading_score"]

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)] ## Combining them together using np.c_

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            ) ## save_object just used for saving the pickel file

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)          