---
title: "[Solution] IllegalStateException — Spring Boot Profile Activation Fix"
description: "Fix IllegalStateException when Spring Boot profiles fail to activate. Resolve profile configuration and activation issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# IllegalStateException — Spring Boot Profile Activation Fix

An `IllegalStateException` with "The following profiles are active" means Spring Boot encountered an error during profile resolution or a required profile-specific configuration file is missing.

## What This Error Means

Common messages:

- `java.lang.IllegalStateException: The following profiles are active: dev,local`
- `IllegalStateException: Failed to load property source from location 'classpath:application-local.yml'`
- `IllegalStateException: Profile 'production' is not defined in any profile-specific property source`

## Common Causes

```java
// Cause 1: Missing profile-specific YAML file
// spring.profiles.active=production but application-production.yml missing

// Cause 2: Typo in profile name
// Active: "prod" but file is application-production.yml

// Cause 3: Conditional bean fails for missing profile
@Profile("staging")
@Bean
public StagingDataSource dataSource() {
    // This bean is required but staging config is incomplete
}

// Cause 4: spring.profiles.active and SPRING_PROFILES_ACTIVE conflict
```

## How to Fix

### Fix 1: Set profiles via multiple mechanisms with fallbacks

Configure profile activation using YAML, environment variables, and programmatic methods with clear precedence.

```java
# application.yml — default profile
spring:
  profiles:
    active: dev  # Fallback

# application-dev.yml — development overrides
---
spring:
  datasource:
    url: jdbc:h2:mem:devdb

# application-prod.yml — production overrides
---
spring:
  datasource:
    url: jdbc:postgresql://prod-host:5432/mydb

# Or set via environment variable (highest priority)
# SPRING_PROFILES_ACTIVE=dev,feature-x
```

### Fix 2: Use programmatic profile activation

Activate profiles programmatically in the main method for maximum control over which profiles are active.

```java
@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(
            Application.class);

        // Set default profiles programmatically
        app.setAdditionalProfiles("default");

        // Conditionally add profiles based on environment
        String env = System.getenv().getOrDefault(
            "APP_ENV", "dev");
        app.setAdditionalProfiles(env);

        // Add profile from command line as well
        if (args.length > 0 && "--prod".equals(args[0])) {
            app.setAdditionalProfiles("production");
        }

        app.run(args);
    }
}
```

### Fix 3: Use @ConditionalOnProperty for environment-specific beans

Replace @Profile with @ConditionalOnProperty for more flexible bean activation based on configuration values.

```java
@Configuration
public class CacheConfig {

    @Bean
    @ConditionalOnProperty(
        name = "app.cache.type",
        havingValue = "redis",
        matchIfMissing = false
    )
    public CacheManager redisCacheManager() {
        return new RedisCacheManager(redisConnectionFactory());
    }

    @Bean
    @ConditionalOnProperty(
        name = "app.cache.type",
        havingValue = "concurrent",
        matchIfMissing = true  // Default when not specified
    )
    public CacheManager concurrentCacheManager() {
        return new ConcurrentMapCacheManager();
    }
}
```

## Related Errors

- {{< relref "spring-boot-properties" >}} — ConfigurationProperties Bind Error
- {{< relref "spring-boot-yaml" >}} — YAML Parsing Error
