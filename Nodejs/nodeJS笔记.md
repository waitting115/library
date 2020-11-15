node自带服务器

vscode安装node snippets插件

输入node-http-server就会提示，点击，就会出现node-http-server简单的配置

## 基本配置

~~~js
//（node-http-server）自动生成的：
// var http = require('http');
// http.createServer(function (request, response) {
//   response.writeHead(200, {'Content-Type': 'text/plain'});
//   response.end('Hello World');
// }).listen(8081);

// console.log('Server running at http://127.0.0.1:8081/');

// 手动敲代码：
// const { resolveSoa } = require('dns');
const http = require('http');
const url = require('url');

// url = http://localhost:3001?name=jingwei&age=18

http.createServer((req, res) => {
    // console.log(req.url);
    res.writeHead(200, {'Content-type': 'text/html;charset="utf-8"'})

    // 由于网页小图标也会触发一次请求我们并不做回应，所以将其过滤掉
    if(req.url !== '/favicon.ico') {
        // console.log(url.parse(req.url, true).query)
        const msg = url.parse(req.url, true).query;
        const str = `您好，您的名字为：${msg.name}，您的年龄为：${msg.age}`;
        console.log(str);
        res.write(str);
    }

    res.end();    
}).listen(3001);

~~~

## supervisor

代码热更新

安装：

> cnpm i -g supervisor

用supervisor替代node命令：

> node hello_node.js  ------>   supervisor hello_node.js 



**解决 supervisor : 无法加载文件 C:\Users\charles\AppData\Roaming\npm\supervisor.ps1**

解决方法：

1.在win10 系统中搜索框 输入 Windows PowerShell，选择 管理员身份运行

2、打开了powershell命令行之后,输入set-ExecutionPolicy RemoteSigned，然后更改权限为A，最后通过 get-ExecutionPolicy 查看当前的状态

## 模块化

test.js（暴露属性方法）

~~~js
function formatApi (str) {
    return 'http://www.tangchaolizi.com/' + str
}

exports.formatApi = formatApi;
~~~

mokuaihua.js（使用属性方法）

~~~js
const http = require('http');
const handleUrl = require('./modules/test');

// console.log(handleUrl.formatApi)

http.createServer((req, res) => {
    res.writeHead(200, {"Content-type": "text/html;charset='utf-8'"});

    const url = handleUrl.formatApi('/jingwe/18')
    res.write(url);

    res.end();
}).listen(3022)
~~~

