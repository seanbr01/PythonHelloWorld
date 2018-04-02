import os
import time
import math
import logging
import logging.handlers

# Sets up logging

# Gets current time
current_time = time.time()

# Change directories and get files.
path = "/tmp/wattime"
os.chdir(path)
dirs = os.listdir(path)

# removes files older than 30 minutes.
for file in dirs:
    creation_time = os.path.getctime(file)
    if (current_time - creation_time) / 60 > 30:
        logging.info("Deleted file: $file")
        os.remove(file)
    print file
