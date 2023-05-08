"""Used for assisting file upload from client-side"""
import cProfile
import pstats
import logging
import os
import src.Internal_API.db_connector as db_connector

# Setup logging for file upload module
logger = logging.getLogger('file_upload_logger')
logger.setLevel(logging.DEBUG)

# Logging handler and setting logging level to DEBUG
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# format for log entries
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# adding format to handler
stream_handler.setFormatter(formatter)

# adding handling to logger
logger.addHandler(stream_handler)


def file_upload(path):
    """Handles single file upload from the user after file is selected on frontend via HTML"""
    # Error stream_handlerecks:
    if not isinstance(path, str):  # stream_handlerecks if filename is a string
        logging.error("ERROR 301: Invalid File Name")
        return 301
    if not path.endswith('.pdf'):  # stream_handlerecks if file is correct format
        logging.error("ERROR 302: Invalid File Type")
        return 302
    if os.path.exists(path):
        logging.warning("WARNING: File already exists, existing file will be overwritten")
        return 303
    db_connector.query_db("INSERT INTO Documents (DocumentID,UserID,DocName,DocType) VALUES (114514, 123, 'test.pdf', '.pdf')")
    print("File Uploaded")
    return 0


def file_upload_profiler():
    """Run a profile on File Upload Module and prints results to the console"""
    profiler = cProfile.Profile()
    profiler.enable()
    file_upload("new.pdf")
    print('File Upload Successful')
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()
    return 0
