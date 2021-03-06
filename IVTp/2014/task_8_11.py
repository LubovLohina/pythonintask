#Задача 8. Вариант 11.
#Доработайте игру "Анаграммы" так, чтобы к каждому слову полагалась подсказка.
#Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
#Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

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
 
correct = word
 
i_dont_know = "Не знаю"
podskazka = word[0] + word[1] + word[2]
 
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
 
scores = 10
 
print(
    """
                        Добро пожаловать в игру 'Анаграммы'!
            Надо переставить буквы так, чтобы получилось осмысленное слово.
                        Если вам нужна подсказка введите: "Не знаю".
	        Но учтите, если вы не будете использовать подсказку, 
			кол-во заработанных очков будет больше.
                       (Для выхода нажмите Enter, не вводя своей версии.)
    """
)
print("Вот анаграмма: ", jumble)
guess = input("\nПопробуйте отгадать исходное слово: ")
while guess != "" and guess != correct:
    if guess != correct and not guess == i_dont_know:
        print("К сожалению, вы неправы.")
    if guess == i_dont_know:
        scores -= 5
        print("\nПодсказка! Первые три буквы слова!", podskazka)
    guess = input("Попробуйте отгадать исходное слово: ")
    if guess == correct:
        print("Да, именно так! Вы отгадали!\n")
 
if scores < 0:
    scores = 0
print("Спасибо за игру! У вас", scores, "очков!")
input("\n\nНажмите Enter, чтобы выйти...")