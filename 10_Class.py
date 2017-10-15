class Student(object):
    id = 12                                       #类属性，通过类名直接访问
    def __init__(self, name, score, rank):        #构造函数，函数名固定
        self.name = name                          #实例属性，当通过实例对象访问实例属性不存在时，会继续访问类属性，优先级实例属性 > 类属性
        self.score = score                        #实例属性
        self.__rank = rank                        #实例属性

    def print_score(self):
        print('%s: %s %s' % (self.name, self.score, self.__rank))

stu = Student("luyujia", 100, 1)
print(stu.name)
stu.print_score()


#实例的变量名如果以两个 下划线__ 开头，就变成了一个私有变量（private）

#可以外部直接给实例增加变量
stu.__rank = 2
print(stu.__rank)
stu.print_score()

# 表面上看，外部代码“成功”地设置了__rank变量，但实际上这个__rank变量和class内部的__rank变量不是一个变量！
# 内部的__rank变量已经被Python解释器自动改成了_Student__rank，而外部代码给bart新增了一个__rank变量


class Animal(object):
    def run(self):
        print('Animal is running...')

#继承
class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

#多态
def run(animal):
    animal.run()

dog = Dog()
cat = Cat()
run(dog)
run(cat)

#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
class Timer(object):
    def run(self):
        print('Start...')
timer = Timer()
run(timer)


#获取实例的类型
#type()
print(type(dog))
#isinstance()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
#dir() 获得一个对象的所有属性和方法
print(dir(dog))