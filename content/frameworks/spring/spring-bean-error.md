---
title: "[Solution] Spring Bean Creation or Injection Failed Error — How to Fix"
description: "Fix Spring bean creation errors. Resolve bean injection failures, circular dependencies, and Spring context issues."
frameworks: ["spring"]
error-types: ["configuration-error"]
severities: ["error"]
weight: 5
comments: true
---

A Spring bean creation or injection failed error occurs when the Spring IoC container cannot instantiate, configure, or inject a bean. This is one of the most common Spring errors and can have many root causes.

## Why It Happens

Spring manages beans through dependency injection. Errors occur when a bean depends on a missing bean, when there is a circular dependency, when a constructor or setter has incorrect annotations, when component scanning misses a package, or when configuration properties are missing.

## Common Error Messages

```
NoUniqueBeanDefinitionException: No qualifying bean of type 'UserService' available
```

```
NoSuchBeanDefinitionException: No bean named 'userRepository' available
```

```
BeanCreationException: Could not autowire field: private UserRepository
```

```
Circular dependency detected: beanA → beanB → beanA
```

## How to Fix It

### 1. Use Correct Injection Annotations

Choose the right injection method:

```java
@Service
public class UserService {

    // Field injection (not recommended for testing)
    @Autowired
    private UserRepository userRepository;

    // Constructor injection (recommended)
    private final UserRepository userRepository;
    private final EmailService emailService;

    public UserService(UserRepository userRepository, EmailService emailService) {
        this.userRepository = userRepository;
        this.emailService = emailService;
    }

    // Setter injection (optional dependencies)
    private AuditService auditService;

    @Autowired
    public void setAuditService(AuditService auditService) {
        this.auditService = auditService;
    }
}
```

### 2. Resolve Circular Dependencies

Break circular dependency chains:

```java
// Problem: A depends on B, B depends on A
@Service
public class ServiceA {
    @Autowired
    private ServiceB serviceB;
}

@Service
public class ServiceB {
    @Autowired
    private ServiceA serviceA;  // Circular!
}

// Solution: Extract shared logic to a third service
@Service
public class SharedService {
    // Common logic here
}

@Service
public class ServiceA {
    private final SharedService sharedService;
    public ServiceA(SharedService sharedService) {
        this.sharedService = sharedService;
    }
}

@Service
public class ServiceB {
    private final SharedService sharedService;
    public ServiceB(SharedService sharedService) {
        this.sharedService = sharedService;
    }
}
```

### 3. Specify Bean Qualifiers

When multiple beans of the same type exist:

```java
@Repository
public class MySqlUserRepository implements UserRepository { }

@Repository
public class MongoUserRepository implements UserRepository { }

@Service
public class UserService {
    private final UserRepository userRepository;

    // Use @Qualifier to specify which bean
    public UserService(@Qualifier("mySqlUserRepository") UserRepository userRepository) {
        this.userRepository = userRepository;
    }
}
```

### 4. Ensure Component Scanning Covers All Packages

Verify your main application class scans the right packages:

```java
@SpringBootApplication(scanBasePackages = "com.example")
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

## Common Scenarios

**Scenario 1: Bean works in dev but fails in test.**
Test context may not load the same beans. Use `@MockBean` or `@ActiveProfiles("test")` to configure test-specific beans.

**Scenario 2: Circular dependency after adding a new field.**
Adding `@Autowired` to a new field can create a circular dependency that didn't exist before. Review the dependency graph.

**Scenario 3: Bean not found after package rename.**
Component scanning is based on the base package. After renaming packages, update `scanBasePackages` or `@ComponentScan`.

## Prevent It

1. **Prefer constructor injection** over field injection. It makes dependencies explicit and enables easier testing.

2. **Use `@Primary` or `@Qualifier`** when multiple beans of the same type exist.

3. **Enable debug logging** with `logging.level.org.springframework=DEBUG` to trace bean creation.
