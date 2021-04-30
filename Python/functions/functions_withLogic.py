def even_check(num):
    result=num%2==0
    return result
print(even_check(20))

#method 2
def even_checker(numb):
    return numb%2==0
print(even_checker(55))

#return true if any number is even inside a list
print('\n3 > \n')
def check_even_list(num_list):
    for number in num_list:
        if number%2==0:
             return True
        else:
            pass
    return False
print(check_even_list([1,3,5]))
print(check_even_list([2,1,2]))
print(check_even_list([2,2,2]))
print(check_even_list([1,2,1]))

#4> return all the even number in a list>
print('\n4> \n')
def check_even_lists(num_lists):
    even_numbers=[]
    for numbers in num_lists:
        if numbers%2==0:
            even_numbers.append(numbers)
        else:
            pass
    return even_numbers
print(check_even_lists([2,8,6,9,7]))
print(check_even_lists([1,3,5,7,9]))