const express=require("express")
const path=require("path")
const app=express()

const Files=require("./modules/database")

app.get("/",(req,res)=>{
    res.sendFile(path.join(__dirname+"/views/index.html"))
});

app.get('/fetch/all/:database',(req,res)=>{
    console.log(req.params.database)
    var f=Files({filename:"test.json",type:"fetch_all",callback:(param)=>{
        if(param==false||param==undefined||param==null){}
        else{
            res.end(JSON.stringify(param))
        }
    }})
    //console.log(f)
    //res.end(JSON.stringify({"data":"[{'key':'value1'}]"}))
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


