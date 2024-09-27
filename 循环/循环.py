stri = "hellow chiko"
tuplei = (1, 2, 3, 4, 5)
listi = [1, 2, 3, 4, 5]
dicti = {"name": "chiko", "age": 25, tuplei: listi}

"""for循环"""
# 对于字符串 打印出字符串每一项
for i in stri:
    print(i)

# 对于字典
for i in dicti:
    print(i)  # 打印每一项的键
    print(dicti[i])  # 打印每一项的值

# 对于列表和元组 用元组为例 列表同理
for i in tuplei:
    print(i)

# range函数 三个参数
for i in range(3):  # 等同于range(0,3) 等同于js的 for(i=0; i<3; i++)
    print(i)
for i in range(2, 8, 2):  # 等同于js的 for(i=2; i<8; i+=2)
    print(i)

"""while循环"""
count = 0
sum = 0
while count < 100:
    sum += 1
    count += 1
print(sum)

"""不同

之前也提到过了，如果一种语法能表示一个功能，那没必要弄两种语法来表示。

竟然都是循环，for 循环和 while 循环肯定有他们的区别的。

那什么时候才使用 for 循环和 while 循环呢？

- for 循环主要用在迭代可迭代对象的情况。

- while 循环主要用在需要满足一定条件为真，反复执行的情况。 （死循环+break 退出等情况。）

- 部分情况下，for 循环和 while 循环可以互换使用。

"""


for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d 是一个合数" % num)
            break
    else:
        print("%d 是一个合数" % num)

"""for循环跟else

当然，这里还用到了 for … else 语句。

其实 for 循环中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行。

当然有 for … else ，也会有 while … else 。他们的意思都是一样的。

"""
