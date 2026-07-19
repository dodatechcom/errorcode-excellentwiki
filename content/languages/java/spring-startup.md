---
title: "[Solution] Java BeanCreationException — application fails to start due to config errors or bean init failures"
description: "Fix Java BeanCreationException when application fails to start due to config errors or bean init failures with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# BeanCreationException — application fails to start due to config errors or bean init failures

A `BeanCreationException` occurs when @Value("${app.database.url}")
private String dbUrl;  // MissingResourceException if not defined.

## Common Causes

```java
@Value("${app.database.url}")
private String dbUrl;  // MissingResourceException if not defined
```

## Solutions

```java
// Fix: default values
@Value("${app.database.url:jdbc:h2:mem:test}") private String dbUrl;

// Fix: @ConfigurationProperties with validation
@ConfigurationProperties(prefix="app")
@Validated
public class AppConfig {
    @NotBlank private String databaseUrl;
}

// Fix: check application.yml for typos
// spring.datasource.url=jdbc:mysql://localhost:3306/mydb
```

## Prevention Checklist

- Use @Value with defaults.
- Use @ConfigurationProperties with @Validated.
- Check application.yml for typos.
- Use spring-boot-configuration-processor.

## Related Errors

NoSuchBeanDefinitionException, MissingRequiredPropertiesException
