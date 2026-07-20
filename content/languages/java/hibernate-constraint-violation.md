---
title: "[Solution] Java ConstraintViolationException — Hibernate database constraint violation"
description: "Fix Java ConstraintViolationException by checking unique constraints, handling duplicates, and verifying data integrity. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 109
---

# ConstraintViolationException — Hibernate database constraint violation

A `ConstraintViolationException` is thrown when a database operation violates a constraint such as a unique key, foreign key, not-null, or check constraint. This typically occurs during inserts or updates when the data conflicts with existing records or schema rules.

## Description

Hibernate wraps database constraint violations into `ConstraintViolationException`. The root cause is a JDBC `SQLIntegrityConstraintViolationException`. Common message variants include:

- `org.hibernate.exception.ConstraintViolationException: could not execute statement`
- `Duplicate entry 'X' for key 'Y'`
- `Column 'X' cannot be null`
- `Duplicate key value violates unique constraint "X"`
- `Foreign key constraint fails`

## Common Causes

```java
// Cause 1: Unique constraint violation
@Entity
@Table(name = "users", uniqueConstraints = @UniqueConstraint(columnNames = "email"))
public class User {
    @Id @GeneratedValue private Long id;
    @Column(nullable = false) private String email;
}

// Inserting duplicate email
User user1 = new User(); user1.setEmail("a@b.com");
User user2 = new User(); user2.setEmail("a@b.com");  // ConstraintViolationException

// Cause 2: Not-null violation
@Entity
public class Product {
    @Column(nullable = false)
    private String name;  // name is null
}

Product p = new Product();
p.setName(null);
productRepository.save(p);  // ConstraintViolationException

// Cause 3: Foreign key violation
@Entity
public class Order {
    @ManyToOne
    @JoinColumn(name = "customer_id", nullable = false)
    private Customer customer;  // customer references non-existent ID
}

// Cause 4: Data too long for column
@Entity
public class Post {
    @Column(length = 50)
    private String title;  // Title is 100 characters
}

Post post = new Post();
post.setTitle("A".repeat(100));
postRepository.save(post);  // ConstraintViolationException
```

## Solutions

### Fix 1: Check existence before inserting

```java
@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Transactional
    public User createUser(CreateUserRequest request) {
        if (userRepository.existsByEmail(request.email())) {
            throw new DuplicateUserException("Email already in use: " + request.email());
        }

        User user = new User();
        user.setName(request.name());
        user.setEmail(request.email());
        return userRepository.save(user);
    }
}
```

### Fix 2: Use @Column constraints properly

```java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(nullable = false)
    private String password;
}

// Validate before save
@Service
public class UserService {
    @Transactional
    public User save(User user) {
        if (user.getName() == null || user.getName().isBlank()) {
            throw new IllegalArgumentException("Name is required");
        }
        if (user.getEmail() == null || user.getEmail().isBlank()) {
            throw new IllegalArgumentException("Email is required");
        }
        return userRepository.save(user);
    }
}
```

### Fix 3: Handle duplicates with UPSERT / ON CONFLICT

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    @Modifying
    @Query(value = "INSERT INTO users (name, email) VALUES (:name, :email) " +
           "ON CONFLICT (email) DO UPDATE SET name = :name", nativeQuery = true)
    int upsertUser(@Param("name") String name, @Param("email") String email);
}

// Or use JPA @SecondaryTable for complex mappings
```

### Fix 4: Catch and handle constraint violations gracefully

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ConstraintViolationException.class)
    public ResponseEntity<ErrorResponse> handleConstraintViolation(
            ConstraintViolationException ex) {
        String message = ex.getSQLException().getMessage();

        if (message.contains("Duplicate entry") || message.contains("unique constraint")) {
            return ResponseEntity.status(HttpStatus.CONFLICT)
                .body(new ErrorResponse("DUPLICATE", "Record already exists"));
        }

        if (message.contains("cannot be null")) {
            return ResponseEntity.badRequest()
                .body(new ErrorResponse("VALIDATION", "Required field is missing"));
        }

        return ResponseEntity.internalServerError()
            .body(new ErrorResponse("CONSTRAINT", "Data integrity violation"));
    }
}
```

### Fix 5: Validate data lengths and formats

```java
@Entity
public class Post {
    @Column(nullable = false, length = 200)
    @Size(min = 1, max = 200)
    private String title;

    @Column(nullable = false, length = 5000)
    @Size(max = 5000)
    private String content;
}

// Use Bean Validation
@Service
public class PostService {
    @Transactional
    public Post createPost(@Valid Post post) {
        // Validation runs before save
        return postRepository.save(post);
    }
}
```

## Prevention Checklist

- Define `@UniqueConstraint` and `@Column(unique = true)` for unique fields
- Validate required fields before saving — never save entities with null required fields
- Check for duplicates with `existsByEmail()` or similar methods before inserting
- Match `@Column(length = N)` with actual database column sizes
- Use `@Valid` with Bean Validation annotations for input validation
- Handle `ConstraintViolationException` in a global exception handler for clean error responses

## Related Errors

- [SQLIntegrityConstraintViolationException](/languages/java/sqlintegrityconstraintviolationexception/)
- [JPA ConstraintViolation](/languages/java/jpa-constraint/)
- [DataTruncation](/languages/java/datatruncation/)
