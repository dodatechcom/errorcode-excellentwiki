---
title: "[Solution] BeanDefinitionOverrideException — Spring Boot Auto-Configuration Order Fix"
description: "Fix BeanDefinitionOverrideException when Spring Boot auto-configuration creates duplicate bean definitions. Resolve bean override conflicts."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# BeanDefinitionOverrideException — Spring Boot Auto-Configuration Order Fix

A `BeanDefinitionOverrideException` means Spring Boot detected two beans with the same name and the override is not explicitly allowed. This commonly happens when your custom configuration defines a bean that conflicts with a Spring Boot auto-configured bean.

## What This Error Means

Common messages:

- `BeanDefinitionOverrideException: Invalid bean definition with name 'dataSource'`
- `BeanDefinitionOverrideException: Definition of bean 'entityManagerFactory' conflicts`
- `BeanCreationException: Unexpected exception during bean creation`

## Common Causes

```java
// Cause 1: Your @Bean method conflicts with auto-configuration
@Configuration
public class AppConfig {
    @Bean
    public DataSource dataSource() { ... }  // Conflicts with auto-config
}

// Cause 2: Multiple @Configuration classes define same bean name
@Configuration
public class DataSourceConfigA {
    @Bean("dataSource")
    public DataSource dataSourceA() { ... }
}
@Configuration
public class DataSourceConfigB {
    @Bean("dataSource")  // Duplicate!
    public DataSource dataSourceB() { ... }
}

// Cause 3: Spring Boot 2.1+ disallows bean overriding by default
```

## How to Fix

### Fix 1: Allow bean definition overriding explicitly

Enable bean override in application.yml to allow your custom bean to replace the auto-configured one.

```java
# application.yml
spring:
  main:
    allow-bean-definition-overriding: true

# Or disable specific auto-configuration instead
@SpringBootApplication(exclude = {
    DataSourceAutoConfiguration.class
})
```

### Fix 2: Use @Primary to resolve ambiguous bean definitions

When multiple beans of the same type exist, mark one as @Primary to make it the default injection candidate.

```java
@Configuration
public class DataSourceConfig {

    @Primary
    @Bean
    public DataSource primaryDataSource() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:postgresql://primary:5432/db1");
        return new HikariDataSource(config);
    }

    @Bean
    public DataSource analyticsDataSource() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:postgresql://analytics:5432/db2");
        config.setDataSourceClassName(
            "org.postgresql.ds.PGSimpleDataSource");
        return new HikariDataSource(config);
    }
}

// Inject primary by default
@Service
public class UserService {
    @Autowired
    private DataSource dataSource; // Gets primaryDataSource

    // Or inject specific by name
    @Qualifier("analyticsDataSource")
    @Autowired
    private DataSource analyticsDs;
}
```

### Fix 3: Use @ConditionalOnMissingBean to avoid conflicts

Annotate your custom bean with @ConditionalOnMissingBean so it only registers when no auto-configured bean exists.

```java
@Configuration
public class CustomAutoConfiguration {

    @Bean
    @ConditionalOnMissingBean(DataSource.class)
    public DataSource customDataSource() {
        // Only creates if no DataSource exists
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:h2:mem:defaultdb");
        return new HikariDataSource(config);
    }

    @Bean
    @ConditionalOnMissingBean(CacheManager.class)
    public CacheManager customCacheManager() {
        return new ConcurrentMapCacheManager("default");
    }
}
```

## Related Errors

- {{< relref "spring-boot-autoconfig-error" >}} — Auto-Configuration Failed
- {{< relref "spring-boot-datasource" >}} — DataSource Configuration Error
