---
title: "[Solution] Java BeanCreationException — Spring cannot create or initialize a bean"
description: "Fix Java BeanCreationException by checking constructors, verifying dependencies, and handling circular references. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 101
---

# BeanCreationException — Spring cannot create or initialize a bean

A `BeanCreationException` is thrown when the Spring IoC container fails to instantiate, configure, or inject a bean. This commonly occurs due to missing dependencies, constructor errors, or circular references between beans.

## Description

Spring manages bean lifecycle through the application context. When a bean cannot be created, the container throws `BeanCreationException` with details about the failure. Common message variants include:

- `Error creating bean with name 'X': Unsatisfied dependency expressed through field 'Y'`
- `Error creating bean with name 'X': Requested bean is a singleton in circular reference`
- `BeanCreationException: No default constructor found`
- `Error creating bean with name 'X': Invocation of init method failed`

## Common Causes

```java
// Cause 1: Missing default constructor
@Service
public class UserService {
    private final UserRepository repo;
    // No constructor, no @Autowired — Spring cannot instantiate
}

// Cause 2: Dependency not found in context
@Service
public class OrderService {
    @Autowired private PaymentGateway gateway;  // No bean of this type
}

// Cause 3: Circular dependency with constructor injection
@Service
public class ServiceA {
    private final ServiceB b;
    public ServiceA(ServiceB b) { this.b = b; }
}
@Service
public class ServiceB {
    private final ServiceA a;
    public ServiceB(ServiceA a) { this.a = a; }
}

// Cause 4: Bean initialization method fails
@Component
public class CacheManager {
    @PostConstruct
    public void init() {
        throw new RuntimeException("Cannot connect to cache server");
    }
}

// Cause 5: Multiple beans of same type without qualifier
public interface Notifier {}
@Service public class EmailNotifier implements Notifier {}
@Service public class SmsNotifier implements Notifier {}

@Service
public class AlertService {
    @Autowired private Notifier notifier;  // Ambiguous — two candidates
}
```

## Solutions

### Fix 1: Provide proper constructors

```java
@Service
public class UserService {
    private final UserRepository repo;

    @Autowired
    public UserService(UserRepository repo) {
        this.repo = repo;
    }
}

// Single constructor — @Autowired is optional in Spring 4.3+
@Service
public class UserService {
    private final UserRepository repo;

    public UserService(UserRepository repo) {
        this.repo = repo;
    }
}
```

### Fix 2: Verify all dependencies are beans

```java
// Ensure the dependency is registered as a bean
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
}

// For conditional dependencies
@Service
@ConditionalOnBean(name = "paymentGateway")
public class OrderService {
    @Autowired private PaymentGateway gateway;
}

// For optional dependencies
@Service
public class OrderService {
    private final ObjectProvider<PaymentGateway> gatewayProvider;

    public OrderService(ObjectProvider<PaymentGateway> gatewayProvider) {
        this.gatewayProvider = gatewayProvider;
    }

    public void process() {
        PaymentGateway gw = gatewayProvider.getIfAvailable();
        if (gw != null) { gw.charge(); }
    }
}
```

### Fix 3: Handle circular references with @Lazy

```java
@Service
public class ServiceA {
    private final ServiceB b;

    public ServiceA(@Lazy ServiceB b) {
        this.b = b;
    }
}

// Or break the cycle by extracting shared logic
@Service
public class SharedLogicService {
    public void doWork() {
        // Shared logic extracted from the circular pair
    }
}
```

### Fix 4: Ensure init methods do not fail

```java
@Component
public class CacheManager {
    @PostConstruct
    public void init() {
        try {
            connectToCache();
        } catch (Exception e) {
            // Log and degrade gracefully instead of failing bean creation
            log.warn("Cache unavailable, using in-memory fallback", e);
            this.delegate = new InMemoryCache();
        }
    }
}
```

### Fix 5: Resolve ambiguity with @Qualifier

```java
@Service
public class AlertService {
    private final Notifier notifier;

    public AlertService(@Qualifier("emailNotifier") Notifier notifier) {
        this.notifier = notifier;
    }
}

// Or use @Primary on the default implementation
@Service @Primary
public class EmailNotifier implements Notifier {}
```

## Prevention Checklist

- Ensure all injectable dependencies are registered as beans in the context
- Use constructor injection and provide a single constructor when possible
- Use `@Lazy` to break constructor-injection circular references
- Validate `@PostConstruct` methods handle failures gracefully
- Use `@Qualifier` or `@Primary` when multiple beans of the same type exist
- Run `spring-boot-starter-actuator` health checks at startup to catch issues early

## Related Errors

- [NoSuchBeanDefinitionException](/languages/java/spring-no-bean-found/)
- [CircularDependencyException](/languages/java/spring-circular-dependency/)
- [IllegalStateException](/languages/java/illegalstateexception/)
