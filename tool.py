import os
import requests
from bs4 import BeautifulSoup

def download_images_from_html(html_file_path, download_folder='images'):
    # Ensure the download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Find all img tags
    img_tags = soup.find_all('img')
    
    for img in img_tags:
        src = img.get('src')
        if src and (src.endswith('.png') or src.endswith('.jpg')):
            try:
                # Download the image
                img_data = requests.get(src).content
                img_name = os.path.basename(src)
                img_path = os.path.join(download_folder, img_name)
                
                # Save the image to the download folder
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)
                print(f"Downloaded {src} to {img_path}")
            except Exception as e:
                print(f"Failed to download {src}: {e}")

# Example usage
download_images_from_html('index.html')
