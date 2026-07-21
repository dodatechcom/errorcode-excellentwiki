---
title: "[Solution] Spring Context Annotation Error"
description: "Fix Spring context annotation errors when @Autowired, @Component, or @Bean annotations fail to inject dependencies."
frameworks: ["spring"]
error-types: ["configuration-error"]
severities: ["error"]
---

Context annotation errors occur when Spring cannot inject dependencies because beans are not properly annotated or the component scan path is wrong.

## Common Causes

- `@ComponentScan` not covering the package
- Bean not annotated with `@Component`, `@Service`, or `@Repository`
- Multiple beans of same type without `@Primary` or `@Qualifier`
- Circular dependency in constructor injection
- AOP proxy required but not created

## How to Fix

### Configure Component Scan

```java
@SpringBootApplication(scanBasePackages = "com.example")
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### Use Correct Annotations

```java
@Component  // Generic component
@Service    // Service layer
@Repository // Data access layer
@Controller // Web controller
@RestController // REST controller
```

### Use @Qualifier for Multiple Beans

```java
@Service
public class NotificationService {
    private final EmailSender emailSender;
    private final SmsSender smsSender;

    public NotificationService(
            @Qualifier("emailSender") EmailSender emailSender,
            @Qualifier("smsSender") SmsSender smsSender) {
        this.emailSender = emailSender;
        this.smsSender = smsSender;
    }
}
```

### Mark Primary Bean

```java
@Bean
@Primary
public DataSource primaryDataSource() {
    return new HikariDataSource(primaryConfig());
}

@Bean
public DataSource secondaryDataSource() {
    return new HikariDataSource(secondaryConfig());
}
```

## Examples

```java
// Bug -- wrong package scan
@ComponentScan(basePackages = "com.wrong.package")
public class Application {}

// Fix -- correct package
@ComponentScan(basePackages = "com.example")
public class Application {}
```
