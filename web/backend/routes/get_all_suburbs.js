const express = require("express");
const router = express.Router();

//const env_ip = process.env.COUCHDB_HOST

//ip = env_ip.replace(/"/g,"");

ip = "http://admin:data-miner!@172.26.133.36:5984"



const nano = require("nano")(ip);

router.get("/",async function(req, res, next){
    console.log(req.query.city)
    
    var shape = [] 
    let id = req.query.id;
    var db = nano.use('postcode_aurin')
    await db.view("get_all",req.query.city).then((body) => {
        body.rows.forEach((doc) => {
            shape.push(doc.value);
        });
    });
    res.send(shape);
});

module.exports = router;
