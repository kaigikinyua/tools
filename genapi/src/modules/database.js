const fs=require("fs")
class Files{
    //filename;data;
    constructor(filename){this.filename=filename}
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

}
module.exports = { DataBase } 