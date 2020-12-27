const path=require("path")
const fs=require("fs")
class DataBase{
    database="";
    constructor(database){this.database=database}
    create(data){}
    delete(key,value){}
    fetch_all(){
        var f=File(this.database)
        var data=f.readFile()
        if(data!=false){
            return data;
        }else{
            console.error("Error while reading from file "+this.filename)
            return {}
        }
    }
    //fetch_filter(){}
    //update(){}
}

class Files{
    filename=""
    constructor(filename){this.filename=filename}
    readFile(){
        var data=fs.createReadStream(this.filename,(err,data)=>{
            if(err){
                return false
            }else{
                return data
            }
        })
    }
    //createFile(){}
    //deleteFile(){}

}