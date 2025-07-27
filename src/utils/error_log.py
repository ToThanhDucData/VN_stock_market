from time import localtime, strftime
import os

def errors_log(e):
    #---------------------------------------------------------------
    ERROR_PATH = os.getenv('ERROR_PATH')
    ERROR = os.path.join(ERROR_PATH, os.getenv('ERROR_FILE'))
    #---------------------------------------------------------------

    curr_time = strftime("%Y:%m:%d %H:%M:%S", localtime())
    with open(ERROR, 'a') as f:
        f.write(f'[{curr_time}] --- {e} \n')