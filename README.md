# PDF Data Extractor

This project is designed to extract structured data from PDF files using **FastAPI** and **pdfplumber**. It processes PDF files, extracts relevant information with regular expressions, and returns the extracted data as flat JSON, ensuring simplicity and ease of use.

## **Features**
- Extracts structured data from PDF files.
- Utilizes regular expressions to identify key details.
- Returns extracted data in a flat JSON format (no nested structures).
- Provides an API endpoint using **FastAPI** for seamless interaction with the extraction process.

## **Requirements**
- Python 3.8 or higher
- **FastAPI**
- **pdfplumber**
- **re** (built-in Python module)
- **collections.deque** (built-in Python module)
- **Uvicorn** (to run the FastAPI server)

---

## **Main Functions**

### **`safe_search(pattern, line, group=1, default="Unknown")`**
A utility function that performs a safe search using regular expressions. It attempts to match the provided pattern within the given line. If a match is found, it returns the specified group; otherwise, it returns a default value.

#### **Parameters**:
- **`pattern`**: The regular expression pattern to search for.
- **`line`**: The line of text in which to perform the search.
- **`group`**: (Optional) The group number to return from the match (default is `1`).
- **`default`**: (Optional) The default value to return if no match is found (default is `"Unknown"`).

#### **Returns**:
- The matched group value or the default value (`"Unknown"`).

---

### **`extract_outgoing_data(pdf_path)`**
This function processes the entire content of a PDF file and applies regular expressions to extract relevant fields. The result is returned as a flat dictionary for easy handling.

#### **Parameters**:
- **`pdf_path`**: The path to the PDF file to be processed.

#### **Returns**:
- A dictionary containing the extracted data. Fields may include:
  - Environment
  - ABA
  - Amount
  - Originator Name
  - And more...
