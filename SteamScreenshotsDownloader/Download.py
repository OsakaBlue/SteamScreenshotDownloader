import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys
import venv

print("Creating venv and getting python libraries... Wait...")
print("\n")

# Виконуємо команди для створення віртуального середовища
venv.create(".venv", with_pip=True, prompt='')

# Передаємо шлях до Python-інтерпретатора віртуального середовища
python_interpreter = os.path.join(os.getcwd(), ".venv", "Scripts", "python")

# Встановлюємо необхідні пакети у віртуальне середовище
subprocess.run([python_interpreter, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.run([python_interpreter, "-m", "pip", "install", "requests", "beautifulsoup4", "selenium"])

# Імпортуємо бібліотеки після встановлення
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def download_page():
    # Отримуємо URL з текстового поля
    url = url_entry.get()
    
    # Ініціалізуємо параметри для веб-драйвера Chrome (headless mode)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    
    #повідомлення
    print("Loading page and scraping HTML... It will take quite some time, if you have a lot of screenshots there...")
    print("Be patient. It is doing it.")

    try:
        # Відкриваємо веб-сторінку
        driver.get(url)

                
        # Отримуємо висоту сторінки
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        # Чекаємо, доки сторінка не завантажиться повністю
        while True:
            # Прокручуємо вниз до кінця сторінки
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # Чекаємо деякий час для завантаження нових елементів
            time.sleep(2)
            
            # Обчислюємо нову висоту сторінки після прокрутки
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            # Якщо нова висота сторінки не змінилася, це означає, що всі елементи загружені
            if new_height == last_height:
                break
                
            last_height = new_height
        
        # Отримуємо HTML-код завантаженої сторінки
        html_source = driver.page_source
        
        # Закриваємо веб-драйвер
        driver.quit()
        

         # Зберігаємо HTML-код у файл "sample.html" в папці scripts
        with open("scripts/temp/sample.html", "w", encoding="utf-8") as file:
            file.write(html_source)

        
        # Почекаємо 3 секунди
        time.sleep(3)
        
        # Запускаємо proceed.bat
        os.system("start proceed.bat")
        
        # Закриваємо вікно tkinter
        root.destroy()
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Створюємо вікно tkinter
root = tk.Tk()
root.title("Web Page Downloader")

# Додаємо поле для введення URL
url_label = tk.Label(root, text="Enter screenshot page URL (https://steamcommunity.com/id/YOUR_ID/screenshots/):")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Додаємо кнопку "OK"
ok_button = tk.Button(root, text="Confirm", command=download_page)
ok_button.pack(pady=10)

# Запускаємо головний цикл вікна tkinter
root.mainloop()