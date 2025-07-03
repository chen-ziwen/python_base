chiko = {"name": "chiko", "age": 25}

# 第一种 利用 + 连接字符串
str1 = "my name is " + chiko["name"] + " and my age is " + str(chiko["age"])

# 第二种 利用 % 格式化字符串
str2 = "my name is %s and my age is %d" % (chiko["name"], chiko["age"])

# 第三种 利用 format 格式化字符串
# 注意 format 需要 Python 2.6 后可用
str3 = "my name is {} and my age is {}".format(chiko["name"], chiko["age"])

# 第四种 利用 f-string 格式化字符串 （最好用的一种，最接近 js 的模板字符串）
# 注意 f-string 需要 Python 3.6 后可用
str4 = f"my name is {chiko['name']} and my age is {chiko['age']}"

print("第一种输出：", str1)
print("第二种输出：", str2)
print("第三种输出：", str3)
print("第四种输出：", str4)
