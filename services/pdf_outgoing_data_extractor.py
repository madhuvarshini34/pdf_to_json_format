import os
import re
import pdfplumber
from collections import deque


class OutgoingPDFData:
    def __init__(self, pdf_folder_path: str):
        self.pdf_folder_path = pdf_folder_path

    @staticmethod
    def safe_search(pattern, line, group=1, default="Unknown"):
        match = re.search(pattern, line)
        return match.group(group) if match else default

    def extract_outgoing_pdf(self, pdf_file_name: str):
        pdf_path = os.path.join(self.pdf_folder_path, pdf_file_name)

        # Check if the file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"File '{pdf_file_name}' not found in the folder.")

        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

        lines = deque(text.splitlines())
        

        # Regular expressions for fields (same as before)
        fields = {
            "environment": r"Environment:\s+([\w\-]+)",
            "aba": r"ABA:\s+(\d+)",
            "mode": r"Mode:\s+([\w\-]+)",
            "service_unit": r"Service Unit:\s+(\d+)",
            "cycle_date": r"Cycle Date:\s+([\d/]+)",
            "system_date/time": r"System Date/Time:\s+([\d/: ]+)",
            "status": r"Status:\s+([\w\-]+)",
            "message_type": r"Message Type:\s+([\w\-]+)",
            "create_time": r"Create Time:\s+([\d/: ]+)",
            "test/prod": r"Test/Prod:\s+([\w\-]+)",
            "imad": r"IMAD:\s+([\w\d ]+)",
            "omad": r"OMAD:\s+([\w\d ]+)",
            "sender_aba": r"Sender ABA \{\d+\}:\s+(\d+)",
            "sender_name": r"Sender ABA \{\d+\}:\s+\d+\s+([\w &]+)",
            "receiver_aba": r"Receiver ABA \{\d+\}:\s+(\d+)",
            "receiver_name": r"Receiver ABA \{\d+\}:\s+\d+\s+([\w &]+)",
            "amount": r"Amount \{\d+\}:\s+([\d.]+)",
            "type/subtype_code": r"Type/Subtype Code \{\d+\}:\s+([\w \-]+)",
            "business_function": r"Business Function \{\d+\}:\s+([\w \-]+)",
            "sender_reference": r"Sender Reference \{\d+\}:\s+([\w+(\d+)]+)",
            "reference_for_beneficiary": r"Reference for Beneficiary \{\d+\}:\s+([\w+(\d+)]+)",
        }

        originator_fields = {
            "originator_id_code": r"ID Code[:\s]+([\w \-]+)",
            "originator_identifier": r"Identifier[:\s]+([\w\d]+)",
            "originator_name": r"Name[:\s]+([\w ]+)",
            "originator_address": r"Address[:\s]+([^\n]+)",
            "originator_to_beneficiary_information_text": r"Text[:\s]+([\w ]+)",
        }

        beneficiary_fields = {
            "beneficiary_id_code": r"ID Code[:\s]+([\w \-]+)",
            "beneficiary_identifier": r"Identifier[:\s]+([\w\d]+)",
            "beneficiary_name": r"Name[:\s]+([\w ]+)",
            "beneficiary_address": r"Address[:\s]+([^\n]+)",
            "beneficiary_information_text":  r"Text[:\s]+([\w ]+)",
        }
        
        extracted_data = {}
        current_group = None

        while lines:
            line = lines.popleft().strip()

            # Detect section markers
            if "Originator {5000}" in line or "Originator to Beneficiary Information {6000}" in line:
                current_group = "Originator"
                continue
            elif "Beneficiary {4200}" in line or "Beneficiary Information {6400}" in line:
                current_group = "Beneficiary"
                continue

            # General fields
            for field_name, pattern in fields.items():
                value = self.safe_search(pattern, line)
                if value != "Unknown":
                    if field_name == "amount":  # Convert amount to float
                        extracted_data[field_name] = float(value)
                    else:
                        extracted_data[field_name] = value

            # Originator fields
            if current_group == "Originator":
                for field_name, pattern in originator_fields.items():
                    value = self.safe_search(pattern, line)
                    if value != "Unknown":
                        extracted_data[field_name] = value
                        break

            if current_group == "Beneficiary":
                for field_name, pattern in beneficiary_fields.items():
                    value = self.safe_search(pattern, line)
                    if value != "Unknown":
                        extracted_data[field_name] = value
                    
        for field_name in fields.keys():
            if field_name not in extracted_data:
                extracted_data[field_name] = None
                

    
        return extracted_data
        
