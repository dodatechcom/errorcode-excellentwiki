---
title: "[Solution] Spring AOP Pointcut Error"
description: "AOP pointcut not matching."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

AOP pointcut not matching.

## Common Causes

Wrong expression.

## How to Fix

Fix expression.

## Example

```java
@Aspect @Component
public class LoggingAspect {
    @Around("execution(* com.example.service.*.*(..))")
    public Object log(ProceedingJoinPoint jp) throws Throwable {
        return jp.proceed();
    }
}
```
