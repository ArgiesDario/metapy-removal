import os
from datetime import datetime, timedelta



def get_modified_files(path, minutes_ago, minutes_buffer=1):
    modified_files = []
    os.chdir(path)
    ago_time = datetime.now()-timedelta(minutes=minutes_ago+minutes_buffer)
    files = os.listdir()
    for file in files:
        file_date = datetime.fromtimestamp(os.path.getmtime(file))
        if file_date >= ago_time:
            modified_files.append(file)
    return modified_files
