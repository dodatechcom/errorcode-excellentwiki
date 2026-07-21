---
title: "[Solution] Spring R2DBC Error"
description: "Fix Spring R2DBC errors when reactive database connections fail or queries timeout."
frameworks: ["spring"]
error-types: ["database-error"]
severities: ["error"]
---

R2DBC errors occur when the reactive database connection cannot be established, queries fail, or connection pooling is misconfigured.

## Common Causes

- R2DBC driver not in classpath
- Connection URL incorrect
- Pool size too small for reactive workload
- Query timeout too short
- Transaction not properly managed in reactive context

## How to Fix

### Configure R2DBC

```yaml
# application.yml
spring:
  r2dbc:
    url: r2dbc:postgresql://localhost:5432/mydb
    username: postgres
    password: secret
    pool:
      initial-size: 5
      max-size: 20
      max-idle-time: 30m
```

### Create Reactive Repository

```java
@Repository
public interface UserRepository extends ReactiveCrudRepository<User, Long> {
    Mono<User> findByUsername(String username);
    Flux<User> findByActiveTrue();
}
```

### Use R2DBC Entity Template

```java
@Service
public class UserService {
    private final R2dbcEntityTemplate template;

    public UserService(R2dbcEntityTemplate template) {
        this.template = template;
    }

    public Mono<User> findByUsername(String username) {
        return template.select(User.class)
            .matching(Criteria.where("username").is(username))
            .one();
    }
}
```

### Handle Connection Errors

```java
@Service
public class UserService {
    private final UserRepository userRepository;

    public Mono<User> getUserSafe(Long id) {
        return userRepository.findById(id)
            .onErrorResume(e -> {
                log.error("Database error: {}", e.getMessage());
                return Mono.empty();
            });
    }
}
```

## Examples

```yaml
# Bug -- wrong R2DBC URL
spring:
  r2dbc:
    url: postgresql://localhost:5432/mydb  # Missing r2dbc: prefix

# Fix -- correct URL
spring:
  r2dbc:
    url: r2dbc:postgresql://localhost:5432/mydb
```
