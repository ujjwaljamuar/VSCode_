text="the agent's phone number is 405-525-6566.call soon"
print('phone' in text)

# regex
import re
pattern='phone'
match=re.search(pattern,text)
print(match)

pattern1='the'
match1=re.search(pattern1,text)
print(match1)

print(match.span())
print(match1.span())

#find all
matches=re.findall('phone',text)
print(matches)
print(len(matches))

for match in re.finditer('phone',text):
    print(match)
    print(match.group())