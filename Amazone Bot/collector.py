import os
import pandas as pd
from bs4 import BeautifulSoup 

d = {'Product Name':[], 'Product Price':[], 'Product Link': []} 


directory = 'C:\\Users\\pcinf\\OneDrive - Higher Education Commission\\Coding\\Web Scraping\\files'

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    
    if file.endswith('.html') and os.path.isfile(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            t = soup.find('h2')
            title = t.get_text()
            
            p = soup.find('div', {'data-cy':'secondary-offer-recipe'})  
            p2 =  p.find('span', {'class':'a-color-base'})  
            price = p2.get_text()
            
            l = t.find('a')
            link = 'https://www.amazon.com' + l['href'] 
            
            d['Product Name'].append(title)
            d['Product Price'].append(price)
            d['Product Link'].append(link)
            
            print("\n========================================\n\n")
        except Exception as e:
            print(f"Error reading file {file}: {e}")
    else:
        print(f"Skipping {file} (not an HTML file or not a file)")

df = pd.DataFrame(data=d)
df.to_csv("Laptopd_ata.csv")




