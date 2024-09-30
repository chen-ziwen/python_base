#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 当同一个类实例化出来的对象 调用同一个方法 但是方法展示出不同的结果 就叫多态


class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    # @property  # 定义getter方法
    # def name(self):
    #     return self.name

    def login(self):
        pass

    def logout(self):
        pass


# vip用户
class VipUser(User):

    def __init__(self, name, age, sex) -> None:
        super().__init__(name, age)
        self.sex = sex

    def login(self):
        print(f"尊敬的VIP用户{self.name} 恭喜您登录成功")

    def logout(self):
        print(f"尊敬的VIP用户{self.name} 恭喜您退出成功")


# 普通用户
class NormalUser(User):

    def __init__(self, name, age, sex) -> None:
        super().__init__(name, age)
        self.sex = sex

    def login(self):
        print("{}，恭喜您登录成功".format(self.name))

    def logout(self):
        print("{}，恭喜您退出成功".format(self.name))


# 多态 不同的用户调用会返回不同的执行结果
def printUserInfo(user):
    user.login()
    user.logout()


if __name__ == "__main__":
    # vip用户
    vip_user = VipUser("chiko", 18, "男")
    print(vip_user.name)  # 输出chiko 相当于调用了getter方法
    printUserInfo(vip_user)

    print("------------")
    # 普通用户
    normal_user = NormalUser("张三", 38, "男")
    printUserInfo(normal_user)
