"""Used to call an external NLP API for a given text input """
# Library imports
import cProfile
import pstats
import logging
import os
import PyPDF2 as pypdf
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import src.Internal_API.db_connector as db_connector

# Setup logging for text analysis module
logger = logging.getLogger('text_analysis_logger')
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


# API_error value for testing only, will be removed when NLP API is implemented
def text_analyze(input):
    """Handles text analysis from a given text and uses external API, returns raw data from NLP analysis"""
    # Error Checks:
    if input is None or input.strip() == '':# Checks if input is empty
        logging.error("ERROR 101: Input not found")
        return 101
    if not isinstance(input, str):  # Checks if input text is a string
        logging.error("ERROR 102: Input is not a string")
        return 102
    if len(input) < 3:# Checks if length of input is within bounds, is lower for testing
        logging.error("ERROR 103: Input is too short")
        return 103
    if len(input) > 15:  # Checks if length of input is within bounds, is higher for testing
        logging.error("ERROR 104: Input is too long")
        return 104
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(input)
    sentiment_score = scores["compound"]
    db_connector.query_db("INSERT INTO Paragraphs (paragraphID,documentID,sentimentNum) VALUES (1, 1234, 0.7)")
    print("Text Analyzed")
    return sentiment_score


# extracted_text and pdf_page are for testing only, will be removed when pypdf is implemented
def pdf_to_text(file_name, extracted_text, pdf_page):
    """Handles the conversion from PDF to a text string, returns string of text or list of strings"""
    if not os.path.isfile(file_name):
        logger.error("ERROR 201: File not found")
        return 201
    if not file_name.endswith('.pdf'):
        logger.error("ERROR 202: Invalid file format")
        return 202
    try:
        pdf_object = open(file_name, 'rb')
        pdf_reader = pypdf.PdfReader(pdf_object)
    except pypdf.utils.PdfReadError:
        logger.error("ERROR 203: Error reading PDF file")
        return 203
    if len(pdf_reader.pages) == 0:
        logger.error("ERROR 204: Selected PDF has no pages")
        return 204
    db_connector.query_db(f"INSERT INTO Paragraphs (paratext) VALUES ('{extracted_text}') WHERE paragraphID = 1")
    print("Text Extracted!")
    return 0

def text_analysis_profiler():
    """Runs a profile on text analysis Module and prints results to the console"""
    profiler = cProfile.Profile()
    profiler.enable()
    text_analyze("Hello World!", False)
    print('Text Analysis Successful')
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()
    return 0
