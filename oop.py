class Cat:
    """这是一个猫类"""
    def __init__(self,new_name):
        print("Jerry is coming")
        #self.attribute = 属性的初始值
        self.name = new_name

    def eat(self):
        print("%s Eat Fish" % self.name)
    
    def __del__(self):
        print("Jerry is over")

    def __str__(self):
        return "Little cat is %s" % self.name
tom = Cat("Jerry")
print(tom)

class HouseItem:
    """家具类"""
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "%s 占地  %s 平方" % (self.name,self.area)

bed = HouseItem("席梦思", 4)
desk = HouseItem("yiyoujia", 5)
print(bed)
print(desk)

class Gun:
    def __init__(self,model):
        """"枪类"""
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0 :
            print("Bullet is over,shoot failed")
            return
        print("突突突突……")
        self.bullet_count -= 1
        print("Bullet is [%s]" % self.bullet_count)

solider = Gun("M416")
solider.add_bullet(0)
solider.shoot()


        