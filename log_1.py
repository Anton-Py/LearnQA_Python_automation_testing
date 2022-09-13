import logging

# logging.basicConfig(level=logging.DEBUG, filename="example.log")
logging.basicConfig(level=logging.DEBUG, filename="example.log", format='%(asctime)s %(levelname)s %(filename)s %(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
