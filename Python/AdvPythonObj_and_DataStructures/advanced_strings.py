s='hello world'
s6=s.capitalize()
print(s6)

s1='hello world'
s1=s1.upper()
print(s1)

s2=s1.lower()
print(s2)

count_O=s.count('o')
print(count_O)

# find 
find_r=s.find('r')
print(find_r)

# center 
center_s=s.center(20,'z')
print(center_s)

# expand tab

print('hellp\thi'.expandtabs())

# check case

s3=s.isalnum()
print(s3)

# is upper and islower

s4=s.isupper()
print(s4)
s5=s.islower()
print(s5)

s7=s.isspace()
print(s7)

s8=s.istitle()
print(s8)

s9='hello'.endswith('o')
print(s9)
# or
s10='hello'
print(s10[-1]=='o')


# split 
s11='hello'.split('e')
print(s11)

# partition
s12='hello'.partition('l')
print(s12)