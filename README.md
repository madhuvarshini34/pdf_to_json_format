PDF Data Extractor
This project is designed to extract structured data from PDF files using FastAPI and pdfplumber. It allows you to process PDF files, extract relevant information using regular expressions, and return the extracted data as JSON without any nested structures.

Features
Extracts structured data from a PDF file.
Uses regular expressions to identify key information.
Returns extracted data in a flat JSON format.
Provides an API endpoint using FastAPI to interact with the PDF extraction process.

Requirements
Python 3.8 or higher
FastAPI
pdfplumber
re (built-in Python module)
deque (built-in Python module)
Uvicorn for running the FastAPI server

Main Functions
safe_search(pattern, line, group=1, default="Unknown")
This function performs a safe search using regular expressions. It attempts to match the provided pattern in the given line. If a match is found, it returns the matched group; otherwise, it returns the default value ("Unknown").

Parameters:

pattern: The regular expression pattern to match.
line: The line of text to search.
group: The group number to return from the match (default is 1).
default: The default value to return if no match is found (default is "Unknown").
Returns:

The matched group or the default value.
extract_outgoing_data(pdf_path)
This function is responsible for extracting all relevant data from the PDF file located at pdf_path. It processes the entire PDF content, applies the regular expressions to extract the desired fields, and returns a flat dictionary of extracted data.

Parameters:

pdf_path: The path to the PDF file from which data is to be extracted.
Returns:

A dictionary containing the extracted data, including fields like Environment, ABA, Amount, Originator Name, and more.
