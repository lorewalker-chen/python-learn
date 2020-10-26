# 创建类
class Dog():
    def __init__(self, name, age):
        #初始化属性name和age
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")


# 使用类
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# 调用方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
your_dog = Dog('lucy', 3)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()