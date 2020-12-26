const express=require("express")

const app=express()

app.get("/",(req,res)=>{
    res.sendFile("views/index.html")
})

app.listen(4000,()=>{
    console.log("GENapi running on port 4000")
})