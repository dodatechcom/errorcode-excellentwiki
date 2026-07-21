---
title: "[Solution] Spring AOP Proxy Error -- How to Fix"
description: "Fix Spring AOP proxy errors. Resolve aspect weaving, proxy creation, and AOP configuration issues in Spring."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

A Spring AOP proxy error occurs when Spring cannot create a proxy for a bean due to final classes, self-invocation issues, or misconfigured aspects. AOP (Aspect-Oriented Programming) relies on proxy creation.

## Why It Happens

Spring AOP creates proxies to intercept method calls. Errors occur when the target class is `final` (cannot be proxied), when methods are called internally within the same bean (self-invocation bypasses the proxy), when aspect annotations are incorrect, or when the AOP proxy mode conflicts with CGLIB or JDK dynamic proxies.

## Common Error Messages

```
org.springframework.aop.framework.AopProxyException: CGLIB cannot proxy final classes
```

```
org.springframework.beans.factory.BeanCreationException: Could not generate CGLIB subclass
```

```
java.lang.IllegalStateException: Cannot enhance @Bean method - already overridden
```

```
BeanNotOfRequiredTypeException: Bean named 'x' is expected to be of type 'Proxy'
```

## How to Fix It

### 1. Avoid Final Classes and Methods

Ensure classes and methods can be proxied:

```java
// Wrong: final class cannot be proxied
@Service
public final class UserService {
    public void save(User user) { }
}

// Correct: non-final class
@Service
public class UserService {
    public void save(User user) { }
}

// Wrong: final method cannot be intercepted
@Service
public class UserService {
    public final void save(User user) { }
}
```

### 2. Avoid Self-Invocation

Call methods through the proxy, not directly:

```java
@Service
public class OrderService {

    @Transactional
    public void createOrder(Order order) {
        // Wrong: self-invocation bypasses @Transactional proxy
        validateOrder(order);

        // Correct: call through the injected proxy
        // or restructure the code
    }

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void validateOrder(Order order) {
        // This method needs its own transaction
    }
}

// Solution: inject self-proxy
@Service
public class OrderService {
    @Autowired
    @Lazy
    private OrderService self;  // Injected proxy

    public void createOrder(Order order) {
        self.validateOrder(order);  // Goes through proxy
    }
}
```

### 3. Configure AOP Properly

Set up aspect configuration correctly:

```java
@Aspect
@Component
public class LoggingAspect {

    @Around("execution(* com.example.service.*.*(..))")
    public Object logMethodCall(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        String methodName = joinPoint.getSignature().getName();

        try {
            Object result = joinPoint.proceed();
            long duration = System.currentTimeMillis() - start;
            log.info("{} executed in {}ms", methodName, duration);
            return result;
        } catch (Throwable t) {
            log.error("{} failed: {}", methodName, t.getMessage());
            throw t;
        }
    }
}
```

### 4. Switch Proxy Mode

Use the appropriate proxy mechanism:

```java
@Configuration
@EnableAspectJAutoProxy(proxyTargetClass = true)  // Use CGLIB
public class AopConfig {
}

// Or in application.properties
// spring.aop.proxy-target-class=true
```

## Common Scenarios

**Scenario 1: AOP works on some beans but not others.**
Beans created by `@Bean` methods may not be proxied the same way as component-scanned beans. Ensure the `@Bean` method returns the correct type.

**Scenario 2: Self-invocation causes annotation to be ignored.**
`@Transactional`, `@Cacheable`, and other AOP-based annotations don't work when called from the same class. Extract the annotated method to a separate bean.

**Scenario 3: CGLIB error in tests.**
Add `spring-boot-starter-aop` dependency and ensure CGLIB is available on the classpath.

## Prevent It

1. **Always use constructor injection** to avoid self-invocation issues.

2. **Keep service classes non-final** and their methods non-final.

3. **Use `@EnableAspectJAutoProxy(proxyTargetClass = true)`** for consistent CGLIB proxying.
