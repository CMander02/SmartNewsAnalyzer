"""Used for assisting file search server-side"""
import cProfile
import pstats
import logging
import os
import src.Internal_API.db_connector as db_connector

# Setup logging for feed ingester module
logger = logging.getLogger('feed_ingester_logger')
logger.setLevel(logging.DEBUG)

# Logging handler and setting logging level to DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# format for log entries
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# adding format to handler
ch.setFormatter(formatter)

# adding handling to logger
logger.addHandler(ch)

# file_found input is temporary, only for testing.
# Implement directory search based on users (if there is a login), e.g a folder for each user


def filename_server_search(filename, file_found):
    """Searches the server for a file given a file name, will return list of matched files"""
    # Error Checks:
    if len(filename) > 25:  # Checks if filename is too long
        logging.error("ERROR 105: File name too long")
        return 105
    if not file_found:  # Checks if file can be found
        logging.error("ERROR 106: No Files Found")
        return 106
    db_connector.query_db("SELECT * FROM Documents WHERE DocName = 'test.pdf'")
    print("File Found")
    return 0


def file_search_profiler():
    """Runs a profile on feed ingester Module and prints results to the console"""
    profiler = cProfile.Profile()
    profiler.enable()
    filename_server_search("test.pdf", True)
    print('File Upload Successful')
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()
    return 0
