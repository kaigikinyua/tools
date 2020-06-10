class TodoListModel{
  List<Todo> todos;
  TodoListModel(this.todos);
  TodoListModel.fromJson(Map<String,dynamic> json){
    if(json["todos"]!=null){
     todos=new List<Todo>();
     json["todos"].forEach((v){
       todos.add(new Todo.fromJson(v));
     });
    }
  }
}

class Todo{
  String todo;
  String time;
  bool routine;
  Todo(this.todo,this.time,this.routine);
  Todo.fromJson(Map<String,dynamic> json){
    todo=json["todo"];
    time=json["time"];
    routine=json["routine"];
  }
}