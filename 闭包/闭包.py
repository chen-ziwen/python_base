# python的闭包也是函数嵌套函数
time = 0


def study_time(time):
    def insert_time(min):
        # nonlocal time 声明变量不是局部变量，也不是全局变量，而是外部嵌套函数内的变量
        nonlocal time  # 没有JS的作用域链好使
        time += min
        return time

    return insert_time


study = study_time(time)  # 0是外部函数的参数

# 因为内部的函数引用到了外部函数的值，所以外部函数的变量不能被垃圾回收机制回收
print(study(1))  # 1
print(study(2))  # 3
print(study(3))  # 6
print(time)  # 0 全局变量没有被修改


"""如何判断闭包
有的，所有函数都有一个  __closure__ 属性，如果函数是闭包的话，那么它返回的是一个由 cell 组成的元组对象。cell 对象的 cell_contents 属性就是存储在闭包中的变量。
        
"""
print(
    study.__closure__
)  # (<cell at 0x00000250248B1E80: int object at 0x00000250243469D0>,)
print(study.__closure__[0].cell_contents)  # 6 闭包保存的值
