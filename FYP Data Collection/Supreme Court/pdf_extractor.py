from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBox, LTTextLine
from bs4 import BeautifulSoup

# Initialize empty HTML content
html_content = ""

# Extract text from each page
for page_layout in extract_pages(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Supreme Court\Supreme_Court_Case.pdf"):
    page_text = ""
    for element in page_layout:
        if isinstance(element, (LTTextBox, LTTextLine)):
            page_text += element.get_text()

    # Wrap each page's content in a <div> with a class or id
    html_content += f'<div class="page" id="page-{page_layout.pageid}">\n{page_text}\n</div>\n'

# Use BeautifulSoup to create proper HTML structure
soup = BeautifulSoup(html_content, "html.parser")
formatted_html = soup.prettify()

# Save the result to an HTML file or print it
print(formatted_html)
