import re
res=re.search(r'cat|dog','the cat is here')
print(res)

res1=re.findall(r'..at','the cat in the hat went splat.')
print(res1)

res2=re.findall(r'^\d','1 is a number')
print(res2)

res3=re.findall(r'\d$','1 is a number,2')
print(res3)

phrase='there are 3 numbers 34 inside 5 this sentence'
pattern=r'[^\d]+'
res4=re.findall(pattern,phrase)
print(res4)

test_phrase='this is a sentence!but it has a punctuation.how can we remove it?'
res5=re.findall(r'[^!.? ]+',test_phrase)
res5=' '.join(res5)
print(res5)

print('\n')

text='only find the hyphen-word in this sentence.but you dont know how long-ish they are.'
pattern=r'[\w]+-[\w]+'
res6=re.findall(pattern,text)
print(res6)

print('\n')
text1='hello, would you like some catfish?'
text2='hello, would you like to take some catnap?'
text3='hello, have you seen this caterpillar?'

res7=re.search(r'cat(fish|nap|claw)',text2)
print(res7)