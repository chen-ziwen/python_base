# -*-coding:utf-8-*-
""" 列表 函数& 方法"""

list1 = [5, "5", 5, False, {}, "hello world"]
num_list = [1, 2, 3, 4, 5]

# 返回列表长度
len1 = len(list1)
print(len1)

# 返回列表最大值
max1 = max(num_list)
print(max1)

# 返回列表最小值
min1 = min(num_list)
print(min1)

# 将元组转换为列表
tuple1 = list((1, 2, 3, 4, 5))
print(tuple1)

# 在列表末尾添加新的对象
list1.append(True)
print(list1)

# 统计某个元素在列表中出现的次数
count = list1.count(5)
print(count)

# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list1.extend(num_list)
print(list1)

# 从列表中找出某个值第一个匹配项的索引位置
idx = list1.index(5)
print(idx)

# 将对象插入列表
num_list.insert(5, 6)
print(num_list)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
val = num_list.pop()
print(val)
val1 = num_list.pop(0)
print(val1)

# 移除列表中的一个元素（参数是列表中元素），并且不返回任何值
list1.remove("5")
print(list1)

# 反向列表中元素
num_list.reverse()
print(num_list)

# 对原列表进行排序
num_list.sort()
print(num_list)
