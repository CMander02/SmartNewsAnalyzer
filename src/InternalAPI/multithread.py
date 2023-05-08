"""Helper Library to run functions in multiple threads"""
import cProfile
import pstats
import threading
import queue
import os
import logging

# Setup logging for multithread helper
logger = logging.getLogger('multithread_logger')
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


q = queue.Queue()


def worker():
    """Runs all functions and processes in the queue"""
    while True:
        try:
            item = q.get(timeout= 5)
            print(f'Working on {item}')
            if isinstance(item, type(lambda:0)):  # Checks if item is a lambda variable
                item()
            print(f'Finished {item}')
            q.task_done()
        except queue.Empty:
            logging.info("INFO: Queue is currently empty")
            return 0


def add_to_queue(func):
    """Sends requests to worker queue"""
    try:
        q.put(func)
        return 0
    except queue.Full:
        logging.error("ERROR: Queue is currently full")
        return 1


def test_queue(num_jobs):
    """Send test task requests to the worker."""
    try:
        for item in range(num_jobs):
            q.put(item)
        return 0
    except queue.Full:
        logging.error("ERROR: Queue is currently full")
        return 1


def start_threading():
    """Initialize threading of items in processing queue"""
    # Turn-on the worker thread.
    threading.Thread(target=worker, daemon=True).start()

    # Block until all tasks are done.
    q.join()
    logging.info('All threading work completed')
    return 0


def multithreading_profiler():
    """Runs a profile on File Upload Module and prints results to the console"""
    profiler = cProfile.Profile()
    profiler.enable()
    test_queue(60)
    start_threading()
    print('Threading profile successful')
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()
    return 0
