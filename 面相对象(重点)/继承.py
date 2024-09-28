class Father(object):  # 新类默认继承于object类 3.6之后可以省略 可以这么写 class Father:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def hello(self):
        print(f"hello {self.name}")

    @classmethod  # 声明类方法
    def get_name(cls):
        print(f"name is {cls.name}")

    @property  # 声明属性 将这个方法作为getter方法 可以直接访问 不需要调用
    def age(self):
        return self._age

    @age.setter  # 声明属性 将这个方法作为setter方法 可以直接赋值 不需要调用
    def age(self, age):
        if age < 0:
            raise ValueError("age must be positive")
        self._age = age


class Son(Father):
    def __init__(self, name, age, sex) -> None:
        super().__init__(name, age)
        self.sex = sex

    def hello(self):
        print(f"hello {self.name} {self.sex}")


if __name__ == "__main__":
    son = Son("chiko", 20, "male")
    son.hello()
    print(f"name is {son.name}, age is {son.age}, sex is {son.sex}")
