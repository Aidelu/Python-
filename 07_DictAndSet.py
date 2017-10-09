#dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
print('Bob' in d)   #通过in判断key是否存
d.pop('Bob')
print(d.get('Bob', -1)) #通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value

#set 
#add
#remove
s = set([1, 1, 2, 2, 3, 3])
s2 = set([1, 4, 5])
print(s)
print(s & s2)   #与
print(s | s2)   #或