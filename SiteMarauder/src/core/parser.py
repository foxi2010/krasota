from bs4 import BeautifulSoup  

def parse_page(html):  
    soup = BeautifulSoup(html, 'lxml')  
    title = soup.find('h1').text.strip()  
    content = soup.find('div', class_='content').text  
    return {"title": title, "content": content}  