//const path=require("path")
const fs=require("fs");
/*class DataBase{
    //database;
    constructor(database){this.database="../Data/"+database}
    fetch_all(){
        var f=new File(this.database)
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
    //create(data){}
    //delete(key,value){}
}
*/
const DataBase=function(app,{database,query,data}){
    app.get('fetch/all/:database',req,res=>{
        console.log(req.params.database)
        res.end(JSON.stringify({"data":"[{'key':'value1'}]"}))
    });
}
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