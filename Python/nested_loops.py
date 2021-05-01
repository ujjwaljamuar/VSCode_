mylist=[]
for x in [2,4,6]:
    for y in [50,100,500]:
        mylist.append(x*y)
print(mylist)

#2nd method
mylist1=[x*y for x in[2,4,6] for y in [50,100,500]]
print(mylist1)

st = ' SAM Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower()=='s':
        print(word)
#other method
str = ' SAM Print only the words that start with s in this sentence'
for word in str.split():
    if word[0]=='s' or word[0]=='S':
        print(word)