---
title: "NoSuchBeanDefinitionException - bean not found"
description: "Spring throws NoSuchBeanDefinitionException when no bean matching the requested type is available in the application context"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["bean", "dependency-injection", "autowired", "component-scan", "spring-context"]
weight: 5
---

This error occurs when Spring's application context cannot find a bean matching the type required for dependency injection. It typically surfaces at startup when `@Autowired` or constructor injection targets have no matching bean definition.

## Common Causes

- Class is not annotated with `@Component`, `@Service`, `@Repository`, or `@Configuration`
- Bean is in a package not covered by `@ComponentScan`
- Multiple beans of the same type exist without `@Primary` or `@Qualifier`
- Bean is conditionally created via `@ConditionalOnProperty` and the condition is not met
- Interface has no concrete implementation registered as a bean

## How to Fix

1. Annotate the class properly:

```java
@Service
public class OrderService {
    // Spring will find this bean
}
```

2. Qualify injection when multiple beans exist:

```java
@Autowired
@Qualifier("stripePaymentService")
private PaymentService paymentService;
```

3. Expand component scan if the bean is in a sub-package:

```java
@SpringBootApplication(scanClasses = {
    AppConfig.class,
    com.other.package.ModuleConfig.class
})
public class Application { }
```

4. Use `@Primary` to mark the default bean:

```java
@Service
@Primary
public class DefaultPaymentService implements PaymentService { }
```

## Examples

```java
@RestController
public class UserController {
    @Autowired
    private UserService userService; // No @Service annotation
}
// NoSuchBeanDefinitionException: No qualifying bean of type 'com.example.UserService'
```

## Related Errors

- [Validation error]({{< relref "/frameworks/spring/validation-error" >}})
- [AOP error]({{< relref "/frameworks/spring/aop-error" >}})
