from importlib.resources import path
import pidfile
import time
ServiceName = 'App1'


print('Starting process')
try:
    with pidfile.PIDFile(filename=ServiceName+'.pid'):
        print('Process started')
        time.sleep(60)
except pidfile.AlreadyRunningError:
    print('Already running.')

print('Exiting')