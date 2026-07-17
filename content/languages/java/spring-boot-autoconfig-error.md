---
title: "[Solution] Spring Boot Auto-Configuration Failed Fix"
description: "Fix Spring Boot auto-configuration failures. Resolve conflicting beans, missing dependencies, and conditional configuration issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Spring Boot Auto-Configuration Failed Fix

A Spring Boot auto-configuration failure occurs when the application context cannot start due to conflicting bean definitions, missing required dependencies, or conditional configuration mismatches.

## What This Error Means

Common messages:

- `BeanCreationException: Error creating bean with name 'dataSource' defined in class path resource`
- `Unsatisfied dependency expressed through field 'userRepository'`
- `No qualifying bean of type 'DataSource' available`
- `BeanCurrentlyInCreationException: Requested bean is currently in creation`

Spring Boot's auto-configuration tries to configure beans automatically based on classpath dependencies. When conditions conflict or required beans are missing, the application fails to start.

## Common Causes

```java
// Cause 1: Multiple datasource auto-configurations on classpath
// Both H2 and PostgreSQL drivers present — which one to use?

// Cause 2: Missing required property
// application.yml missing spring.datasource.url

// Cause 3: Conflicting manual and auto-configured beans
@Configuration
public class AppConfig {
    @Bean
    public DataSource dataSource() { ... }  // Conflicts with auto-config
}

// Cause 4: Starter dependency missing
// Using JdbcTemplate but spring-boot-starter-jdbc not on classpath
```

## How to Fix

### Fix 1: Exclude conflicting auto-configurations

```java
@SpringBootApplication(exclude = {
    DataSourceAutoConfiguration.class,
    HibernateJpaAutoConfiguration.class,
})
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### Fix 2: Set required properties

```yaml
# application.yml
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/mydb
    username: user
    password: pass
    driver-class-name: org.postgresql.Driver
```

### Fix 3: Use conditional beans to avoid conflicts

```java
@Configuration
@ConditionalOnClass(name = "org.postgresql.Driver")
public class PostgresConfig {
    @Bean
    public DataSource dataSource() {
        return DataSourceBuilder.create()
            .url("jdbc:postgresql://localhost:5432/mydb")
            .build();
    }
}
```

### Fix 4: Debug auto-configuration report

```yaml
# application.yml
debug: true
```

```bash
# Or start with --debug flag
java -jar app.jar --debug
```

### Fix 5: Use @Primary for ambiguous beans

```java
@Configuration
public class DataSourceConfig {
    @Primary
    @Bean
    public DataSource primaryDataSource() {
        return createDataSource("primary");
    }

    @Bean
    public DataSource secondaryDataSource() {
        return createDataSource("secondary");
    }
}
```

### Fix 6: Check dependency tree for conflicts

```bash
mvn dependency:tree
gradle dependencies
```

## Related Errors

- {{< relref "spring-bean" >}} — Spring bean creation error.
- {{< relref "spring-validation" >}} — Spring validation configuration error.
