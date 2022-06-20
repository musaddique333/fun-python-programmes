import random


def computer():
    comp = random.choice(t)
    game(comp)


def user():
    print('\n\tr = rock, p = paper,s = scissors\n')
    print('\n\tEnter 69 to exit\n')
    play = input()
    if play == "r":
        play = "rock"
    elif play == "p":
        play = "paper"
    elif play == "s":
        play = "scissors"
    return play


def opted_ones(u, c):
    print(f'\nYou opted {u} computer opted {c}')


def defeat():
    print("\n\n\t\tYou loose!")
    computer()


def victory():
    print('\n\n\t\tYou win!!!')
    computer()


def game(c):
    u = user()
    if u == c:
        opted_ones(u, c)
        print('\nDraw!! try again')
        computer()
    elif u == 'rock' and c == 'paper':
        opted_ones(u, c)
        defeat()
    elif u == 'rock' and c == 'scissors':
        opted_ones(u, c)
        victory()
    elif u == 'paper' and c == 'rock':
        opted_ones(u, c)
        victory()
    elif u == 'paper' and c == 'scissors':
        opted_ones(u, c)
        defeat()
    elif u == 'scissors' and c == 'paper':
        opted_ones(u, c)
        victory()
    elif u == 'scissors' and c == 'rock':
        opted_ones(u, c)
        defeat()
    elif u == '69':
        print('\n\n\tThanks for playing!!')
    else:
        print('\n\n\tWrong hand sign!! please try again')
        computer()



t = ('rock', 'paper', 'scissors')
computer()
