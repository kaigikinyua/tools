class TodoListModel{
  List<Todo> todos;
  TodoListModel({this.todos});
  TodoListModel.fromJson(List<dynamic> json){
    if(json!=null){
     todos=new List<Todo>();
     json.forEach((v){
       todos.add(new Todo.fromJson(v));
     });
    }
  }
  Map<String,dynamic> toJson(){
    Map<String,dynamic> data;
    if(this.todos!=null){
      todos.map((f)=>{
        print(f)
      });
      //data["todos"]=this.todos.map((f)=>f.toJson()).toList();
      //print(data["todos"]);
    }
    return data;
  }
}

class Todo{
  String todo;
  String time;
  bool routine;
  Todo({this.todo,this.time,this.routine});
  Todo.fromJson(Map<String,dynamic> json){
    todo=json["todo"];
    time=json["time"];
    routine=json["routine"];
  }
  Map<String,dynamic> toJson(){
    Map<String,dynamic> data;
    data["todo"]=this.todo;
    data["time"]=this.time;
    data["routine"]=this.routine;
    return data;
  }
}