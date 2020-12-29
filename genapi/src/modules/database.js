const fs=require("fs")
const path=require("path")

class Files{
    //filename=null
    //data=null
    constructor(filename){
        this.filename="/Data/"+filename
    }
    readFile(callback){
        fs.readFile(path.join(__dirname+this.filename),'utf-8',(err,data)=>{
            if(err){
                console.log(err)
                callback(false)
            }
            else{
                this.data=data
                callback(JSON.parse(data))
            }
        })
        return this.data;
    }
    //createFile(){}
    //deleteFile(){}

} 

module.exports=function({filename,type,callback}){
    fetch_all=()=>{
        var f=new Files(filename)
        f.readFile((data)=>{
            if(data!=false){
                callback(data)
            }else{
                callback(null)
            }
        })
        return {}
    }
    if(type=="fetch_all"){
        return fetch_all()
    }
}

