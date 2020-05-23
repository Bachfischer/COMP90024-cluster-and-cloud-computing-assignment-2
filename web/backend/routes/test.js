var express = require("express");
var router = express.Router();

var shapefile = require("shapefile");

/*var fs = require('fs'),
    path = require('path'),
    filePathSHP = path.join(__dirname,'Australia_Polygon.shp');
    filePathDBF = path.join(__dirname,'Australia_Polygon.dbf');
var shape =[]

shapefile.open(filePathSHP,filePathDBF)
    .then(source => source.read()
        .then(function log(result){
            if(result.done) return;
            shape.push(result.value)
            return source.read().then(log);
        }))
    .catch(error => console.error(error.stack));
*/
router.get("/",function(req, res, next){
    res.send(shape);
});

module.exports = router;
