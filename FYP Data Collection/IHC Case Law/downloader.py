import requests

def file_downloader(links_list):
    path_to_save = r'C:\Users\pcinf\OneDrive - Higher Education Commission\Coding\Web Scraping\FYP Data Collection\IHC Case Law\Cases PDFs'

    for i, url in enumerate(links_list, start=1):
        response = requests.get(url)
        
        with open(rf'{path_to_save}\case_{i}.pdf', 'wb') as file:
            file.write(response.content)