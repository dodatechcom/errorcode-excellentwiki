---
title: "BeanCreationException in AOP proxy"
description: "Spring throws BeanCreationException when an AOP proxy cannot be created for a bean"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring fails to create an AOP proxy for a bean, typically due to circular dependencies, missing aspect definitions, or incompatible proxy modes.

## Common Causes

- Circular dependency involving proxied beans
- `@Aspect` class has injection issues
- Final methods cannot be proxied (CGLIB limitation)
- Proxy mode mismatch (JDK vs CGLIB)
- Bean initialization fails before proxy is created

## How to Fix

1. Enable CGLIB proxying if using final methods:

```java
@EnableAspectJAutoProxy(proxyTargetClass = true)
@Configuration
public class AopConfig { }
```

2. Break circular dependencies:

```java
@Service
public class OrderService {
    private final Lazy<OrderValidator> validator;

    public OrderService(Lazy<OrderValidator> validator) {
        this.validator = validator; // Breaks the circular dependency
    }
}
```

3. Verify aspect configuration:

```java
@Aspect
@Component
public class LoggingAspect {

    @Around("execution(* com.example.service.*.*(..))")
    public Object logMethodCall(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object result = joinPoint.proceed();
        long duration = System.currentTimeMillis() - start;
        log.info("Method {} took {}ms", joinPoint.getSignature(), duration);
        return result;
    }
}
```

## Examples

```java
@Service
public class ServiceA {
    @Autowired private ServiceB b;
}
@Service
public class ServiceB {
    @Autowired private ServiceA a;
}
// BeanCreationException: Requested bean could not be created — circular reference
```

## Related Errors

- [Bean not found]({{< relref "/frameworks/spring/spring-bean-not-found" >}})
- [Validation error]({{< relref "/frameworks/spring/spring-validation-error" >}})
