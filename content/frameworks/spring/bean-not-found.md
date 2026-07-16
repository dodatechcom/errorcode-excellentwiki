---
title: "No qualifying bean of type 'X'"
description: "Spring throws this exception when it cannot find a bean matching the requested type during dependency injection."
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["dependency-injection", "beans", "spring-context"]
weight: 5
---

This error occurs when Spring's application context cannot locate a bean that matches the type required for injection. It typically surfaces at startup when a `@Autowired`, `@Inject`, or constructor injection target has no matching bean definition.

## Common Causes

- The class is not annotated with `@Component`, `@Service`, `@Repository`, or `@Configuration`
- The class is in a package not covered by `@ComponentScan`
- Multiple beans of the same type exist and no `@Primary` or `@Qualifier` is specified
- The bean is conditionally created (`@ConditionalOnProperty`) and the condition is not met

## How to Fix

Ensure the class is properly annotated and within the component scan path:

```java
@Service
public class PaymentService {
    // Spring will find this bean
}
```

If you have multiple implementations, qualify the injection:

```java
@Autowired
@Qualifier("stripePaymentService")
private PaymentService paymentService;
```

Expand your component scan if the bean is in a sub-package:

```java
@SpringBootApplication(scanClasses = {AppConfig.class, com.other.package.ModuleConfig.class})
public class Application { }
```

## Example

```java
@RestController
public class UserController {

    @Autowired
    private UserService userService; // UserService has no @Service annotation
}
```

```text
NoSuchBeanDefinitionException: No qualifying bean of type 'com.example.UserService' available
```

## Related Errors

- [No mapping found for HTTP request]({{< relref "/frameworks/spring/mapping-error" >}})
