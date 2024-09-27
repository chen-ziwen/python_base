# 两数之和 如果参数不是整形或者浮点型 抛出错误
def sum(num1, num2):
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise TypeError("参数类型错误")
    return num1 + num2


print(sum(99, 89))


# 不带参数值的return语句返回None， 所以说None就类似于JS中的undefined
def test():
    pass


print(test())  # 返回None


# 函数可以同时返回多个值
def division(num1, num2):
    # 求商与余数
    a = num1 % num2
    b = (num1 - a) / num2
    return b, a  # 同时返回多个值，但其实是返回了一个元组


num1, num2 = division(9, 4)  # 类似于JS的解构
tuple = division(9, 4)

print(num1, num2)
print(tuple)

# 主要的参数类型有：默认参数、关键字参数（位置参数）、不定长参数。
# 参数类型和用法和JS基本一致，例如默认参数必须放在最后面
# python不同的是 默认参数的值是不可变的对象，比如None、True、False、数字或字符串 因为如果是可变对象后续操作修改了它 会造成很多麻烦


# python有关键字参数 这个非常好 JS不支持不过可以通过对象的形式来达到差不多的效果 下面是例子
def person(name, age, sex):
    print(name, age, sex)


person(sex="man", name="chiko", age=25)  # 可以自行决定函数参数顺序


# 不定长参数 类似JS中的...args
