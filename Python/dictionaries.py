# unordered mappings for storing objects in an ordered sequence.uses { } braces &it cant be sorted means cant be indexed or sliced.
my_dic={'key1':'value1','key2':'value2'}

print(my_dic['key1'])

prices={'apple':'100','potato':'40',"milk":'rs 60'}
print('price of milk is '+prices['milk'])

d={'k1':10012,'k2':[0,1,2],'k3':{'inside key':100}}
print(d['k3']['inside key'])
print(d['k2'][2])

f={'key6':['a','b','c']}
print(f['key6'][2].upper())

#add key value to a dictionary

g={'k1':100,'k2':200}
g['k3']=300
print(g)

#print values by methods
print(g.keys())
print(g.values())
print(g.items())
