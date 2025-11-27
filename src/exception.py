## Here we will write our own custom exception
import sys ## Any exception that is basically getting controlled this sys library will automatically have that information
from src.logger import logging

def error_message_detail(error,error_detail:sys): ## This error detail will be present inside my sys
    ## The return type of sys it provides u : exc_tb ---> Info regarding on which file the exception has occured, on which line no. the exception has occured all these info will be probably given and stored in this variable right now.
    _,_,exc_tb = error_detail.exc_info() ## --> This is execution info it will probably give u 3 important informations : First 2 info not interested but last will give me exc_tb
    file_name = exc_tb.tb_frame.f_code.co_filename  ## These are properites inside exc_tb , by this we will be able to get the filename over here.
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error) ## Same "error" which we have provided above in the function
    )
    return error_message
    ## Whenever my error raises i will particularly call this function

class CustomException(Exception):  ## Whenever i raise the custom exception its inheriting the parent exception
    def __init__(self,error_message,error_detail:sys):  ## Error detail is basically being tracked by sys
        super().__init__(error_message) ## Since we have to inherit the init function
        self.error_message = error_message_detail(error_message,error_detail=error_detail) 

    def __str__(self):
        return self.error_message ## Whenever i try to print it i will be getting all the error message over here 
                  