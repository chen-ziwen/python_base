"""
接收一个函数作为参数
嵌套一个包装函数, 包装函数会接收原函数的相同参数，并执行原函数，且还会执行附加功能
返回嵌套函数
"""

import time


def decorator(func):
    def punch():
        print(time.strftime("%Y-%m-%d", time.localtime(time.time())))
        func()  # 相当于把test函数作为参数传入执行

    return punch  # 必须返回包装函数


@decorator
def test():
    print("chiko 上班打卡")


test()
