import requests
from bs4 import BeautifulSoup
import os

# Функція для отримання посилань з вказаного HTML-файлу
def get_links_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    links = []
    divs = soup.find_all('div', class_='imgWallHover')
    print(f"Знайдено {len(divs)} елементів з класом 'imgWallHover'.")

    for div in divs:
        img_id = div.get('id')
        if img_id and img_id.startswith('imgWallHover'):
            img_id = img_id.replace('imgWallHover', '')
            print(f"Отримано ідентифікатор з елемента 'imgWallHover': {img_id}")
            link = f"https://steamcommunity.com/sharedfiles/filedetails/?id={img_id}"
            links.append(link)
        else:
            print("Не вдалося знайти ідентифікатор для елемента 'imgWallHover'.")

    return links

# Функція для запису посилань у файл
def write_links_to_file(links, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')

# Викликаємо функції
html_file = 'scripts/temp/sample.html'  # Вкажіть шлях до вашого HTML-файлу
output_dir = 'scripts/temp'
output_file = os.path.join(output_dir, 'urls.txt')

# Перевірка наявності директорії для вихідного файлу
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

links = get_links_from_html(html_file)
print(f"Отримано {len(links)} посилань.")

write_links_to_file(links, output_file)

print(f"Посилання було збережено у файлі {output_file}.")
