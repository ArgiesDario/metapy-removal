import os
from datetime import datetime, timedelta



def __get_modified_files(path, minutes_ago, current_time=datetime.now(), minutes_buffer=1):
    """Get all modified files in the last X+buffer minutes in the given path

    Parameters:
    - path [string] : Path to search for files
    - minutes_ago [int] : Minutes ago to search for modified files
    - current_time [datetime] : Current datetime
    - minutes_buffer [int] : Buffer added to minutes_ago

    Returns:
    - modified_files [list] : List of file names modified in last minutes_ago+buffer in path
    """
    modified_files = []
    os.chdir(path)
    ago_time = current_time-timedelta(minutes=minutes_ago+minutes_buffer)
    files = os.listdir()
    for file in files:
        file_date = datetime.fromtimestamp(os.path.getmtime(file))
        if file_date >= ago_time:
            modified_files.append(file)
    return modified_files
