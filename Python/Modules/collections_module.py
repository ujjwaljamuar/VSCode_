from collections import Counter
mylist=[1,1,1,1,2,2,2,2,3,3,3,3]
print(Counter(mylist))

mylist1=['a','a',10,10,10]
print(Counter(mylist1))

print(Counter('aaaaaanncccccckkkddd'))

sentence='How many times does each word show up in this sentence with a word .'
print(Counter(sentence))
print(Counter(sentence.lower().split()))

print('\n')

letters='aaaabbbccccdddddddddd'
c=Counter(letters)
print(c)

print(c.most_common())
print(c.most_common(2))

print(list(c))


from collections import defaultdict
d={'a':10}
print(d['a'])


d=defaultdict(lambda:0)   #if the key is not present in it then it will print it as a default value
print(d['wwrong'])

print('\n')

mytuple=(10,20,30)
print(mytuple[0])

from collections import namedtuple
Dog=namedtuple('Dog',['age','breeed','name'])
sammy=Dog(age=65,breeed='husky',name='sam'
