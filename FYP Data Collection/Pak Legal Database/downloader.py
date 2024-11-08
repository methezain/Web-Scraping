import requests
from Scraper_downloader import pdf_links

# Loop over each link and download the PDF
for i, link in enumerate(pdf_links, 1):
    response = requests.get(link)
    if response.status_code == 200:
        with open(rf"C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\Pak Legal Database\pdf's\file_{i}.pdf", "wb") as file:
            file.write(response.content)
        print(f"Downloaded file_{i}.pdf")
    else:
        print(f"Failed to download from {link}")
