---
title: "[Solution] Java ClassCastException — Hibernate proxy cannot be cast to entity subclass"
description: "Fix Java ClassCastException when hibernate proxy cannot be cast to entity subclass with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassCastException — Hibernate proxy cannot be cast to entity subclass

A `ClassCastException` occurs when Animal a = em.find(Animal.class, 1L);
Dog d = (Dog) a;  // ClassCastException — HibernateProxy.

## Common Causes

```java
Animal a = em.find(Animal.class, 1L);
Dog d = (Dog) a;  // ClassCastException — HibernateProxy
```

## Solutions

```java
// Fix: unwrap
Dog d = em.find(Animal.class,1L).unwrap(Dog.class);

// Fix: Hibernate.initialize
Hibernate.initialize(a);
if (a instanceof Dog d) { /* ... */ }

// Fix: @Proxy(lazy=false)
@Entity @Proxy(lazy=false)
public class Animal {}
```

## Prevention Checklist

- Use EntityManager.unwrap() for safe extraction.
- Call Hibernate.initialize() before accessing lazy proxies.
- Use @Proxy(lazy=false) to disable proxying.

## Related Errors

ClassCastException, LazyInitializationException
