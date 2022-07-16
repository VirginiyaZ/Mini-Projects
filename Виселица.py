import random 
def hangman(word):
    wrong=0  ##  the counter of wrong letters 
    stages=["",
            "____________          ",
            "|                     ",
            "|          |          ",
            "|          0          ",
            "|         /|\         ",
            "|         / \         ",
            "|                     ",    
             ]

    rletters = list(word) ## a list which contains each symbol of WORD
    board = ["_"] * len(word) ## a list of strings which displayed during the game
    win = False  # Flag
    print('*** Welcome to the HangMan game ***')

    while wrong < len(stages)-1:  ## loop 
        print('\n')
        char_message=input('Enter any letter:  ')
        if char_message in rletters:
            add_letter=rletters.index(char_message)
            board[add_letter]=char_message
            rletters[add_letter] = '$' ## if the word has dublicates (similar letters) will be
        else:                          ## replased with $ to let the code itterate normaly
            wrong +=1
        print((" ".join(board)))

        range= wrong +1
        print('\n'.join(stages[0:range]))

        if '_' not in board:
            print('You win! The word was:  ')
            print(' '.join(board))
            win=True
            break
                

    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You loose! The word was: {}.'.format(word))
    

 
        
list_of_words = ['cat','dog','apple', 'vehickle', 'rainbow', 'forest', 'butterfly', 'dragonfly', 'flower', 'cloud', 'daisy',
                 'milk', 'goose', 'country', 'owl', 'programm',
                 ]
choice=random.choice(list_of_words)
hangman(choice)