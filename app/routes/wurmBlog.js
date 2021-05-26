var express = require('express');
var router = express.Router();

/* GET home page. */
 router.get('/', function(req, res, next) {
  res.render('wurmBlog', { title: 'Wurmwelten...', subTitle: "Kompostwürmer. Was können sie, wozu sind sie gut?" });
});


module.exports = router;
