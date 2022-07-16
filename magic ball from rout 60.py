import random
from time import sleep

def greetings_answers(answers):
    print('Привет Вопрошайка, я магический шар, и я знаю ответ на любой твой вопрос.')
    sleep(1.45)
    print('Давайте знакомится! ')
    name=input('Как Вас зовут?   ')
    print('Рад познакомится',name,'!')
    
    while True:
        ask_qsn = input('Что вас волнует?  ')
        if ask_qsn != '':
            sleep(1.55)
            print(random.choice(answers))
        
        ask_variable = input("Хочешь задать еще один вопрос? (да/нет) или ('yes/no')")   
        if 'да' in ask_variable.lower() or 'yes' in ask_variable.lower():
            pass
        elif 'нет' in ask_variable.lower() or 'no' in ask_variable.lower():
            print('Возвращайся если возникнут вопросы!')
            break

answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова",
    "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
greetings_answers(answers)    
