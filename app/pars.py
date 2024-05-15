from bs4 import BeautifulSoup
import sqlite3
import requests
url = 'https://studioband.info/tops.html'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
links = soup.find_all('a')
conn = sqlite3.connect('links.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS links (link TEXT)')
conn.commit()
for link in links:
    link_url = link['href']
    link_response = requests.head(link_url)
if link_response.status_code == 200:  # Проверка успешного статуса ответа
    cursor.execute('INSERT INTO links (link) VALUES (?)', (link_url,))
conn.commit()
conn.close()
