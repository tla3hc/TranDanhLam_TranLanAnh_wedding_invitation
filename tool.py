import os
import requests
from bs4 import BeautifulSoup

def download_images_from_html(file_path):
    file_path = os.path.abspath(file_path)
    with open(file_path, 'r') as f:
        contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')

    for img in soup.find_all('img'):
        src = img.get('src')
        if src.endswith('.png') or src.endswith('.jpg'):
            response = requests.get(src, stream=True)
            if response.status_code == 200:
                with open(os.path.join('images', os.path.basename(src)), 'wb') as out_file:
                    out_file.write(response.content)
            
download_images_from_html('index.html')
