---
title: "[Solution] Java BeanCreationException — Spring cannot instantiate or inject a bean due to missing deps or errors"
description: "Fix Java BeanCreationException when spring cannot instantiate or inject a bean due to missing deps or errors with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# BeanCreationException — Spring cannot instantiate or inject a bean due to missing deps or errors

A `BeanCreationException` occurs when @Service
public class UserService {
    @Autowired private UserRepository repo;  // repo bean not defined
}.

## Common Causes

```java
@Service
public class UserService {
    @Autowired private UserRepository repo;  // repo bean not defined
}
```

## Solutions

```java
// Fix: ensure all deps defined
@Repository
public interface UserRepository extends JpaRepository<User,Long> {}

// Fix: ConditionalOnBean
@ConditionalOnBean(name="optionalService")
@Service
public class DependentService {}

// Fix: ObjectProvider
@Autowired private ObjectProvider<OptionalDependency> opt;

// Fix: @Lazy for circular
@Service
public class ServiceA { @Lazy @Autowired private ServiceB b; }
```

## Prevention Checklist

- Ensure all @Autowired deps are beans.
- Use @ConditionalOnBean for optional deps.
- Use @Lazy for circular deps.
- Add @PostConstruct validation.

## Related Errors

NoSuchBeanDefinitionException, CircularDependencyException
