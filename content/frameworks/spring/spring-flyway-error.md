---
title: "[Solution] Spring Flyway Migration Error"
description: "Fix Spring Flyway migration errors when database migrations fail to execute or conflict."
frameworks: ["spring"]
error-types: ["database-error"]
severities: ["error"]
---

Flyway migration errors occur when SQL migration scripts have syntax errors, version conflicts, or the migration table is corrupted.

## Common Causes

- Migration script has SQL syntax errors
- Two migrations with the same version number
- Migration modifies already-executed version
- `flyway_schema_history` table corrupted
- Baseline not set for existing database

## How to Fix

### Configure Flyway

```yaml
# application.yml
spring:
  flyway:
    enabled: true
    locations: classpath:db/migration
    baseline-on-migrate: true
    baseline-version: 1
```

### Write Migration Scripts

```sql
-- V1__create_users_table.sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- V2__add_user_status.sql
ALTER TABLE users ADD COLUMN status VARCHAR(20) DEFAULT 'active';
```

### Handle Migration Failures

```java
@Configuration
public class FlywayConfig {
    @Bean
    public FlywayMigrationInitializer flywayInitializer(DataSource dataSource) {
        Flyway flyway = Flyway.configure()
            .dataSource(dataSource)
            .locations("classpath:db/migration")
            .baselineOnMigrate(true)
            .load();
        return new FlywayMigrationInitializer(flyway, (f) -> {
            try {
                f.migrate();
            } catch (Exception e) {
                log.error("Flyway migration failed", e);
            }
        });
    }
}
```

## Examples

```sql
-- Bug -- duplicate version
-- V1__create_table.sql (already executed)
CREATE TABLE users (id BIGINT PRIMARY KEY);

-- Fix -- create new version
-- V3__add_index.sql
CREATE INDEX idx_users_email ON users(email);
```

Check migration status: `flyway info`
