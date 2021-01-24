const fs=require("fs")
const path=require("path")

class Files{
    constructor(filename){
        this.filename="/Data/"+filename+".json"
    }
    readFile(){
        try{
            var data=fs.readFileSync(path.join(__dirname+this.filename),'utf-8')
            return data;
        }catch(e){
            console.error(`Could not read file ${this.filename}`)
            console.error(e)
            return false;
        }
    }
    //createFile(){}
    //deleteFile(){}
}
function filter({field,value,operand,data}){
    var data_obj=new Object()
    data_obj=data
    //search for the field
    //do operation in accordance with the operator
    switch(operand){
        case 'eq':
            console.log("Equal to")
            break;
        case 'lt':
            console.log("Less than")
            break;
        case 'gt':
            console.log("Greater than")
            break;
        case 'ne':
            console.log("Not equal to")
            break;
        default:
            console.log("Filter query")
    }
    //return data
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
        var data=f.readFile()
        if(data!=false){
            return data;
        }
        return {}
    }
    filter=()=>{
        if(query==undefined || query==null || query==false) return {}
        var f=new Files(filename)
        var data=f.readFile()
        var filtered_data=null;
        var splitters=['eq','lt','gt','ne']
        splitters.forEach(s=>{
            if(query.indexOf(s)!=-1){
                var split=query.split(s)
                var field=split[0];var value=split[1]
                filtered_data=filter({field:field,value:value,operand:s,data:data})
            }
        });

    }
    if(type=="fetch_all"){
        return fetch_all()
    }else if(type=="filter"){
        return filter()
    }else{

    }
}

