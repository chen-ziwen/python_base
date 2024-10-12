import requests

url = "https://movie.douban.com/j/chart/top_list"

# 参数
params = {"type": 11, "interval_id": "100:90", "action": "", "start": 0, "limit": 20}

# 请求头
headers = {
    # 请求载体的身份标识 大部分请求如果不带上这个标识 网站将会检测为异常ip请求
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

resp = requests.get(url, params=params, headers=headers)
print(resp.text)
