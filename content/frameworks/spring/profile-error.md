---
title: "Profile not found"
description: "Spring fails to start because the requested active profile does not exist in the configuration"
frameworks: ["spring"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Spring is started with an active profile (via `spring.profiles.active` or command-line argument) that does not have a corresponding properties or YAML file, or references beans that do not exist.

## Common Causes

- Typo in the profile name passed via `--spring.profiles.active`
- Profile-specific config file does not exist (`application-dev.yml`)
- Profile-conditional beans are not available (`@Profile("dev")`)
- Bean depends on a profile-specific property that is missing

## How to Fix

1. Create profile-specific configuration files:

```
src/main/resources/
  application.yml
  application-dev.yml
  application-prod.yml
```

2. Set the active profile correctly:

```bash
# Via command line
java -jar app.jar --spring.profiles.active=dev

# Via environment variable
SPRING_PROFILES_ACTIVE=dev java -jar app.jar
```

3. Use `@Profile` annotation to conditionally define beans:

```java
@Configuration
@Profile("dev")
public class DevConfig {
    @Bean
    public DataSource dataSource() {
        return new EmbeddedDatabaseBuilder().build();
    }
}
```

4. Provide default values for optional profile-specific properties:

```yaml
# application.yml
spring:
  profiles:
    active: dev

# application-dev.yml
spring:
  datasource:
    url: jdbc:h2:mem:testdb
```

## Examples

```bash
java -jar app.jar --spring.profiles.active=staging
```

```text
NoSuchBeanDefinitionException: No bean named 'dataSource' available:
No active profile set and no profile-specific bean definitions found
```

## Related Errors

- [Serialization error]({{< relref "/frameworks/spring/serialization-error" >}})
