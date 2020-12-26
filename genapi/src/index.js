const express=require("express")
const path=require("path")
const app=express()

//app.set("view engine","ejs")

app.get("/",(req,res)=>{
    res.sendFile(path.join(__dirname+"/views/index.html"))
})


app.listen(4000,()=>{
    console.log("GENapi running on port 4000")
})