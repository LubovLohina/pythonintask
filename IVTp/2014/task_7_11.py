#Задача 7. Вариант 11.
#Разработайте систему начисления очков для задачи 6, 
#в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.



#Лохина Л. М.
#16.04.2016

import random

print ('Программа случайным образом загадывает название одного из девяти действующих вокзалов Москвы, а игрок должен его угадать.')

n = random.randint(1,9)

if n==1:
	station = 'Белорусский'
elif n==2:
	station = 'Казанский'
elif n==3:
	station = 'Киевский'
elif n==4:
	station = 'Курский'
elif n==5:
	station = 'Ленинградский'
elif n==6:
	station = 'Павелецкий'
elif n==7:
	station = 'Рижский'
elif n==8:
	station = 'Савеловский'
elif n==9:
	station = 'Ярославский'

trial = 8
bonus = 8000

while trial > 0 :	
	answer = input ('\nНазовите один из вокзалов: ')
	if answer.lower() == station.lower():
		print('\nВы угадали!!!')
		print ('Вам начислено', bonus, 'баллов.')
		break
	else:
		print("\nВы не угадали!!!")
		trial -= 1
		bonus -= 1000
		if trial > 1:
			print ('Попробуйте еще раз.')
		else:
			print("Правильный ответ: " , station)


input("\n\nНажмите Enter для выхода.")
