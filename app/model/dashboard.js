var connection     = require('../lib/dbconn');

/* function getTemp(req, res, next) {
    var dbRequest = 'SELECT * FROM temp order by id desc limit 200';
    connection.query(dbRequest, function(error, rows) {
        if(rows.length !== 0) {
//            req.temp = rows[0];
            console.log(rows);
//            return next();
        }

        res.render('../views/error'); /* Render the error page.
    });
}
*/

function getTemp() {
  return new Promise((resolve, reject) => {
    const query = "SELECT oben, unten, aussen, date_format(datumZeit,'%a %H:%i') as stunde,time_format(datumZeit,'%i') as minute from temp order by id desc limit 200";
    connection.query(query, (error, results) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(JSON.stringify(results)));
//        resolve(results);
//        console.log(JSON.parse(JSON.stringify(results)));
      }
    });
  });
}

module.exports = {
  getTemp,
}
