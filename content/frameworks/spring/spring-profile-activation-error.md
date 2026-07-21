---
title: "[Solution] Spring Profile Activation Error"
description: "Fix Spring profile activation errors when the wrong profile is activated or profile-specific config is missing."
frameworks: ["spring"]
error-types: ["configuration-error"]
severities: ["error"]
---

Profile activation errors occur when Spring activates the wrong profile, profile-specific properties are not loaded, or conditional beans fail.

## Common Causes

- Profile not specified in application startup
- Profile name typo in configuration
- `@Profile` annotation on wrong beans
- Profile-specific property file missing
- Default profile not configured

## How to Fix

### Activate Profiles

```bash
# Command line
java -jar app.jar --spring.profiles.active=production

# Environment variable
export SPRING_PROFILES_ACTIVE=production

# application.yml
spring:
  profiles:
    active: development
```

### Configure Profile-Specific Properties

```
application.yml            # Common config
application-dev.yml        # Development
application-prod.yml       # Production
application-test.yml       # Testing
```

### Use @Profile Annotation

```java
@Configuration
public class DataSourceConfig {
    @Bean
    @Profile("dev")
    public DataSource devDataSource() {
        return new EmbeddedDatabaseBuilder()
            .setType(EmbeddedDatabaseType.H2)
            .build();
    }

    @Bean
    @Profile("prod")
    public DataSource prodDataSource() {
        HikariConfig config = new HikariConfig();
        config.setJdbcUrl("jdbc:postgresql://localhost:5432/prod");
        return new HikariDataSource(config);
    }
}
```

### Handle Missing Profiles

```java
@Bean
@ConditionalOnMissingBean
public DataSource defaultDataSource() {
    return new EmbeddedDatabaseBuilder()
        .setType(EmbeddedDatabaseType.H2)
        .build();
}
```

## Examples

```yaml
# Bug -- wrong profile name
spring:
  profiles:
    active: production  # File is application-prod.yml

# Fix -- match profile name to file
spring:
  profiles:
    active: prod
```

Verify profile-specific files exist:
```
application.yml
application-dev.yml
application-prod.yml
```
