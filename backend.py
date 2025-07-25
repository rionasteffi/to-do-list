@Entity
public class Todo {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String title;
    private String description;
    private boolean completed;
}@Repository
public interface TodoRepository extends JpaRepository<Todo, Long> {}
@Service
public class TodoService {
    @Autowired
    private TodoRepository repo;

    public List<Todo> getAll() { return repo.findAll(); }
    public Todo get(Long id) { return repo.findById(id).orElseThrow(); }
    public Todo save(Todo todo) { return repo.save(todo); }
    public void delete(Long id) { repo.deleteById(id); }
}
@RestController
@RequestMapping("/api/todos")
@CrossOrigin(origins = "*")
public class TodoController {
    @Autowired
    private TodoService service;

    @GetMapping
    public List<Todo> getAll() { return service.getAll(); }

    @PostMapping
    public Todo create(@RequestBody Todo todo) { return service.save(todo); }

    @PutMapping("/{id}")
    public Todo update(@PathVariable Long id, @RequestBody Todo todo) {
        Todo existing = service.get(id);
        existing.setTitle(todo.getTitle());
        existing.setDescription(todo.getDescription());
        existing.setCompleted(todo.isCompleted());
        return service.save(existing);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Long id) { service.delete(id); }
}
spring.datasource.url=jdbc:mysql://localhost:3306/todo_db
spring.datasource.username=root
spring.datasource.password=yourpassword
spring.jpa.hibernate.ddl-auto=update













