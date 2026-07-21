---
title: "[Solution] Spring Flyway Baseline Error"
description: "Fix Spring Flyway baseline errors when applying migrations to an existing database fails."
frameworks: ["spring"]
error-types: ["database-error"]
severities: ["error"]
---

Flyway baseline errors occur when the existing database schema does not match the baseline version, causing Flyway to fail on startup.

## Common Causes

- Database already has tables but Flyway is not initialized
- Baseline version set incorrectly
- `flyway_schema_history` table missing
- Existing schema changes not captured in baseline
- Multiple database instances with different states

## How to Fix

### Set Baseline on Migrate

```yaml
spring:
  flyway:
    enabled: true
    baseline-on-migrate: true
    baseline-version: 1
    baseline-description: "Initial schema"
```

### Create Baseline Manually

```bash
# Create baseline from existing schema
flyway baseline -baselineVersion=1 -baselineDescription="Existing schema"
```

### Handle Existing Database

```java
@Configuration
public class FlywayConfig {
    @Bean
    public FlywayMigrationInitializer flywayInitializer(DataSource dataSource) {
        Flyway flyway = Flyway.configure()
            .dataSource(dataSource)
            .locations("classpath:db/migration")
            .baselineOnMigrate(true)
            .baselineVersion(Version.fromVersion("1"))
            .load();
        return new FlywayMigrationInitializer(flyway);
    }
}
```

### Repair Corrupted History

```bash
# Repair flyway_schema_history
flyway repair

# Or manually fix
DELETE FROM flyway_schema_history WHERE success = false;
```

## Examples

```yaml
# Bug -- baseline not enabled
spring:
  flyway:
    enabled: true
    # baseline-on-migrate: false  (default)
    # Fails if database already has tables

# Fix -- enable baseline
spring:
  flyway:
    enabled: true
    baseline-on-migrate: true
    baseline-version: 0
```
