# 爬虫：通过编写程序来获取到互联网上的资源
# 百度
# 需求：用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容
# 用python搞定以上的需求，非常简单
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)
# print(resp)

# print(resp.read().decode("utf-8"))

# 将html读取到文件中
with open("mybaidu.html", mode="w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
print("over")
