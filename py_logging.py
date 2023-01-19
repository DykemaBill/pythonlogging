# External libraries
import json, logging, logging.handlers

# Starting up
print("Starting up...")

# Configuration file name
config_name = 'settings'
config_file = config_name + '.cfg'

# Set default configuration variables
logfilesize = [ 10000, 9 ] # 10000 is 10k, 9 is 10 total copies

# Read configuration file function
config_error = False
def config_file_read():
    try:
        with open(config_file, 'r') as config_contents:
            cfg_data = json.loads(config_contents.read())
            global logfilesize
            # Read log file settings
            logfilesize.clear()
            logfilesize.append(cfg_data['logfilesize'][0])
            logfilesize.append(cfg_data['logfilesize'][1])
    except IOError:
        print('Problem opening ' + config_file + ', check to make sure your configuration file is not missing.')
        global config_error
        config_error = True

# Read configuration file
config_file_read()

# Log file name
log_name = 'example'
log_file = log_name + '.log'
# Start logger with desired output level
logger = logging.getLogger('Logger')
logger.setLevel(logging.INFO)
# Setup log handler to manage size and total copies
handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=logfilesize[0], backupCount=logfilesize[1])
# Setup formatter to prefix each entry with date/time 
formatter = logging.Formatter("%(asctime)s - %(message)s")
# Add formatter
handler.setFormatter(formatter)
# Add handler
logger.addHandler(handler)

# Starting log
logger.info('****====****====****====****====****==== Starting up ====****====****====****====****====****')

# Config file status
if config_error == True:
    print ("Unable to set configuration variables!")
    logger.error('Problem opening ' + config_file + ', check to make sure your configuration file is not missing.')
else: # Config settings out to the log
    print ("Configuration file read...")
    logger.info('Log file size is set to ' + str(logfilesize[0]) + ' bytes and ' + str(logfilesize[1]) + ' copies')

# Log file message
print ("Check log file " + log_file + " to see if things worked correctly.")
logger.info('Log file ' + log_file + ' populated correctly.')