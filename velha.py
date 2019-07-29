from random import randint
from random import choice

grid = [[' ','|',' ','|',' '],
        ['-','+','-','+','-'],
        [' ','|',' ','|',' '],
        ['-','+','-','+','-'],
        [' ','|',' ','|',' ']]

sequences = list()
user_symbol = ' '
prog_symbol = ' '
players = int()
time = 1

def show():
    for i in range(0,5):
        print()
        for j in range(0,5):
            print(f' {grid[i][j]}', end = '')
    print()

def numberOfPlayers():
    global players
    players = int(input('\n How many players? '))
    while players < 1 or players > 3:
        players = int(input(' How many players? '))

def takeSymbol(players):
    global user_symbol
    global prog_symbol
    if players == 1:
        user_symbol = input(' X or O? ')
        if user_symbol not in 'XO':
            print(' Alright then...')
            prog_symbol = choice(['X','O'])
        elif user_symbol == 'X':
            prog_symbol = 'O'
        else:
            prog_symbol = 'X'
    else:
        user_symbol = input(' Player1: X or O? ') 
        if user_symbol not in 'XO':
            print(' Alright then...')
        prog_symbol = input(' Player2: X or O? ') 
        if prog_symbol not in 'XO':
            print(' No problem...')
    print()

def readCoordinates():
    global grid
    if players == 2:
        print(f' Player{time}:',end='')
    print(' Enter the coordinates [0,2]:')
    x = int(input(' x: '))
    y = int(input(' y: '))
    if x not in range(0,3) or y not in range(0,3) or grid[x * 2][y * 2] != ' ':
        print(' Unavailable coordinates, please try again.')
        x = int(input(' x: '))
        y = int(input(' y: '))
    if time == 2:
        grid[x * 2][y * 2] = prog_symbol
    else:
        grid[x * 2][y * 2] = user_symbol

def separate():
    global sequences
    sequences = [[grid[0][0], grid[0][2], grid[0][4]],
                 [grid[2][0], grid[2][2], grid[2][4]],
                 [grid[4][0], grid[4][2], grid[4][4]],
                 [grid[0][0], grid[2][0], grid[4][0]],
                 [grid[0][2], grid[2][2], grid[4][2]],
                 [grid[0][4], grid[2][4], grid[4][4]],
                 [grid[0][0], grid[2][2], grid[4][4]],
                 [grid[0][4], grid[2][2], grid[4][0]]]

def analyse():
    global user_symbol
    global prog_symbol
    for symbol in [prog_symbol,user_symbol]:
        for i in range(0,8):
            if sequences[i].count(symbol) == 2:
                if sequences[i][1] == symbol:
                    if sequences[i].index(symbol) == 0:
                        if sequences[i][2] == ' ':
                            return programTurn(i,2)
                    elif sequences[i].index(symbol) == 1:
                        if sequences[i][0] == ' ':
                            return programTurn(i,0)
                elif sequences[i][1] == ' ':
                    return programTurn(i,1)
    return programTurn(i)

def victoryOrDraw():
    flag = 1
    for i in range(0,8):
        if sequences[i].count(prog_symbol) == 3:
            if players == 1:
                return 'You lose!\n'
            else:
                return 'Player2 lose!\n'
        elif sequences[i].count(user_symbol) == 3:
            if players == 1:
                return 'You win!\n'
            else:
                return 'Player1 win!\n'
        elif ' ' in sequences[i]:
            flag = 0
    if flag == 1:
        return 'Draw!\n'  

def programTurn(i,j = -1):
    global grid
    if j == 0:
        if i == 4:
            j = 2
        elif i == 5 or i == 7:
            j = 4
        if i == 1 or i == 2:
            i *= 2
        else:
            i = 0
    elif j == 1:
        if i == 3:
            j = 0
        elif i == 5:
            j = 4
        else:
            j = 2
        if i == 2:
            i = 4
        elif i != 0:
            i = 2
    elif j == 2:
        if i == 3 or i == 7:
            j = 0
        elif i != 4:
            j = 4
        if i == 1:
            i = 2
        elif i != 0:
            i = 4
    elif j == -1:
        i = choice([0,2,4])
        j = choice([0,2,4])
        while grid[i][j] == user_symbol or grid[i][j] == prog_symbol:
            i = choice([0,2,4])
            j = choice([0,2,4])
    grid[i][j] = prog_symbol


show()
numberOfPlayers()
takeSymbol(players)
while(True):
    if time == 1 or time == 2:
        readCoordinates()
        if players == 1:
            time = 0
        elif time == 1:
            time = 2
        else:
            time = 1
    else:
        separate()
        analyse()
        time = 1
    show()
    separate()
    message = victoryOrDraw()
    if message != None:
        print(message)
        break
