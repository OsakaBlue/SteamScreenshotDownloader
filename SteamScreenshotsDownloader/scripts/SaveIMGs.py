import os
import requests
import uuid
from urllib.parse import urlparse

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def download_image(url, folder_name):
    response = requests.get(url)
    if response.status_code == 200:
        # Отримання імені зображення з URL або генерація випадкового імені
        image_name = os.path.basename(urlparse(url).path)
        if not image_name:
            image_name = str(uuid.uuid4()) + '.jpg'
        with open(os.path.join(folder_name, image_name), 'wb') as f:
            f.write(response.content)
            print(f"Screenshot downloaded: {image_name}")
    else:
        print(f"Could not save screenshot from {url}")

def process_txt_file(file_path):
    folder_name = os.path.join("Screenshots", os.path.splitext(os.path.basename(file_path))[0])
    create_folder_if_not_exists(folder_name)

    with open(file_path, 'r') as file:
        for line in file:
            image_url = line.strip()
            download_image(image_url, folder_name)

if __name__ == "__main__":
    txt_files = [os.path.join("scripts", "temp", "URLS", file) for file in os.listdir(os.path.join("scripts", "temp", "URLS")) if file.endswith('.txt')]
    
    if not txt_files:
        print("Could not find TXT files (links) in scripts\\temp\\URLS ")
    else:
        for txt_file in txt_files:
            print(f"Processing {txt_file}...")
            process_txt_file(txt_file)


print("\n")
