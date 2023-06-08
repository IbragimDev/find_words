import random
import os

letters = [
    "kitob",
    "ruchka",
    "stol",
    "telefon",
    "monitor",
    "klaviatura",
    "noutbuk",
    "ko'cha",
    "uy",
    "televidenie",
    "radio",
    "muzika",
    "tarjimon",
    "davlat",
    "dorilar",
    "ilm-fan",
    "sinf",
    "shaxs",
    "tadbirkor",
    "dastur",
]
words = random.choice(letters)
words = words.lower()

answers = 5
w_words = []
message = ""
while True:
    os.system("cls")
    secret = ""
    for i in words:
        if i in w_words:
            secret += i
        else:
            secret += "#"
    print(secret)
    print(f"Urinishlar soni {answers}")
    print(message)
    if answers <= 0:
        print(f"Sizda {answers} urinish qoldi va yutqazdingiz")
        break
    elif "#" not in secret:
        print("Siz yutdingiz")
        break
    input_word = input("Biron harf kiriting ").lower()

    if input_word in w_words:
        message = f"Siz {input_word} harfini kiritib bo`lgansiz !"
    elif input_word in words:
        message = f"So`zda {input_word} harfi bor"
        w_words.append(input_word)
    else:
        message = f"So`zda {input_word} harfi yo`q"
        answers -= 1
input("Chiqish uchun Enter tugmasini bosing")
