---
title: "[Solution] Java NullPointerException"
description: "Spring Component Injection Null"
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# @Autowired fields are null at runtime due to proxy or lifecycle issues

A `@Autowired` is thrown when public class helper {.

## Common Causes

```java
public class Helper {
    @Autowired private UserService userService;  // null if not a Spring bean
}
```

## Solutions

```java
// Fix: constructor injection
@Service
public class MyService {
    private final UserService repo;
    @Autowired
    public MyService(UserService repo) { this.repo = Objects.requireNonNull(repo); }
}

// Fix: @Lazy for circular deps
@Lazy @Autowired private ServiceB b;

// Fix: @Value with defaults
@Value("${app.timeout:30}") private int timeout;
```

## Prevention Checklist

- Prefer constructor injection.
- Use @Value with defaults.
- Add @PostConstruct validation.
- Never instantiate Spring beans with new.

## Related Errors

[NullPointerException](nullpointerexception), [BeanCreationException](spring-boot-bean-creation)
