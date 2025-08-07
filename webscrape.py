import requests
from bs4 import BeautifulSoup
import os


url = 'https://www.indiatoday.in/'

response = requests.get(url)

if response.status_code == 200:
   html_content = response.text
else:
   print(f"Failed to retrieve page. Status code: {response.status_code}")
   exit()


soup = BeautifulSoup(html_content, 'html.parser')

file_path = 'Top_HeadLines.txt'

with open(file_path, 'w') as myfile:

    for h2 in soup.find_all('h2'):
        a_tag = h2.find('a')
        if a_tag:
            web_text = a_tag.get_text(strip=True)
            myfile.write(web_text + '\n')

if os.path.exists(file_path):
    if os.path.getsize(file_path) > 0:
        print(f"Top headlines saved in file {file_path}")
    else:
        print("The file is empty.")
else:
   print("The file does not exist.")

