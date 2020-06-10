import 'dart:io';
import 'dart:convert';

main(){
 print(Files.readFile());
 String toFIle='{"todos":[{"todo":"learn dart"},{"todo":"learn flutter"}]}';
 Files.writeFile(toFIle);
}

class Files{
  static String readFile(){
     var file=File("todos.json");
     var fileData="";
     try{
       fileData=file.readAsStringSync();
     }catch(e){
       print(e);
     }
    return fileData;
  }
  static Future<bool> writeFile(String data) async{
    var file=File("todos.json");
    try{
      file.writeAsString(data);
      return true;
    }catch (e){
      print(e);
      return false;
    }
  }

}