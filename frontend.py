http: ^1.1.0
flutter_hooks: ^0.20.0
class Todo {
  int? id;
  String title;
  String description;
  bool completed;

  Todo({this.id, required this.title, required this.description, this.completed = false});

  factory Todo.fromJson(Map<String, dynamic> json) => Todo(
        id: json['id'],
        title: json['title'],
        description: json['description'],
        completed: json['completed'],
      );

  Map<String, dynamic> toJson() => {
        "id": id,
        "title": title,
        "description": description,
        "completed": completed,
      };
}
class TodoService {
  final baseUrl = 'http://localhost:8080/api/todos';

  Future<List<Todo>> fetchTodos() async {
    final response = await http.get(Uri.parse(baseUrl));
    return (json.decode(response.body) as List)
        .map((e) => Todo.fromJson(e))
        .toList();
  }

  Future<void> createTodo(Todo todo) async {
    await http.post(Uri.parse(baseUrl),
        headers: {'Content-Type': 'application/json'},
        body: json.encode(todo.toJson()));
  }

  Future<void> updateTodo(Todo todo) async {
    await http.put(Uri.parse('$baseUrl/${todo.id}'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode(todo.toJson()));
  }

  Future<void> deleteTodo(int id) async {
    await http.delete(Uri.parse('$baseUrl/$id'));
  }
}
