import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
#Linux: Change the \ to / (config/logging.conf)
CONFIG_PATH = os.path.join(ROOT_DIR, 'config\logging.conf')

#CONFIG_PATH_SEARCH_FILE = os.path.join(ROOT_DIR, 'log\search_files.log')
#print(CONFIG_PATH_SEARCH_FILE)
