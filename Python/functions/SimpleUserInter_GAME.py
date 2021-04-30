game_list=[0,1,2]
def display_game(game_list):
    print('Here is the game list : ')
    print(game_list)


def postion_choice():
    choice='WRONG'
    while choice not in ['0','1','2']:
        choice=input('Pick a postion (0,1 or 2) : ')
        if choice not in ['0','1','2']:
            print('Sorry ,invalid choice! ')
    return int(choice)


def replacemnt_choice(game_list,postion):
    user_placemnt=input('enter a string to place at that postion : ')
    game_list[postion]=user_placemnt
    return game_list


def gameon_choice():
    choice='WRONG'
    while choice not in ['Y','N']:
        choice=input('Keep Playing? (Y OR N) : ')
        if choice not in ['Y','N']:
            print('i dont understand ')
    if choice =='Y':
        return True
    else:
        return False


game_on=True
game_list=[0,1,2]
while game_on:
    display_game(game_list)

    postion=postion_choice()

    game_list=replacemnt_choice(game_list,postion)

    display_game(game_list)

    game_on=gameon_choice()