'''
整数
浮点数
字符串（转义字符：\，Python还允许用r''表示''内部的字符串默认不转义）
布尔值(and or not)
空值:none
还有还有。。。
'''

#Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')

#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''1
2
3''')

#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

#除法：/  和  //
#//称为地板除，两个整数的除法仍然是整数，只取整数部分

