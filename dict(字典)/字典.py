dict = {"name": "chiko", "age": 25, "sex": "man", "is_good": False}
print(dict["name"])  # 只能这样写 不能通过.来访问

# dict （字典）键必须不可变，可是键可以用数字，字符串或元组充当，但是就是不能使用列表
# 其实字典就是哈希表，就是每个编程语言会有所不同的特性

str1 = str(dict)
print(str1)

# 以列表返回字典中的所有键
print(dict.keys())

# 以列表返回字典中的所有值
print(dict.values())

# 以列表返回可遍历的(键, 值) 元组数组
print(dict.items())
