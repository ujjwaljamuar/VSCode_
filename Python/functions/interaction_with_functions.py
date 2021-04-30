#shuffle function
exapmle=[1,2,3,4,5,9]
from random import shuffle
shuffle(exapmle)
print(exapmle)

#by using functions
print('\n2> \n')
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result=shuffle_list(exapmle)
print(result)

#3
mylist=['','O','']
print(shuffle_list(mylist))

print('\n4>\n')
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input('pick a number 0,1 or 2 > ')
    return int(guess)
    my_index=player_guess()

def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print('correct')
    else:
        print('incorrect')
        print(mylist)

#initial list
mylist=[' ','O',' ']

#shuffled list
mixedup_list=shuffle_list(mylist)

#user guess
guess=player_guess()

#check the guess
check_guess(mixedup_list,guess)

