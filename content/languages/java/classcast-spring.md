---
title: "[Solution] Java ClassCastException — retrieving beans by type where actual type doesn't match due to proxies"
description: "Fix Java ClassCastException when retrieving beans by type where actual type doesn't match due to proxies with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassCastException — retrieving beans by type where actual type doesn't match due to proxies

A `ClassCastException` occurs when UserService proxy = context.getBean(UserServiceImpl.class);
// CGLIB proxy may not cast to impl.

## Common Causes

```java
UserService proxy = context.getBean(UserServiceImpl.class);
// CGLIB proxy may not cast to impl
```

## Solutions

```java
// Fix: inject by interface
@Autowired private MyInterface service;

// Fix: ObjectProvider
@Autowired private ObjectProvider<UserService> sp;

// Fix: context.getBean with type
UserService s = context.getBean("userService", UserService.class);
```

## Prevention Checklist

- Inject by interface, not implementation.
- Use @Lazy for circular deps.
- Use @Primary/@Qualifier to disambiguate.

## Related Errors

ClassCastException, BeanCreationException
