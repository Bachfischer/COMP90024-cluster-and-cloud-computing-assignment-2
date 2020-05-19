const express = require("express");
const router = express.Router();

const env_ip = process.env.COUCHDB_HOST

ip = env_ip.replace(/"/g,"");

const nano = require("nano")(ip);

router.get("/",async function(req, res, next){
    
    var shape = [] 
    let id = req.query.id;
    var db = nano.use('aurin_postcode')
    
    await db.view('get_all',"id").then((body) => {
        body.rows.forEach((doc) => {
            console.log(doc.value);
            shape.push(doc.value);
        });
    });
    res.send(shape);
});

module.exports = router;
