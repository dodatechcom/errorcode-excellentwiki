---
title: "[Solution] Java CircularDependencyException — two beans depend on each other creating circular dependency"
description: "Fix Java CircularDependencyException when two beans depend on each other creating circular dependency with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# CircularDependencyException — two beans depend on each other creating circular dependency

A `CircularDependencyException` occurs when @Service public class ServiceA { @Autowired private ServiceB b; }
@Service public class ServiceB { @Autowired private ServiceA a; }.

## Common Causes

```java
@Service public class ServiceA { @Autowired private ServiceB b; }
@Service public class ServiceB { @Autowired private ServiceA a; }
```

## Solutions

```java
// Fix: @Lazy
@Service
public class ServiceA { @Lazy @Autowired private ServiceB b; }

// Fix: setter injection
@Service
public class ServiceA {
    private ServiceB b;
    @Autowired public void setB(ServiceB b) { this.b = b; }
}

// Fix: ApplicationContext.getBean()
@Service
public class ServiceA {
    @Autowired private ApplicationContext ctx;
    public void work() { ServiceB b = ctx.getBean(ServiceB.class); }
}

// Fix: extract shared logic to third service
```

## Prevention Checklist

- Use @Lazy to break cycles.
- Prefer constructor but use setter to break.
- Refactor shared logic to third service.
- Use allow-circular-references as last resort.

## Related Errors

BeanCreationException, IllegalStateException
