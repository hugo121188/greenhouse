var mysql        = require('mysql');
var connection   = mysql.createConnection({
  supportBigNumbers: true,
  bigNumberStrings: true,
  host     : "localhost",
  user     : "greenhouse",
  password : "housedelagreen",
  database : "greenhouse"
});

module.exports = connection;
