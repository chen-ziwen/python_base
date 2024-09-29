"""
接收一个函数作为参数
嵌套一个包装函数, 包装函数会接收原函数的相同参数，并执行原函数，且还会执行附加功能
返回嵌套函数
"""

import time


def decorator(func):
    def punch():
        t = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        func(t)  # 相当于把test函数作为参数传入执行

    return punch  # 必须返回包装函数


@decorator
def test(time):  # 果然可以这样用 装饰器好强
    print(f"{time} chiko 打卡成功！")


test()


# 进阶例子
def decoratorUpd(func):
    def punch(*args, **kwargs):  # *args 可变长参数 **kwargs 可变长关键字参数
        print(time.strftime("%Y-%m-%d", time.localtime(time.time())))
        func(*args, **kwargs)

    return punch


@decoratorUpd
def test2(name, age):
    print(f"{name} {age} 打卡成功！")


@decoratorUpd
def test3(reason, **kwargs):
    print(reason)
    print(kwargs)


test3("chiko", name="chiko", sex="男", age=99)
