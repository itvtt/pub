const express = require('express');
const app = express();


var mysql = require('mysql2');
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '1234',
    database: 'testdb'
});

// MySQL 연결
connection.connect((err) => {
    if (err) {
      console.error('MySQL connection failed: ', err);
      throw err;
    }
    console.log('Connected to MySQL');
  });
  
  // 루트 경로에 대한 핸들러
  app.get('/', (req, res) => {
    // MySQL에서 데이터를 가져오는 쿼리
    const query = 'SELECT * FROM user';
  
    connection.query(query, (err, results) => {
      if (err) {
        console.error('MySQL query error: ', err);
        res.status(500).send('Internal Server Error');
        return;
      }
  
      // HTML 페이지에 결과를 전달
      const data = results[0]; // 여기서는 첫 번째 결과만 사용하도록 가정
      res.send(`
        <html>
          <head>
            <title>MySQL Data</title>
          </head>
          <body>
            <h1>User Data</h1>
            <p>ID: ${data.id}</p>
            <p>User ID: ${data.userid}</p>
            <p>Username: ${data.username}</p>
          </body>
        </html>
      `);
    });
  });
  
  // 서버를 3000번 포트에서 시작
  app.listen(3000, () => {
    console.log('Server is running on port 3000');
  });