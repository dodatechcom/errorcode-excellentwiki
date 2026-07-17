---
title: "[Solution] BeanCreationException in AOP — Spring AOP Fix"
description: "Fix BeanCreationException when Spring AOP proxy creation fails. Resolve circular dependencies and advisor configuration issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["spring", "aop", "aspectj", "proxy", "bean-creation"]
weight: 5
---

# BeanCreationException in AOP — Spring AOP Fix

A `BeanCreationException` in AOP context occurs when Spring cannot create a proxy for a bean. This is often caused by circular dependencies, missing AspectJ configuration, or internal method calls bypassing the proxy.

## What This Error Means

Common messages:

- `BeanCreationException: Error creating bean with name 'myService'`
- `BeanCurrentlyInCreationException: Requested bean is currently in creation`

## Common Causes

```java
// Cause 1: Circular dependency
@Service
public class ServiceA {
    @Autowired
    private ServiceB serviceB;
}

@Service
public class ServiceB {
    @Autowired
    private ServiceA serviceA;  // Circular dependency
}

// Cause 2: Self-invocation bypasses proxy
@Service
public class MyService {

    @Transactional
    public void outerMethod() {
        innerMethod();  // Bypasses AOP proxy — no transaction!
    }

    @Transactional
    public void innerMethod() { }
}
```

## How to Fix

### Fix 1: Use @Lazy to break circular dependency

```java
@Service
public class ServiceA {
    @Lazy
    @Autowired
    private ServiceB serviceB;
}
```

### Fix 2: Inject self via ApplicationContext

```java
@Service
public class MyService implements ApplicationContextAware {
    private ApplicationContext context;

    @Transactional
    public void outerMethod() {
        context.getBean(MyService.class).innerMethod();
    }

    @Transactional
    public void innerMethod() { }

    @Override
    public void setApplicationContext(ApplicationContext ctx) {
        this.context = ctx;
    }
}
```

### Fix 3: Use aspectj-weaving instead of Spring proxy

```properties
spring.aop.proxy-target-class=false
```

## Related Errors

- {{< relref "spring-bean" >}} — NoSuchBeanDefinitionException
- {{< relref "spring-security" >}} — AccessDeniedException
- {{< relref "spring-webflux" >}} — WebExchangeBindException
