---
title: "Spring AMQP message conversion error"
description: "Spring AMQP fails to convert incoming RabbitMQ message body to the expected Java type during listener invocation"
frameworks: ['spring']
error-types: ['runtime-error']
severities: ["error"]
weight: 5
---

This error occurs when spring amqp fails to convert incoming rabbitmq message body to the expected java type during listener invocation.

## Common Causes

- Incorrect dependency injection wiring or missing bean definitions
- Framework version incompatibility with Spring Boot auto-configuration
- Missing required annotations on service or configuration classes
- Environment-specific configuration not loaded properly
- Transaction boundaries not aligned with persistence operations
- Serialization or deserialization failures during message processing

## How to Fix

1. Verify your Spring configuration and bean wiring:

```java
@Configuration
public class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}
```

2. Check for missing annotations:

```java
@Service
@Transactional
public class UserService {
    @Autowired
    private UserRepository userRepository;

    public User findById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
    }
}
```

3. Ensure proper exception handling:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        return ResponseEntity.status(HttpStatus.NOT_FOUND)
            .body(new ErrorResponse(ex.getMessage()));
    }
}
```

## Examples

```java
// Common mistake: calling transactional method from same class
@Service
public class OrderService {
    public void processOrder(Order order) {
        // This bypasses the proxy -- transaction won't apply
        this.saveOrder(order);
    }

    @Transactional
    public void saveOrder(Order order) {
        orderRepository.save(order);
    }
}
```

```text
org.springframework.transaction.TransactionSystemException: Could not commit JPA transaction
    at org.springframework.orm.jpa.JpaTransactionManager.commit(JpaTransactionManager.java:332)
```

## Prevention

1. Use constructor injection instead of field injection for better testability
2. Keep transactional methods in separate beans to avoid proxy bypass issues
3. Enable Spring Boot debug logging to trace bean creation and wiring
4. Write integration tests that exercise the full request lifecycle
