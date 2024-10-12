const url = "https://fanyi.baidu.com/sug";
// const s = prompt("请输入你要翻译的英文单词")

// 其实模拟请求很简单 如果是post请求就去看请求头中的格式是什么
// 如果是json那就转换成json 如果是表单 但就转换成对应的表单格式

const data = {
    kw: "hello"
}

fetch(url, {
    method: "POST",
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    // 这个请求体的格式为表单默认编码类型
    body: new URLSearchParams(data).toString()
}).then(resp => resp.json()).then(data => {
    console.log(data);
})