const model = require('../model/dashboard');
//const form = require('../views/form/formKunden')
var connection     = require('../lib/dbconn');

/* function listActionDash(request, response){
  model.getTemp().then(
    temp => {
      response.render('../views/index', { temp , title:"Dashboard"});
      console.log(temp)
    },
    error => response.send(error),
  );
}

function renderIndex(req, res) {

    res.render('../views/index',{ temp, title: 'Gewächshausweltren...' });
}

*/

function listActionDash(request, response){
  model.getTemp().then(
    temp => {
//      console.log(temp);
      var unten = temp.map(a => a.unten);
      var oben = temp.map(a => a.oben);
      var aussen = temp.map(a => a.aussen);
      var datum = temp.map(a => a.datum);
      var stunde = temp.map(a=> a.stunde);
      console.log(stunde);
//      for(var i in stunde) {
//        stunde.push(stunde[i].stunde);
//        hum.push(data[i].hum);
//      }
      var minute = temp.map(a=> a.minute);
//      var datum = {JSON.stringify(datum1)}
      response.render('../views/index', {stunde, minute, unten, oben,aussen, datum: datum, title: "Digitale Gewächshauswelten..."});
//      console.log(JSON.stringify(datum));
    },
    error => response.send(error),
  );
}

module.exports = {
  listActionDash,
//  renderIndex,
}
