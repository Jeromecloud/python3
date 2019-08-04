class Dog(object):
    # 类属性归类所有
    count = 0
    name = 0

    #类方法
    @classmethod
    def runrun(cls):
        #在方法内部，可以通过cls或者类名访问类属性或类方法
        print("%s run fast " % cls.name)
    
    #实例方法
    def __init__(self,name):
        self.name = name
        Dog.count += 1
    def bark(self):
        print("Bark")
    
    #静态方法
    #不需要访问类属性和方法，也不需要访问实例属性和方法
    #通过类名调用
    @staticmethod
    def www():
        print("wowwow")

class God(Dog):
    def bark(self):
        print("Fly")

Dog.www()

wangcai = Dog("旺财")
wangcai.bark()
Dog.runrun()

#实例属性归实例所有，可以不在类里面
wangcai.hello = 0

print(Dog.count)
print(wangcai.hello)

