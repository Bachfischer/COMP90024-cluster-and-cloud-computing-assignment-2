var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var cors = require('cors')
var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var get_all = require("./routes/get_all");
var get_all_cities = require("./routes/get_all_cities");
var get_all_suburbs = require("./routes/get_all_suburbs");
var testAPI = require("./routes/test.js");
var couchDB = require("./routes/couch.js");
var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.disable('etag');
app.use(cors());
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/get_all',get_all);
app.use('/get_all_cities',get_all_cities);
app.use('/get_all_suburbs',get_all_suburbs);
app.use('/test', testAPI);
app.use('/couch', couchDB);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
app.listen(8000, function(){
    console.log("listening")
})
