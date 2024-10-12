import requests

url = "https://fanyi.baidu.com/sug"

s = input("请输入你要翻译的英文单词")
data = {"kw": s}  # python请求直接字典格式 甚至都不要手动将他转为表单格式

# 发送post请求
resp = requests.post(url, data=data)  # data是表单格式 还可以传入json
# resp = requests.post(url, json=data) # 还可以传入json
print(resp.json())
