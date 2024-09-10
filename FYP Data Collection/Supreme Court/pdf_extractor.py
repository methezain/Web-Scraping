from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine

text_content = ""

for page_layout in extract_pages(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Supreme Court\Supreme_Court_Case.pdf"):
    page_text = ""
    for element in page_layout:
        if isinstance(element, (LTTextBox, LTTextLine)):
            page_text += element.get_text() + "\n"

    text_content += page_text + "\n\n"


file_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Supreme Court\Cases_TXT'

with open(rf"{file_path}\output.txt", "w", encoding="utf-8") as f:
    f.write(text_content)