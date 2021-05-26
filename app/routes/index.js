var express = require('express');
var router = express.Router();
const model = require('../model/dashboard');
const {
  listActionDash,
//  renderIndex,
}= require('../controller/dashboard');
/* GET home page. */
/* router.get('/', function(req, res, next) {
  res.render('index', { title: 'Gewächshausweltren...' });
});
*/
router.get('/',listActionDash);

module.exports = router;
