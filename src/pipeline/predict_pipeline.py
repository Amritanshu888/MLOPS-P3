## Now i will try to create a simple web application which will be interacting with these pickle files
## In our web application we will be having a form where i will be giving my input data which will be responsible for predicting the student performance.
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        ## This predict is just like my model prediction : What it is basically doing is prediction
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            ## Once we load this we need to scale the data
            data_scaled = preprocessor.transform(features) ## First Transformation will happen
            preds = model.predict(data_scaled)  ## Then prediction will happen
            return preds
        except Exception as e:
            raise CustomException(e,sys)

class CustomData: ## This CustomData class will be responsible in mapping all the inputs that we are giving in the HTML to the backend with these particular values
    def __init__( self,
                 gender: str,
                 race_ethnicity: int,
                 parental_level_of_education,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
        
        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

        ## These values are basically coming from my web application 
    
    ## This is a variables mapping function to probably get it in form of Dataframe
    def get_data_as_data_frame(self): ## This function will return all my input data in the form of dataframe, bcoz we train our model in the form of dataframe
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            } ## Whatever inputs i m giving in my web application will get mapped in this particular value
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)