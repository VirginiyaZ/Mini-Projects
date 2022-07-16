# for i in range(int(input())):
#     s = input()
#     print(s[::2], s[1::2])

# def find_digit(num):
#     left = 1
#     right=n
#     middle = (left + right)//2
#     count = 1
#     while middle != num:
#         middle = (left + right)//2
#         if middle < num:
#             left = middle+1
#             count +=1
#         elif middle > num:
#             right = middle -1
#             count +=1
#     print("Количество попыток :",round(count))
#     return middle 

# n = int(input())    
# num = n 
# print("Ваше число:",find_digit(num))   

# from math import ceil, log
# print(ceil(log(int(input()), 2)))

# N = int(input().strip())
# print("Weird" if ((N%2!=0) or (N%2==0 and N in range(6,21))) else "Not Weird")

# import random
# from time import sleep

# def greetings_answers(answers):
#     print('Привет Вопрошайка, я магический шар, и я знаю ответ на любой твой вопрос.')
#     sleep(1.45)
#     print('Давайте знакомится! ')
#     name=input('Как Вас зовут?   ')
#     print('Рад познакомится',name,'!')
    
#     while True:
#         ask_qsn = input('Что вас волнует?  ')
#         if ask_qsn != '':
#             sleep(1.55)
#             print(random.choice(answers))
        
#         ask_variable = input("Хочешь задать еще один вопрос? (да/нет) или ('yes/no')")   
#         if 'да' in ask_variable.lower() or 'yes' in ask_variable.lower():
#             pass
#         elif 'нет' in ask_variable.lower() or 'no' in ask_variable.lower():
#             print('Возвращайся если возникнут вопросы!')
#             break

# answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова",
#     "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
# greetings_answers(answers)    



import random 
# R=rock, S=Scissors, P=paper
should_continue =True # making a loop
while should_continue:
    player_choice = input('Player choice: [R/S/P]').lower()

    if player_choice not  in ['r', 's', 'p']:
        print('Incorrect input. Try again.')
        continue

    generate = {1:'r', 2:'s', 3:'p'}
    comp_choice = generate[random.randint(1,3)]

    print(f'Computer choice = {comp_choice}')

    winning_comb = [('p', 'r')], [('r', 's')],[('s', 'p')]

    if  player_choice == comp_choice:
        print('A draw')
    elif (player_choice,comp_choice) in winning_comb:
        print('Player wins')
    else:
        print('Computer wins')   
    
    ans_continue = input('Want to proceed? (y/n)').lower()
    if ans_continue  == 'y':
        continue
    else:
        print('Thank you! Catch you later!')
        break
