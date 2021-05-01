try:
    f=open('testfile','r')
    f.write('write a test line')
except TypeError:
    print('there was a type error!')
except OSError:
    print('All other exception')
finally:
    print('I always run.')


def ask_for_int():
    while True:
        try:
            result=int(input('plase provide a number : '))
        except:
            print('whoops! thats not a number')
            continue
        else:
            print('yes thank you')
            break
        finally:
            print('i am ging to ask you again')
ask_for_int()

def ask():
    while True:
        try:
            x=int(input('Provide an integer : '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
    print('Thank you the sqaure is ')
    print(x**2)
ask()