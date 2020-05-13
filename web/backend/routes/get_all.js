const express = require("express");
const router = express.Router();

const nano = require("nano")("http://admin:data-miner!@172.26.132.56:5984");

router.get("/",async function(req, res, next){
    
    var shape = [] 
    let id = req.query.id;
    var db = nano.use('geo_json')
    
    await db.view('get_all',"id").then((body) => {
        body.rows.forEach((doc) => {
            console.log(doc.value);
            shape.push(doc.value);
        });
    });
    res.send(shape);
});

module.exports = router;
