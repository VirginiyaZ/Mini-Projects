import random
from time import sleep
# checking for the interger  + set range up as 'boundary'
def is_valid(n,boundary):
    return n.isdigit() and 1 <= int(n) <= boundary +1

def answer():

    while True:
        answer = input('Желаете ли сыграть еще разок?  ')
        if 'да' in answer.lower() or 'yes' in answer.lower():
            show_time()
        elif 'нет' in answer.lower() or 'no' in answer.lower():
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

def show_time():
    print('Добро пожаловать в числовую угадайку!')
    sleep(0.13)
  
    boundary = int(input('Введите верхнюю границу диапазона игры: '))
    num = random.randint(1, boundary)
    attemps = 0
    while True:
        n = input()
        if not is_valid(n, boundary):
            print(f'А может быть все-таки введем целое число от 1 до {boundary}?')
            continue
          
# Здесь идет сама угадайка и в случае если выборали повторить игру      
        n = int(n)
        if n == num:
            attemps += 1
            print('Вы угадали, поздравляем! Число попыток:', attemps)
            sleep(0.13)
            print('Хотите сыграть еще разок?) (Да/Нет) или (Yes/No)')
            break
        if n < num:
            print('Ваше число меньше загаданного')
            attemps += 1
        if n > num:
            print('Ваше число больше загаданного')
            attemps += 1

show_time()
answer()

    


