#.format() method and f-strings string literals
n="hey! how you doing"

print(n[::-1])

print("hello {}".format("my name is ujjwal"))

print("hello {} {} {}".format("my ","surname","is"))

print("hello {2} {1} {0} {3}".format("how","you","doin'","!"))

print("hey ! {b} {c} {a} ".format(a="doin'",b="how",c="you"))

print("hey {r:1.4f}".format(r=4545656))

#f string
name="ujjwal"
age=19
print(f"hello, my name is {name} and i am {age} years old")