from PIL import Image, ImageDraw, ImageFont
import random
import time

def new_year_greeting():
    # Запрос имени пользователя
    name = input("Введите ваше имя: ")

    # Список случайных поздравительных фраз с чёрным юмором
    phrases = [
        "{name}, с Новым годом! Пусть твоя жизнь в следующем году станет лучше... или хотя бы не хуже, чем у рыбы в аквариуме!",
        "С Новым годом, {name}! Желаю тебе столько счастья, чтобы сосед начал завидовать и задумался о переезде!",
        "{name}, поздравляю! Новый год - это возможность снова попытаться стать взрослым, а потом сдаться и пойти есть торт!",
        "С Новым годом, {name}! Пусть твои мечты сбываются, а кошмары остаются в 2023-м. Да, включая утренние понедельники!"
        "{name}, с Новым годом! Пусть твоя жизнь в следующем году станет лучше... или хотя бы не хуже, чем у рыбы в аквариуме!",
        "С Новым годом, {name}! Желаю тебе столько счастья, чтобы сосед начал завидовать и задумался о переезде!",
        "{name}, поздравляю! Новый год - это возможность снова попытаться стать взрослым, а потом сдаться и пойти есть торт!",
        "С Новым годом, {name}! Пусть твои мечты сбываются, а кошмары остаются в 2023-м. Да, включая утренние понедельники!"
    ]

    # Выбор случайной поздравительной фразы
    greeting = random.choice(phrases)

    arts = [
    """
           *
          ***
         *****
        *******
       *********
          |||
          |||
        """]
     # Выбор случайной поздравительной фразы и ASCII-арта
    greeting = random.choice(phrases).format(name=name)
    art = random.choice(arts)

    # Печать с эффектом печатной машинки
    print("\n" + art)
    for char in greeting:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

# Вызов функции
new_year_greeting()