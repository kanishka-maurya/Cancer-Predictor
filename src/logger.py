# Creating a logger to track events going on in the program.

import logging
import os
from datetime import datetime

# Creating path to store log files.
LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
LOG_PATH = os.path.join(os.getcwd(),"LOGS")
os.makedirs(LOG_PATH,exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_PATH,LOG_FILE)

# Logging Configuration.
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = '{asctime} {name} {levelname} {message}',
    style = "{",
    level = logging.INFO,
    filemode = "w"
)