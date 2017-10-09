#list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
#倒数第1个、倒数第2个、倒数第3个
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

classmates.append('Adam')   #往list中追加元素到末尾
classmates.insert(1, 'Jack')    #把元素插入到指定的位置
print(classmates)

classmates.pop()    #删除list末尾的元素
classmates.pop(1)   #删除指定位置的元素
print(classmates)


#tuple
#tuple和list非常类似，获取元素的方法和list是一样的，但是tuple一旦初始化就不能修改，所以代码更安全
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
t = (1)     #定义一个只有"1"元素的tuple
print(t)
t2 = (1,)   #定义一个只有1个元素的tuple
print(t2)

#“可变的”tuple
t = ('a', 'b', ['A', 'B'])
print(t)
