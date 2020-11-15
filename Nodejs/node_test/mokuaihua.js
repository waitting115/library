const http = require('http');
const handleUrl = require('./modules/test');

// console.log(handleUrl.formatApi)

http.createServer((req, res) => {
    res.writeHead(200, {"Content-type": "text/html;charset='utf-8'"});

    const url = handleUrl.formatApi('/jingwe/18')
    res.write(url);

    res.end();
}).listen(3022)