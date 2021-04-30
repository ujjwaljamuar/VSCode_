#Q1 > Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
st = 'Print only the words that start with s in this sentence'
print('Q no. 1')
for word in st.split():
    if word[0]=='s' or word[0]=='S':
        print(word)
for word in st.split():
    if word[0].lower()=='s':
        print(word)

# Q2 > Use range() to print all the even numbers from 0 to 10.
print('Q NO.2')
mylist=[x for x in range(0,11) if x%2==0]
print(mylist)
mylist1=[x for x in range(0,11,2)]
print(mylist1)

#Q3 > Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print('Q no. 3')
mylist=[x for x in range(1,50) if x%3==0]
print(mylist)
mylist1=[x for x in range(1,50,3)]
print(mylist1)

#Q4 > **Go through the string below and if the length of a word is even print "even!"**
print("Q no. 4")
st='print every word in this sentence that has even number of letters'
for word in st.split():
    if len(word) %2==0:
        print(word+ ' is even')

#Q5 > Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
#  and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
print('Q no. 5')
for num in range(1,101):
    if num%3==0 and num %5==0:
        print('fizzbuzz')
    elif num%3==0:
        print('fizz')
    elif num%5==0:
        print('buzz')
    else:
        print(num)

#Q 6 > Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
print('Q no. 6')
word1=[word[0] for word in st.split()]
print(word1)

