## Logger is for the purpose that any execution that probably happens we should be able to log all those informations the execution and everything in some files so that we should be able to track if there is some errors event the custom exception error, will try to log any exception that comes.
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) ## os.getcwd() --> to get the current working directory
os.makedirs(logs_path,exist_ok=True) ## exist_ok=True --> It says even though there is a file or folder keep on appending the files inside that whenever we want to create the file

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO, ## In case of info only i will print these messages
)