"""
    ____                  __    _  __                  
   / __ \____ _____  ____/ /__ | |/ /                  
  / /_/ / __ `/ __ \/ __  / _ \|   /                   
 / ____/ /_/ / / / / /_/ /  __/   |                    
/_/ ___\__,_/_/ /_/\__,_/\___/_/|_|     _              
   /  _/___  ____/ /_  _______/ /______(_)__  _____    
   / // __ \/ __  / / / / ___/ __/ ___/ / _ \/ ___/    
 _/ // / / / /_/ / /_/ (__  ) /_/ /  / /  __(__  )     
/___/_/ /_/\__,_/\__,_/____/\__/_/  /_/\___/____/      
                                                       
""" 

import time
import tkinter as tk
import tkinter.messagebox as messagebox
import webbrowser

def calculate_age():
    age = age_entry.get()
    if age.lower() == "rickroll":
        messagebox.showinfo("Rick Astley", "Я тебя зарикролил :3")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    else:
        try:
            age = int(age)
            result_label.config(text="Загрузка...")
            result_label.update()
            time.sleep(3)
            result_label.config(text=f"Поздравляем, вы долбоёб уже {age} лет!\nВыпьем за это :>")
        except ValueError:
            messagebox.showerror("Ошибка", "Некорректный ввод. Пожалуйста, введите число.")

# Выводим при запуске окно с приветствием
messagebox.showinfo("Привет", "Калькулятор был создан PandeX (vk.com/pandex_official).\nУважай его работу, это собственное производство")

# Создание графического интерфейса с помощью библиотеки Tkinter
root = tk.Tk()
root.title("Калькулятор возраста")

# Создание виджетов интерфейса
age_label = tk.Label(root, text="Введите свой возраст:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

calculate_button = tk.Button(root, text="Сделать физические расчеты вселенной (посчитать)", command=calculate_age)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Добавление текста "PandeX Industries" внизу окна
company_label = tk.Label(root, text="PandeX Industries", fg="gray")
company_label.pack(side="bottom")

# Запуск главного цикла событий для отображения интерфейса
root.mainloop()
