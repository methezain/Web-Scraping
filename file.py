import os
from docx import Document

def docx_to_text(docx_path, text_path):
    try:
        doc = Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        with open(text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)
        return True
    except Exception as e:
        print(f"Error processing {docx_path}: {str(e)}")
        return False

# Specify the directory path for the Word files
docx_directory_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\NAVTTC ML'

# Specify the directory path for the output text files
text_directory_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\NAVTTC ML'

# Initialize a list to store the names of failed Word files
failed_docx = []

# Iterate over the files in the Word directory
for filename in os.listdir(docx_directory_path):
    if filename.endswith(".docx"):
        docx_file = os.path.join(docx_directory_path, filename)
        text_file = os.path.join(text_directory_path, f"{os.path.splitext(filename)[0]}.txt")
        if not docx_to_text(docx_file, text_file):
            failed_docx.append(filename)

# Print the names of the Word files that failed
if failed_docx:
    print("The following Word files could not be converted to text:")
    for doc in failed_docx:
        print(doc)
