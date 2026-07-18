---
title: "[Solution] Spring Data Repository Error — How to Fix"
description: "Fix Spring Data repository errors. Resolve repository bean creation, query derivation, and JPA issues."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Spring Data repository error occurs when the repository interface cannot be created, when derived queries fail, or when JPA/Hibernate configuration issues prevent data access. Spring Data relies on correct interface definitions and entity mappings.

## Why It Happens

Spring Data generates repository implementations at runtime. Errors occur when entity classes are missing `@Entity`, when repository interfaces don't extend the correct base interface, when query method names don't follow naming conventions, when the database schema doesn't match entity definitions, or when transactions are not properly configured.

## Common Error Messages

```
Failed to create query for method: No property 'name' found for type 'User'
```

```
IllegalStateException: Failed to instantiate: No default constructor found
```

```
PersistenceException: Unable to build Hibernate SessionFactory
```

```
IncorrectResultSizeDataAccessException: query returned more than one row
```

## How to Fix It

### 1. Define Entities Correctly

Ensure entities have proper annotations:

```java
@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(nullable = false)
    private String name;

    @OneToMany(mappedBy = "author", cascade = CascadeType.ALL)
    private List<Post> posts;

    // Default constructor (required by JPA)
    public User() {}

    public User(String email, String name) {
        this.email = email;
        this.name = name;
    }

    // Getters and setters
}
```

### 2. Create Repository Interfaces

Extend the correct base repository:

```java
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    // Derived queries
    Optional<User> findByEmail(String email);
    List<User> findByNameContainingIgnoreCase(String name);
    List<User> findByEmailAndName(String email, String name);
    boolean existsByEmail(String email);

    // Custom queries with @Query
    @Query("SELECT u FROM User u WHERE u.email LIKE %:domain")
    List<User> findByEmailDomain(@Param("domain") String domain);

    // Native queries
    @Query(value = "SELECT * FROM users WHERE created_at > :date", nativeQuery = true)
    List<User> findRecentUsers(@Param("date") LocalDateTime date);

    // Projections
    @Query("SELECT u.email as email, u.name as name FROM User u")
    List<UserProjection> findAllProjections();
}
```

### 3. Handle Repository Method Errors

Catch and handle common exceptions:

```java
@Service
public class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User findByEmailOrThrow(String email) {
        return userRepository.findByEmail(email)
            .orElseThrow(() -> new ResourceNotFoundException("User not found: " + email));
    }

    @Transactional
    public User createUser(User user) {
        if (userRepository.existsByEmail(user.getEmail())) {
            throw new DuplicateResourceException("Email already exists: " + user.getEmail());
        }
        return userRepository.save(user);
    }

    public List<User> searchUsers(String query) {
        // Use Specification for complex queries
        Specification<User> spec = Specification
            .where(UserSpecs.emailContains(query))
            .or(UserSpecs.nameContains(query));
        return userRepository.findAll(spec);
    }
}
```

### 4. Configure JPA Properties

Set database-specific properties:

```yaml
# application.yml
spring:
  jpa:
    hibernate:
      ddl-auto: validate  # Use 'validate' in production
    show-sql: true
    properties:
      hibernate:
        format_sql: true
        dialect: org.hibernate.dialect.PostgreSQLDialect
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: user
    password: pass
```

## Common Scenarios

**Scenario 1: Derived query method not found.**
Check that the property name matches the entity field name exactly. `findByEmail` requires a `email` field in the entity.

**Scenario 2: Repository returns wrong results.**
Verify the query method name or `@Query` annotation. Use `@Query` for complex queries instead of relying on derived query names.

**Scenario 3: LazyInitializationException in service.**
Entity collections marked as `FetchType.LAZY` are not loaded outside the transaction. Use `@Transactional(readOnly = true)` or `JOIN FETCH` in the query.

## Prevent It

1. **Always define a no-arg constructor** in entity classes (JPA requirement).

2. **Use `ddl-auto: validate`** in production to ensure schema matches entities.

3. **Test repository methods with `@DataJpaTest`** for fast, isolated database tests.
