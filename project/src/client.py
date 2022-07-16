from game_result import GameResult
from game import Game
from game_status import GameStatus



def end_of_game_handler(result: GameResult):
    print(f'Questions asked : {result.questions_passed}. Mistakes made : {result.mistakes_made}.')
    print(f'You won' if result.won else 'You lost')
    

game = Game('project/src/data/Questions.csv', 3, end_of_game_handler)

while game.game_status == GameStatus.IN_PROGRESS:
    # if game.is_last_question():
    #     print('No more questions')
    #     break
    q = game.get_next_question()
    print("Do you believe in the next statement or question? Enter 'y' or 'n' ")
    print(q.text)

    answer = input() == 'y'
    if q.is_true == answer:
        print('Well Done! You are right!')
    else: 
        print('Ooops, actually you are mistaken. Here is the explanation:')
        print(q.explanation)

    game.give_answer(answer)
   
