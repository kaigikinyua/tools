const express=require("express")
const path=require("path")
const app=express()

//const DataBase=require("./modules/database")
//import  DataBase from './modules/database';
//app.set("view engine","ejs")

app.get("/",(req,res)=>{
    res.sendFile(path.join(__dirname+"/views/index.html"))
});

app.get('/fetch/all/:database',(req,res)=>{
    console.log(req.params.database)
    res.end(JSON.stringify({"data":"[{'key':'value1'}]"}))
});

app.get('/fetch/filter/:database/:query',(req,res)=>{
    var database=req.params.database;
    var query=req.params.query
    console.log(query)
    res.end(JSON.stringify({"data":"['key':'fetch filter not implemented']"}))
})


app.listen(4000,()=>{
    console.log("GENapi running on port 4000")
})


