from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    webpage = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=', 'r').text 

    soup = BeautifulSoup(webpage , 'lxml') 

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx') 

    print("Enter skill you are unfimiliar with (i.e linux, database)")  
    unfimiliar_skills = input('>').lower()
    print(f"Filtering out {unfimiliar_skills}")

    for index, job in enumerate(jobs):
        date_published = job.find('span', class_='sim-posted').span.text
        
        if 'few' or '1' or '6' in date_published:
            job_name = job.find('strong', class_='blkclor').text
            company_name = job.find('h3', class_='joblist-comp-name').text.replace('\n','').replace('  ','').replace(' ','-')
            job_location = job.find('span').text
            skills_required = job.find('span', class_='srp-skills').text.replace('\n','').replace('  ','').replace(',',', ')
            job_link = job.header.h2.a['href']
            
            if unfimiliar_skills not in skills_required:
                with open(f'posts/{index} - {unfimiliar_skills} excluded.txt', 'w') as f:
                    f.write(f"Company Name : {company_name}\n")
                    f.write(f"Job Location : {job_location}\n") 
                    f.write(f"Skills Required : {skills_required}\n") 
                    f.write(f"Job Link : {job_link}") 
                print(f"Files saved : {index} - {unfimiliar_skills} excluded.txt")
                
                
                
refresh_time = int(input('Refresh Time seconds (i.e 15): '))

while True:
    find_jobs()
    print(f"Waiting for {refresh_time} seconds...")
    time.sleep(refresh_time)  
        
        
        
        


    
    
     
