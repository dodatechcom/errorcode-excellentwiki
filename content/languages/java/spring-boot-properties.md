---
title: "[Solution] ConfigurationProperties Bind Error — Spring Boot Fix"
description: "Fix @ConfigurationProperties binding errors in Spring Boot. Resolve property binding failures and prefix mismatches."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ConfigurationProperties Bind Error — Spring Boot Fix

A `@ConfigurationProperties` binding error occurs when Spring Boot cannot map externalized configuration properties to a Java bean. This is caused by mismatched property names, missing setter methods, or incorrect prefix configuration.

## What This Error Means

Common messages:

- `ConfigurationPropertiesBindException: Cannot bind @ConfigurationProperties`
- `BindException: Failed to bind properties under 'app.mail' to MailProperties`
- `BeanCreationException: Error creating bean with name 'mailProperties'`

## Common Causes

```java
// Cause 1: Missing setter or constructor binding
@ConfigurationProperties(prefix = "app.mail")
public class MailProperties {
    private String host;  // No setter, no constructor!
}

// Cause 2: Property name mismatch
// YAML: app.mail-host: smtp.example.com
// Java: @ConfigurationProperties(prefix = "app") — prefix too short

// Cause 3: Missing @EnableConfigurationProperties or @ConfigurationPropertiesScan
// Properties class exists but is not registered as a bean
```

## How to Fix

### Fix 1: Use record types for immutable configuration binding

Java records provide constructor binding automatically, eliminating the need for setter methods.

```java
@ConfigurationProperties(prefix = "app.mail")
public record MailProperties(
    String host,
    int port,
    String username,
    String password,
    Map<String, String> properties
) {}

# application.yml
app:
  mail:
    host: smtp.example.com
    port: 587
    username: user@example.com
    password: secret
    properties:
      mail.smtp.auth: true
      mail.smtp.starttls.enable: true
```

### Fix 2: Enable @ConfigurationPropertiesScan for automatic discovery

Use @ConfigurationPropertiesScan to automatically find and register all @ConfigurationProperties classes in your project.

```java
@SpringBootApplication
@ConfigurationPropertiesScan  // Auto-discovers all @ConfigurationProperties
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

// Properties class — no explicit @Bean needed
@ConfigurationProperties(prefix = "app.cache")
public class CacheProperties {
    private Duration ttl = Duration.ofMinutes(30);
    private int maxEntries = 1000;
    private boolean enabled = true;

    // Getters and setters
    public Duration getTtl() { return ttl; }
    public void setTtl(Duration ttl) { this.ttl = ttl; }
    public int getMaxEntries() { return maxEntries; }
    public void setMaxEntries(int maxEntries) { this.maxEntries = maxEntries; }
    public boolean isEnabled() { return enabled; }
    public void setEnabled(boolean enabled) { this.enabled = enabled; }
}
```

### Fix 3: Use @Validated for nested property validation

Add validation annotations to @ConfigurationProperties to ensure required properties are present at startup.

```java
@ConfigurationProperties(prefix = "app.database")
@Validated
public class DatabaseProperties {

    @NotBlank
    private String url;

    @NotBlank
    private String username;

    @Min(1)
    @Max(100)
    private int poolSize = 10;

    @Valid
    private SslProperties ssl = new SslProperties();

    // Getters and setters
}

public class SslProperties {
    private boolean enabled = false;
    private String trustStore;

    // Getters and setters
}
```

## Related Errors

- {{< relref "spring-boot-yaml" >}} — YAML Parsing Error
- {{< relref "spring-boot-profile" >}} — Profile Activation Error
