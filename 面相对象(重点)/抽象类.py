from abc import ABCMeta, abstractmethod


class Pet(
    metaclass=ABCMeta
):  # 加上这个元类 如果子类没有实现该类的抽象方法 将无法被实例化
    def __init__(self, nickname, life):
        self._nickname = nickname
        self._life = life

    @abstractmethod
    def make_vocie(self):
        pass

    @abstractmethod
    def max_weight(self):
        pass


class Cat(Pet):

    def make_vocie(self):
        print("喵 喵 喵")

    def max_weight(self):
        print("20kg")

    pass


class Dog(Pet):
    def make_vocie(self):
        print("汪 汪 汪")

    def max_weight(self):
        print("80kg")

    pass


# cat和dog实例调用相同的方法 但是结果却不一样 这就是多态
cat = Cat("凯蒂", 10)
cat.make_vocie()
cat.max_weight()

dog = Dog("旺财", 20)
dog.make_vocie()
dog.max_weight()
