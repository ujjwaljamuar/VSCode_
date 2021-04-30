''' \d -    a digit                        file_\d\d             file_25
    \w -    alphanumeric                   \w-\w\w\w             A-b 1
    \s -    white spaces                   a\sb\sc               a b c
    \D -    non digit                      \D\D\D                ABC
    \W -    non alphanumeric               \W\W\W\W              +-*/
    \S -    non white space                \S\S\S\S              Yoyo

Quantifiers :-
    +       occurs one or more time        versiom \w-\+         version A-b1_1
    {3}     occurs exactly 3 times         \D{3}                 abc
    {2,4}   occurs 2 to 4 times            \d{2,4}               123
    {3,}    occurs 3 or more times         \w{3,}                anycharacters2
    *       occurs 0 or more times         A*B*C*                AAAACCCCC
    ?       once or more                   plurals?              plural
    ^       used to exclude things
'''
import re
text=('my phone number is 408-555-1234')
phone=re.search('\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone)
print(phone.group())

print('\n')
phonee=re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phonee.group())

print('\n')
phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultts=re.search(phone_pattern,text)
print(resultts.group())
print(resultts.group(1))
print(resultts.group(2))
print(resultts.group(3))