s=set()
s.add(1)
s.add(2)
s.add(2)
print(s)

# clear the set
s.clear()
print(s)

s1={1,2,3}
s2=s1.copy()
print(s2)
s1.add(4)

# difference method
diff=s1.difference(s2)
print(diff)

# difference update
s3={1,2,3}
s4={1,4,5}
s3.difference_update(s4)
print(s3)

# discard 
s5={1,2,3,4,5}
s5.discard(2)
print(s5)

# intersection
s6={1,2,3}
s7={1,2,4}
s8=s6.intersection(s7)
print(s8)

s6.intersection_update(s7)
print(s6)

# is disjoint

s9={1,2}
s10={1,2,4}
s11={5}
dj=s9.isdisjoint(s10)
print(dj)
print(s10.isdisjoint(s11))

# is subset
s12={1,2}
s13={1,2,4}
print(s12.issubset(s13))


print(s12.symmetric_difference(s13))

print(s12.symmetric_difference_update(s13))

#union

print(s12.union(s13))
print(s12.update(s13))