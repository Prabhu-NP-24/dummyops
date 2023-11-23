// var express = require('express');
// var app = express();

// app.get('/', function (req, res) {
//   res.send('<h1>Just Do IT !!!</h1>');

// });

// var server = app.listen(3000, function () {
//   var port = server.address().port;

//   console.log('Your nodejs app is listening at port %s',  port);
// });

const fs = require('fs');
const path = '/usr/src/app/data/log.txt';

fs.writeFileSync(path, 'Hello, Docker! This is a Task 5 log entry.', { flag: 'a' });
console.log('Log entry written to', path);