---
title: "[Solution] NoSuchBeanDefinitionException — Spring Bean Not Found Fix"
description: "Fix Spring NoSuchBeanDefinitionException when a bean is not found in the application context. Check @Component scanning, @Qualifier, and configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# NoSuchBeanDefinitionException — Spring Bean Not Found Fix

A `NoSuchBeanDefinitionException` is thrown when Spring cannot find a bean definition that matches the requested type or name. This typically occurs during dependency injection when `@Autowired` or `ApplicationContext.getBean()` requests a bean that does not exist in the container.

## What This Error Means

The exception fires during the wiring phase of the Spring application context. Common message formats:

- `No qualifying bean of type 'com.example.MyService' available`
- `No bean named 'myBean' available`
- `No qualifying bean of type 'com.example.MyService' available: expected at least 1 bean which qualifies as autowire candidate`

## Common Causes

```java
// Cause 1: Component not scanned
@Service
public class MyService { }

@Autowired
private MyService myService;  // NoSuchBeanDefinitionException if not in scan path

// Cause 2: Missing @Component annotation
public class MyService { }  // No annotation — Spring doesn't manage this class

// Cause 3: Multiple beans without @Qualifier
@Service("serviceA")
public class MyServiceA implements MyInterface { }

@Service("serviceB")
public class MyServiceB implements MyInterface { }

@Autowired
private MyInterface myInterface;  // Ambiguous — which one?

// Cause 4: Bean created conditionally
@ConditionalOnProperty(name = "feature.enabled", havingValue = "true")
@Service
public class FeatureService { }

// Cause 5: Profile not active
@Profile("prod")
@Service
public class ProdService { }
```

## How to Fix

### Fix 1: Ensure component scanning covers the package

```java
@SpringBootApplication(scanBasePackages = "com.example")
public class Application { }
```

### Fix 2: Add the missing annotation

```java
@Service
public class MyService { }
```

### Fix 3: Use @Qualifier when multiple beans exist

```java
@Autowired
@Qualifier("serviceA")
private MyInterface myInterface;
```

### Fix 4: Use @Primary for the default bean

```java
@Service
@Primary
public class MyServiceA implements MyInterface { }
```

### Fix 5: Check active profiles

```bash
export SPRING_PROFILES_ACTIVE=prod
# or
spring.profiles.active=prod
```

## Related Errors

- {{< relref "spring-security" >}} — AccessDeniedException in Spring Security
- {{< relref "spring-validation" >}} — MethodArgumentNotValidException
- {{< relref "spring-aop" >}} — BeanCreationException in AOP context
