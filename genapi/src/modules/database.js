const fs=require("fs")
const path=require("path")

class Files{
    constructor(filename){
        this.filename="/Data/"+filename+".json"
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
class Database{
    static tables:(database)=>{
        var f=new Files(database);
        var data=f.readFile((data)=>{
            if (data!=false){
                return data;
            }else{console.log("Error while reading file")}
        });
    }
}

module.exports=function({filename,type,callback,query}){
    fetch_all=()=>{
        var f=new Files(filename)
        f.readFile((data)=>{
            if(data!=false){callback(data)}
            else{callback(null)}
        })
        return {}
    }
    filter=()=>{
        if(query==undefined || query==null || query==false) return {}
        var f=new Files(filename)
        f.readFile((data)=>{
            if(data!=false){callback(data)}
            else{
                //filter data
            }
        })
    }
    if(type=="fetch_all"){
        return fetch_all()
    }else if(type=="filter"){
        return filter()
    }else{

    }
}

