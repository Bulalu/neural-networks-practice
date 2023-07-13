import PyPDF2
import re

def read_pdf(file_path):
    # Open the PDF file in binary mode
    with open(file_path, 'rb') as file:
        # Initialize a PDF file reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize an empty list to store the PDF text
        pdf_text = []
        count = 0
        # Loop through each page in the PDF
        for page in pdf_reader.pages:
            # Extract the text from the page
            if count >= 1:
                    break
            text = page.extract_text()
            
            # split the text into lines
            lines = text.split('\n')
            count += 1
            for line in lines:
                # Split the line on 'KE' or 'ME' and keep the left part
               
                left_part = re.split(' KE | ME ', line)[0]
                pdf_text.append(left_part)
                
            
    # Return the extracted text
    return pdf_text

# Usage
file_path = 'data1.pdf'
print(read_pdf(file_path))
