# Creating Custom Exceptions for handling errors.

import os
import sys

def get_error_details(error_message,error_details:sys):
    error_type,error_value,error_tb = error_details.exc_info()
    file_name = error_tb.tb_frame.f_code.co_filename
    error = f"Error: {error_type} \n Filename: {file_name} \n Line No.: {error_tb.tb_lineno} \n Error Message: {error_message}"
    return error

class CustomException(Exception):
    def __init__(self,error_message,error_details):
        super().__init__(error_message)
        self.error_details = get_error_details(error_message,error_details)

    def __str__(self):
        return self.error_details

   