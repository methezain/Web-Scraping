import re
txt_path = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\IHC Case Law\output.txt'
with open(txt_path, 'r') as f:
    text = f.read()

pattern = r"([A-Za-z\s\.]+)\.\s*VS\s*([A-Za-z\s\.]+)(?=\s+and)"

match = re.search(pattern, text)

if match:
    name1 = match.group(1).strip()
    name2 = match.group(2).strip()
    print(f"First Name: {name1}")
    print(f"Second Name: {name2}")
else:
    print("Names not found") 