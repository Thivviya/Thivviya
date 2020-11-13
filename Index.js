var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
});

/* GET Lang page. */
router.get('/lang', function(req, res) {
  var db = req.db;
  var collection = db.get('cust');
  collection.find({},{},function(e,docs){
      res.render('lang', {
          "lang" : docs
      });
  });
})

module.exports = router;

