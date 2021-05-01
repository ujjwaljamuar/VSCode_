l=[1,2,3]
l.append(4)
print(l)

# count
print(l.count(1))

# extend
x=[1,2,3]
x.append([4,5])
print(x)

x1=[1,2,3]
x1.extend([4,5])
print(x1)

print(l.index(2))

# insert
x2=[1,2,3]
x2.insert(2,'inserted')
print(x2)

# pop
ele=l.pop()
print(ele)
print(l)

l.pop(0)
print(l)

# remove
print(x2)
x2.remove('inserted')
print(x2)

x3=[1,2,3,4,3]
print(x3)
x3.remove(3)
print(x3)


# reverse
x3.reverse()
print(x3)