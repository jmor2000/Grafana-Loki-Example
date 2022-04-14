from importlib.resources import path
import pidfile
import time
ServiceName = 'app1'
#=======================>>>>>Logging
import logging
logging.basicConfig(filename= ServiceName+'.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

print('Starting process')
logging.info('Starting process')
try:
    with pidfile.PIDFile(filename=ServiceName+'.pid'):
        logging.info('Process Started')
        print('Process started')
        
        for x in range(1000):
            time.sleep(1)
            logging.info('Alive')

except pidfile.AlreadyRunningError:
    print('Already running.')
    logging.warning('Process Second Generation Attempt')

print('Exiting')
logging.info('Exiting')