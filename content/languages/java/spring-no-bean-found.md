---
title: "[Solution] Java NoSuchBeanDefinitionException — Spring cannot find a bean of the required type"
description: "Fix Java NoSuchBeanDefinitionException by checking @Component annotations, verifying @Autowired usage, and using @Qualifier. Copy-paste solutions with code examples."
languages: ["java"]
severities: ["error"]
error-types: ["runtime"]
weight: 102
---

# NoSuchBeanDefinitionException — Spring cannot find a bean of the required type

A `NoSuchBeanDefinitionException` is thrown when Spring cannot locate a bean that matches the requested type or name. This occurs when a class is not registered as a bean or when `@Autowired` targets a type with no matching definition.

## Description

Spring resolves dependencies by type during component scanning and autowiring. When the container cannot find a matching bean, it throws `NoSuchBeanDefinitionException`. Common message variants include:

- `No qualifying bean of type 'com.example.UserService' available`
- `No qualifying bean of type 'com.example.UserRepository' available: expected at least 1 bean which qualifies as autowire candidate`
- `No bean named 'customRepo' available`
- `Unsatisfied dependency expressed through field 'userRepo'; nested exception is NoSuchBeanDefinitionException`

## Common Causes

```java
// Cause 1: Class not annotated as a bean
public class UserService {  // Missing @Service or @Component
    public void process() {}
}

// Cause 2: Component scan misses the package
// Main app in com.example.app, service in com.other.service
@ComponentScan("com.example.app")  // Does not scan com.other.service
@SpringBootApplication
public class Application {}

// Cause 3: Interface with no concrete bean
public interface PaymentProcessor {}
// No @Service or @Bean for any implementation

// Cause 4: Wrong type in @Autowired
@Service
public class OrderService {
    @Autowired private UserServiceImpl impl;  // Should be UserService interface
}

// Cause 5: Multiple candidates with no disambiguation
@Service public class EmailNotifier implements Notifier {}
@Service public class SmsNotifier implements Notifier {}

@Service
public class AlertService {
    @Autowired private Notifier notifier;  // Two candidates, no @Primary
}
```

## Solutions

### Fix 1: Annotate the class as a bean

```java
@Service
public class UserService {
    // Spring will detect and register this bean
}

// Or use @Component for general classes
@Component
public class CacheHelper {}

// Or register manually in configuration
@Configuration
public class AppConfig {
    @Bean
    public UserService userService() {
        return new UserService();
    }
}
```

### Fix 2: Fix component scan paths

```java
// Scan all packages that contain beans
@SpringBootApplication(scanBasePackages = {"com.example", "com.other"})
public class Application {}

// Or restructure your packages to fall under the base package
// com.example.app (main)
// com.example.service (beans)
// com.example.repository (beans)
```

### Fix 3: Use @Qualifier to disambiguate

```java
@Service
public class AlertService {
    private final Notifier notifier;

    public AlertService(@Qualifier("emailNotifier") Notifier notifier) {
        this.notifier = notifier;
    }
}

// Or use @Primary on the default implementation
@Service @Primary
public class EmailNotifier implements Notifier {}
```

### Fix 4: Use ObjectProvider for optional beans

```java
@Service
public class ReportService {
    private final ObjectProvider<PdfExporter> pdfExporter;

    public ReportService(ObjectProvider<PdfExporter> pdfExporter) {
        this.pdfExporter = pdfExporter;
    }

    public void export() {
        PdfExporter exporter = pdfExporter.getIfAvailable();
        if (exporter != null) {
            exporter.export();
        } else {
            // Use CSV fallback
        }
    }
}
```

### Fix 5: Implement all required interfaces

```java
public interface PaymentProcessor {
    void process(double amount);
}

@Service
public class StripePaymentProcessor implements PaymentProcessor {
    @Override
    public void process(double amount) {
        // Stripe implementation
    }
}
```

## Prevention Checklist

- Verify all injectable classes carry `@Component`, `@Service`, `@Repository`, or `@Bean`
- Ensure component scan packages include all bean locations
- Use `@Primary` or `@Qualifier` when multiple beans implement the same interface
- Use `ObjectProvider` or `@ConditionalOnMissingBean` for optional dependencies
- Check that interfaces have at least one concrete implementation registered as a bean
- Run application with `--debug` flag to see auto-configuration and bean registration details

## Related Errors

- [BeanCreationException](/languages/java/spring-bean-creation-failed/)
- [UnsatisfiedDependencyException](/languages/java/spring-bean-creation/)
- [IllegalArgumentException](/languages/java/illegalargumentexception/)
