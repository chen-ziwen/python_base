import requests

url = "https://www.baidu.com/s?wd=周杰伦"

# 通过设置 User-Agent来伪装请求的身份 不设置无法请求成功
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)

print(resp.text)
