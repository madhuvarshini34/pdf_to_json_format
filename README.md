# PDF Data Extractor Tool

This project is a lightweight and efficient tool designed to extract structured data from PDF documents. It leverages **FastAPI**, **pdfplumber**, and **HTML templates** for seamless data extraction and user interaction. The tool processes the PDF content using regular expressions and outputs the extracted data in a flat JSON format or displays it on a web page.

---

## Features

- Extracts and processes text from PDF documents.
- Utilizes regular expressions to extract structured data fields.
- Provides both REST API and HTML-based user interfaces via FastAPI.
- Displays the extracted data on a web page using HTML templates.

---

## Project Structure

### **Packages and Modules**

#### 1. `pdf_processor`
- **`Pdf_outgoing_extractor.py`**
  - `extract_outgoing_data(pdf_path)`: Extracts structured data from PDF content using regex and returns a dictionary.
  - `safe_search(pattern, line, group=1, default="Unknown")`: Safely applies regex to a given line of text and returns the result.

#### 2. `API`
- **`main.py`**
  - Sets up the FastAPI server and exposes:
    - `/extract`: API endpoint for PDF data extraction.
    - `/upload`: HTML-based form for uploading a PDF and viewing results.

#### 3. `templates`
- Contains HTML templates for rendering the web interface:
  - **`upload.html`**: A form for uploading PDF files. Displays the extracted data in a user-friendly table format.

---

## Libraries Utilized

- **FastAPI**: For building the REST API and web application.
- **Jinja2**: For rendering HTML templates.
- **pdfplumber**: For extracting text from PDF documents.
- **re**: For pattern matching and data extraction using regular expressions.
- **Uvicorn**: For running the FastAPI server.

---

## Manual Inputs and Configuration

### 1. Regular Expressions for Extraction
Define regex patterns for extracting specific fields from the PDF content in the `pdf_processor` module.

### 2. HTML Templates
Ensure the `templates` folder contains:
- **`upload.html`**: A file upload form with a submit button that displays extracted data in a structured table format.

---

## Usage

### 1. Start the FastAPI Server
Run the server using Uvicorn:
```bash
uvicorn main:app --reload
```

### 2. Access the Web Interface
Navigate to `http://127.0.0.1:8000/upload` in a browser:
- Upload a PDF file through the form.
- View the extracted data on the result page.

### 3. API Endpoint
Use the `/extract` endpoint for direct API interaction.

---

## Example Workflow

1. Place the PDF file in the project directory or upload it via the web interface.
2. Start the FastAPI server using Uvicorn.
3. Use the `/upload` endpoint for HTML-based interaction or `/extract` for API-based processing.
4. View the extracted data either as JSON (API).

---

## Notes

- Ensure regex patterns are updated to match changes in the PDF layout or format.
- Install the required libraries before running the script:
  ```bash
  pip install fastapi uvicorn pdfplumber jinja2
  ```
- Use responsive design principles in the HTML templates for better usability.
