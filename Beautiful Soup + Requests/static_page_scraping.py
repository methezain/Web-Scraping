from bs4 import BeautifulSoup 

with open('html files/sample_page.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content , 'lxml')
    course_cards = soup.find_all('div', class_='card-body')  
    
    
    for each_Course in course_cards:
        course_name = each_Course.h5.text 
        course_price = each_Course.a.text.split()[0]   
        
        print(f"{course_name} costs {course_price}")
        

        
        