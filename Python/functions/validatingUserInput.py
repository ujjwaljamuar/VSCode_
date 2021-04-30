def user_choice():
    choice='WRONG'
    acceptable_range= range(0,10)
    within_range=False

    while choice.isdigit()==False or within_range==False :
        choice=input('enter a digit between 0 to 10 : ')
        #digit check
        if choice.isdigit()==False:
            print('Sorry! this is not a digit. ')
            #range check
        if choice.isdigit()==True:
            if int(choice) in acceptable_range:
                within_range=True
            else:
                print('Sorry!Not in Range')
                within_range=False
    return print(int(choice))
user_choice()