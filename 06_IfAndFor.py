a = input("a:")#input()返回的数据类型是str
a = int(a)
if a > 2:
    print(2)
elif a > 3:
    print(3)
else:
    print(a)

sum = 0
#for执行缩进块的语句
#break、continue用法类似C++
for x in list(range(10)):#range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
    sum = sum + x
    print(sum)