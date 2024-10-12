let url = "https://movie.douban.com/j/chart/top_list";

// 参数
const params = { "type": 11, "interval_id": "100:90", "action": "", "start": 0, "limit": 20 };

const headers = {
    // 请求载体的身份标识 大部分请求如果不带上这个标识 网站将会检测为异常ip请求
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

// nodejs比起python麻烦不少 需要手动拼接url
const query = new URLSearchParams(params).toString();
url = `${url}?${query}`;

fetch(url, {
    method: "GET",
    headers: headers, // 看抓包工具的请求头中是否有Content-type 没有就是没有请求体 一般get请求也不会带请求体
}).then(resp => resp.json()).then(data => {
    console.log(data);
})