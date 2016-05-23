#Задача 9 Вариант 11.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать,
#есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". 
#Вслед за тем игрок должен попробовать отгадать слово.

#Лохина Л. М.
#20.05.2016

import random

WORDS = ("питон",
         "анаграмма",
         "простая",
         "сложная",
         "ответ",
         "подстаканник")
 
word = random.choice(WORDS)
 
print("\t\tЗдравствуй игрок!")
print("Попробуй угадать с пяти попыток слово, которое загадал компьютер.")
print("Ты можешь спрашивать, есть ли определенная буква в слове. А потом скажешь слово.")
print("Итак, поехали!")
print("\nКоличество букв в слове:", len(word))
 
tries = 5
letter = ()
while tries >= 1:
    letter = str(input("В загаданном слове есть буква: "))
    if letter not in word:
        tries -= 1
        print("\nВы ошиблись, такой буквы нет в слове!")
        print(" У вас осталось", tries, "попыток(ки)!")
    if letter in word:
        tries -= 1
        print("\nВы угадали, эта буква есть в слове!")
        print("У вас осталось", tries, "попыток(ки)!")

i_dont_know = "Не знаю"
print("\nВаши 5 попыток закончились, вы готовы угадать слово?")
print("Если вы сдались и не хотите продолжать, напишите 'Не знаю'.")
correct = (input("\nЭто слово: "))
 
while correct != word:
    print("Попробуйте еще раз!")
    correct = (input("\nЭто слово: "))
    if correct == word:
        print("\nПоздравляю! Вы выиграли!")
    if correct == i_dont_know:
        print("\nОчень жаль!")
        break
 
input("\nНажмите Enter, чтобы выйти...")