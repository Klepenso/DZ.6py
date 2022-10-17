# Задача 1. Напишите программу, удаляющую из текста все слова содержащие "абв".

from ntpath import join

text = 'абвгдейка раз два три'

text = list(filter(lambda x: 'абв' not in x, text.split()))
text1 = " ".join(text)

print(text1)
