---
title: "[Solution] UnsatisfiedDependencyException — Spring Boot DataSource Configuration Fix"
description: "Fix UnsatisfiedDependencyException when Spring Boot cannot create the dataSource bean. Configure database connections correctly."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# UnsatisfiedDependencyException — Spring Boot DataSource Configuration Fix

An `UnsatisfiedDependencyException` when creating the `dataSource` bean means Spring Boot's auto-configuration cannot find the required database connection properties. This is one of the most common Spring Boot startup errors and indicates a missing or misconfigured database connection.

## What This Error Means

Common messages:

- `UnsatisfiedDependencyException: Error creating bean with name 'dataSource' defined in class path resource`
- `BeanCreationException: Error creating bean with name 'dataSource'`
- `Failed to configure a DataSource: 'url' attribute is not specified`

## Common Causes

```java
// Cause 1: Missing datasource properties in application.yml
// No spring.datasource.url defined

// Cause 2: Multiple datasource drivers on classpath
// Both H2 and PostgreSQL drivers present, auto-config confused

// Cause 3: Excluded auto-configuration accidentally
@SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })

// Cause 4: Wrong property key
spring:
  datasource:        # correct
  data-source:       # wrong — kebab case issue
```

## How to Fix

### Fix 1: Configure datasource properties in application.yml

Provide the required spring.datasource.* properties with correct values for your database.

```java
spring:
  datasource:
    url: jdbc:postgresql://localhost:5432/myapp
    username: ${DB_USERNAME:postgres}
    password: ${DB_PASSWORD:secret}
    driver-class-name: org.postgresql.Driver
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      idle-timeout: 30000
      connection-timeout: 20000
```

### Fix 2: Exclude conflicting auto-configuration

If you are using a non-standard database setup, exclude the auto-configuration and define your own DataSource bean.

```java
@SpringBootApplication(exclude = {
    DataSourceAutoConfiguration.class,
    DataSourceTransactionManagerAutoConfiguration.class
})
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

@Configuration
public class DataSourceConfig {

    @Bean
    public DataSource dataSource() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:postgresql://localhost:5432/myapp");
        config.setUsername("postgres");
        config.setPassword("secret");
        config.setMaximumPoolSize(20);
        return new HikariDataSource(config);
    }
}
```

### Fix 3: Use multiple datasource configuration

When your application needs multiple databases, disable the default auto-configuration and configure each datasource explicitly.

```java
@Configuration
public class MultiDataSourceConfig {

    @Primary
    @Bean
    @ConfigurationProperties("spring.datasource.primary")
    public DataSource primaryDataSource() {
        return DataSourceBuilder.create().build();
    }

    @Bean
    @ConfigurationProperties("spring.datasource.secondary")
    public DataSource secondaryDataSource() {
        return DataSourceBuilder.create().build();
    }
}

# application.yml
spring:
  datasource:
    primary:
      url: jdbc:postgresql://primary-host:5432/db1
      username: user1
      password: pass1
    secondary:
      url: jdbc:mysql://secondary-host:3306/db2
      username: user2
      password: pass2
```

## Related Errors

- {{< relref "spring-boot-autoconfig-error" >}} — Auto-Configuration Failed
- {{< relref "jdbc-conn" >}} — JDBC Connection Error
