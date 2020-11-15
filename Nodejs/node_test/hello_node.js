//自动生成的：
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
