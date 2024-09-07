from PyPDF2 import PdfReader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

reader = PdfReader(r"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Supreme Court\Supreme_Court_Case.pdf")

number_of_pages = len(reader.pages)

text = ''

for i in range(number_of_pages):
    page = reader.pages[i]
    text += page.extract_text() + '\n'  

print(text) 

