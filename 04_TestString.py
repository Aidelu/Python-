print('包含中文的str')

print(ord('A')) #获取字符的整数表示

print(chr(66))  #把编码转换为对应的字符

x = b'ABC'  #Python对bytes类型的数据用带b前缀的单引号或双引号表示
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print( '中文'.encode('utf-8'))

#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
print(b'ABC'.decode('ascii'))

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
print(len('中文'))    #str
print(len('中文'.encode('utf-8')))    #bytes

'''
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
'''
print( 'Hi, %s, you have $%d.' %('Michael', 1000000))
