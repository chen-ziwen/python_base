class Person:
    var1 = "chiko"

    def __init__(self, name, age, sex) -> None:  # 构造函数 TS中的constructor
        self.name = name
        self.age = age
        self.sex = sex
        pass

    @classmethod  # 类方法
    def get_name(cls):
        """
        类方法的第一个参数是类本身，不是实例对象 为什么叫cls 其实这是一个编程规范
        """
        print(f"name is {cls.var1}")

    def hello(self):  # 实例方法
        print(f"hello {self.var1}")


person = Person("chiko", 20, "male")
# Person.get_name()  # 类方法

# 重写hello实例方法
Person.hello = lambda self: print(f"hello {self.var1} again")
# 重写get_name类方法
Person.get_name = lambda: print(f"name is {Person.var1} again")

person.hello()
Person.get_name()
