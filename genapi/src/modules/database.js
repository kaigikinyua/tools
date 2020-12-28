const fs=require("fs")
const path=require("path")

module.exports=function({filename,type,callback}){
    console.log("Hello world")
    fetch_all=()=>{
        console.log("fetching all")
        filename="/Data/"+filename
        var read=fs.readFile(path.join(__dirname+filename),'utf-8',(err,data)=>{
            if(err){
                console.error(err)
                callback(false)
            }else{
                console.log(data)
                console.log("data read from "+filename)
                callback(JSON.parse(data))
            }
        });
        return {}
    }
    if(type=="fetch_all"){
        return fetch_all()
    }
}

/*class Files{
    //filename;data;
    constructor(filename){this.filename="../Data/"+filename}
    readFile(){
        var data=fs.createReadStream(this.filename,(err,data)=>{
            if(err){
                this.data=false
            }else{
                this.data=data
                console.log(data)
            }
        })
        return this.data;
    }
    //createFile(){}
    //deleteFile(){}

}*/ 