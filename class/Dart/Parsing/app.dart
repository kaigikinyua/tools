import 'dart:io';
import 'dart:convert';
import './model.dart';
main(){
  stdout.write("Here are your current todos\n");
  Map<String,dynamic> todos= json.decode(Files.readFile());
  List<dynamic> todoList=todos["todos"];
  var mytodos=TodoListModel.fromJson(todoList);
  print(mytodos.toJson());
  print("Would you like to add a todo\ny/n");
  
  var addTodo=stdin.readLineSync();
  
  if(addTodo=="y"){
    Todo newTodo=MyTodos.addTodo();
    todoList.add(newTodo);
    Map<String,dynamic> decodedTodo=mytodos.toJson(); 
    var dataToFile='{ "todos":'+json.encode(decodedTodo)+'}';
    
    print(dataToFile);
    //Files.writeFile(dataToFile.toString());
  }
}


class MyTodos{
  //input output operations
  static Todo addTodo(){
    print("Todo task=> ");
    var tdo=stdin.readLineSync().toString();
    print("Time=> ");
    var time=stdin.readLineSync().toString();
    var newTodo= new Todo(todo: tdo,time: time,routine: false);
    return newTodo;
  }
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