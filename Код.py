from task_integer21 import task_integer21
from task2_49 import task2_49
from task_boolean7 import task_boolean7

print("1 - Знайти кількість секунд з останньої хвилини")
print("2 - Обчислити значення y за формулою")
print("3 - Перевірка істинності висловлювання")
choice = input("Виберіть задачу (1, 2 або 3): ")

if choice == "1":
    task_integer21()
elif choice == "2":
    task2_49()
elif choice == "3":
    task_boolean7()
else:
    print("Невірний вибір.")
    
    
import math # підключення бібліотеки

def task_integer21(): #З початку доби минуло N секунд (N - ціле). Знайти кількість секунд, що
#пройшли з початку останньої хвилини.
    try:  # перевірка на помилки
        n = int(input("N (секунди) = "))
    except:  # якщо помилка
        print("N повинно бути цілим числом!")
        input("Натисніть Inter, щоб вийти...")
    else:  # якщо немає помилки
        res = n % 60
        print("Секунди з моменту останньої хвилини = ", res)

        
def task2_49(): 
    from math import sin, sqrt, log, radians, e
    try: # перевірка на помилки
        x = float(input("Введіть x = "))
    except: # якщо помилка
        print("x повинен бути ЧИСЛОМ!")
    else: # в іншому випадку
        try: # обчислення виразу
            numerator = 4 * (3 ** (2 * x - 2)) * (e ** x) * abs(sin(radians(127) + 2 * x))
            denominator = log(2 * abs(x / 2), 3)
            y = numerator / denominator
        except: # якщо помилка
            print("Проблема у розрахунках!")
        else: # в іншому випадку
            print("y =", y)

def task_boolean7(): # Дано три цілих числа: A, B, C. Перевірити істинність висловлювання: «Число B знаходиться між числами A і C».
    try: # введення чисел
        A = int(input("A = "))
        B = int(input("B = "))
        C = int(input("C = "))
    except: # перевірка на помилки
        print("Кожне число має бути цілим!")
        input("Натисність Inter для виходу...")
    else: # якщо помилок немає
        res = (A < B < C) or (C < B < A)  # перевірка, чи міститься В між А та С
        print("B між A та C:", res)
