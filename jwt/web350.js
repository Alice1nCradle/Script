const jwt = require('jsonwebtoken');
var fs = require('fs');
var privateKey = fs.readFileSync('public.key');
var token = jwt.sign({ user: 'admin' }, privateKey, { algorithm: 'HS256' });
console.log(token)