import os
from pdfminer.high_level import extract_text

def pdf_to_text(pdf_path, text_path):
    try:
        text = extract_text(pdf_path)
        with open(text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)
        return True
    except Exception as e:
        print(f"Error processing {pdf_path}: {str(e)}")
        return False

# Specify the directory path for the PDF files
pdf_directory_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\IHC Case Law\Cases PDFs'

# Specify the directory path for the output text files
text_directory_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\IHC Case Law\Output TXT'

# Initialize a list to store the names of failed PDF files
failed_pdfs = []

# Iterate over the files in the PDF directory
for filename in os.listdir(pdf_directory_path):
    if filename.endswith(".pdf"):
        pdf_file = os.path.join(pdf_directory_path, filename)
        text_file = os.path.join(text_directory_path, f"{os.path.splitext(filename)[0]}.txt")
        if not pdf_to_text(pdf_file, text_file):
            failed_pdfs.append(filename)

# Print the names of the PDF files that failed
if failed_pdfs:
    print("The following PDF files could not be converted to text:")
    for pdf in failed_pdfs:
        print(pdf)