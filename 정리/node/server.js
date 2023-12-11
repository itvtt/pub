const express = require('express');
const app = express();

app.listen(8080, function(){
    console.log('listening on 8080')
});

app.get('/pet', function(요청, 응답){
    응답.send('반갑습니다');
});


app.get('/beauty', function(요청, 응답){
    응답.send('ㅂ티페이지');
});

app.get('/beauty2', function(요청, 응답){
    응답.send('ㅂ티2페이지');
});

app.get('/', function(요청, 응답){
    응답.sendFile(__dirname + '/index.html');
});