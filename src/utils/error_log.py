from time import localtime, strftime

def errors_log(error_file, e):
    curr_time = strftime("%Y:%m:%d %H:%M:%S", localtime())
    with open(error_file, 'a') as f:
        f.write(f'[{curr_time}] --- {e} \n')