import os
import requests
from bs4 import BeautifulSoup

# Функція для збереження посилання на скріншот у файлі з назвою гри
def save_screenshot_url(screenshot_url, game_name):
    folder_path = "scripts/temp/URLS"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filename = os.path.join(folder_path, f"{game_name}.txt")
    with open(filename, "a") as file:
        file.write(screenshot_url + "\n")

# Зчитуємо посилання з файлу urls.txt та виконуємо код для кожного з них
with open("scripts/temp/urls.txt", "r") as file:
    for line in file:
        url = line.strip()  # Видаляємо зайві пробіли та переноси рядка

        # Отримання HTML-коду сторінки
        response = requests.get(url)
        html_content = response.text

        # Парсинг HTML-коду
        soup = BeautifulSoup(html_content, "html.parser")

        # Перевірка наявності елемента з назвою гри
        app_name_element = soup.find("div", class_="apphub_AppName ellipsis")
        if app_name_element:
            game_name = app_name_element.text.strip()
            game_name = game_name.replace(":", "")  # Усуваємо символ ":" у назві гри для назви файлу
        else:
            # Якщо назву гри не знайдено, шукаємо посилання з атрибутом data-panel
            game_name_element = soup.find("a", {"data-panel": True})
            if game_name_element:
                game_name = game_name_element.text.strip()
            else:
                print(f"Could not find game's name on {url} page... Skipping")
                continue

        actual_media = soup.find("div", class_="actualmediactn")
        if actual_media:
            screenshot_url = actual_media.find("a")["href"]
            save_screenshot_url(screenshot_url, game_name)
            print(f"Screenshot link from {url} page saved in {game_name}.txt")
        else:
            print(f"Could not find screenshot link on {url} page... Skipping")

print("Screenshots link list created successfully. Proceeding...")
print("\n")
