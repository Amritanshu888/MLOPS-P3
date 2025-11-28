import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

## Reason of using Data Ingestion Config : Any input that i require i will give it through this DataIngestionConfig, we will also be creating an artifact folder as it will allow us to see our output
@dataclass  ## If u use dataclass u will be able to directly define ur class variables no need to use init
class DataIngestionConfig:
    ## Defining class variables
    train_data_path:str = os.path.join('artifacts',"train.csv")
    test_data_path:str = os.path.join('artifacts',"test.csv")
    raw_data_path:str = os.path.join('artifacts',"data.csv")
    ## These are the inputs i m giving to my data ingestion component
    ## Now data ingestion component knows where to save the train path, test path and data path.

class DataIngestion:
    ## When u have to only define the variables in a class we use dataclass and when u have to define functions also in the class there u use init method
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() ## These three paths will be saved inside this class variable, will be saved like sub variables
        
    def initiate_data_ingestion(self):
        ## If ur data is stored in some databases i will write the code to read it from the databases(here in this function)
        logging.info("Entered the Data Ingestion Method or Component")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the Dataset as DataFrame")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            ) ## These two informations will be required for my data transformation component, so that it can grab these informations and start the further process.
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))  ## Once i print this it is basically going to give me my r2_score

