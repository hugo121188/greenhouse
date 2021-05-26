const model = require('../model/dashboard');
//const form = require('../views/form/formKunden')
var connection     = require('../lib/dbconn');

function renderIndex(req, res) {

    res.render('../views/user',{ title: 'Usergedöhnse' });
}


module.exports = {
  renderIndex,
}
