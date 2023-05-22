import logging
import datetime

# swagger and logger

current_date = datetime.datetime("%d-%m-%Y")
def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(message)s')
    fileHandler = logging.FileHandler('log/'+log_file + '_'+ current_date)
    
    l.setLevel(level)
    l.addHandler(fileHandler)

def get_or_create(modulename):
    setup_logger('log', modulename)
    logobj = logging.getLogger('log')
    return logobj