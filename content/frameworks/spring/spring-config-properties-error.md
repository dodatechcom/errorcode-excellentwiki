---
title: "[Solution] Spring Configuration Properties Error"
description: "Fix Spring configuration properties errors when @ConfigurationProperties fails to bind or validate values."
frameworks: ["spring"]
error-types: ["configuration-error"]
severities: ["error"]
---

Configuration properties errors occur when `@ConfigurationProperties` cannot bind values from properties files or environment variables.

## Common Causes

- Property names do not match field names
- `@EnableConfigurationProperties` not activated
- Nested properties not properly structured
- Type mismatch between property and field
- Validation constraints not triggered

## How to Fix

### Define Configuration Properties

```java
@Component
@ConfigurationProperties(prefix = "app")
@Validated
public class AppProperties {
    @NotBlank
    private String name;

    @Min(1)
    @Max(100)
    private int maxConnections;

    private Database database = new Database();

    // Getters and setters

    public static class Database {
        private String url;
        private int poolSize;
        // Getters and setters
    }
}
```

### Configure in YAML

```yaml
# application.yml
app:
  name: my-application
  max-connections: 50
  database:
    url: jdbc:postgresql://localhost:5432/db
    pool-size: 20
```

### Enable Configuration Properties

```java
@SpringBootApplication
@EnableConfigurationProperties(AppProperties.class)
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### Use @ConfigurationProperties on Bean

```java
@Bean
@ConfigurationProperties(prefix = "spring.datasource.hikari")
public HikariConfig hikariConfig() {
    return new HikariConfig();
}
```

## Examples

```java
// Bug -- prefix does not match
@ConfigurationProperties(prefix = "application")
public class AppProperties {
    private String name;
}

# application.yml
app:
  name: my-app  # Wrong prefix!

// Fix -- match prefix
@ConfigurationProperties(prefix = "app")
public class AppProperties {}
```
