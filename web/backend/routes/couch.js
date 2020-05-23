const express = require("express");
const router = express.Router();


router.get("/",async function(req, res, next){
    
    var shape = null

    let id = req.query.id;
    const nano = require("nano")("http://admin:data-miner!@172.26.133.36:5984");
    var db = nano.use('geo_json')
    await db.view('geo_json',"id",{key: 3458,include_docs: true
    }, function(err,res){
        if(!err){
            console.log(JSON.strinfigy(res));
            shape = JSON.stringify(res);
        }
        else{
            console.log(err)
        }
    })
/*
        .then((body) => {
            shape=body
        })
    console.log(shape)
    */


    res.send(shape);
});

module.exports = router;
