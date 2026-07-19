---
title: "[Solution] FlywayMigrateException — Spring Boot Flyway Migration Fix"
description: "Fix FlywayMigrateException when database migrations fail in Spring Boot. Resolve version conflicts, checksum errors, and schema issues."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# FlywayMigrateException — Spring Boot Flyway Migration Fix

A `FlywayMigrateException` means Flyway could not apply database migrations during Spring Boot startup. This happens when migration scripts have errors, version conflicts, or when the database schema is out of sync with the migration history.

## What This Error Means

Common messages:

- `org.flywaydb.core.internal.exception.FlywayMigrateException: Migration failed`
- `FlywayMigrateException: Unable to migrate schema for table flyway_schema_history`
- `MigrationException: Failed to execute migration V3__add_user_table.sql`

## Common Causes

```java
// Cause 1: Migration script has SQL syntax errors
// V2__create_orders_table.sql contains invalid SQL

// Cause 2: Checksum mismatch — migration was modified after execution
// V1__init.sql was changed after it was already applied

// Cause 3: Out-of-order migrations enabled but version conflict
// V5 exists but V4 was never run

// Cause 4: Missing required table or column referenced in migration
// ALTER TABLE users ADD COLUMN email already exists
```

## How to Fix

### Fix 1: Repair the Flyway schema history table

When migrations fail partway through, repair the schema history table to remove the failed migration entry, then re-run.

```java
# Using Flyway CLI
flyway repair -url=jdbc:postgresql://localhost:5432/mydb \
    -user=postgres -password=secret

# Or using Spring Boot Actuator endpoint
curl -X POST http://localhost:8080/actuator/flyway \
    -H "Content-Type: application/json" \
    -d '{"action": "repair"}'

# Java programmatic repair
Flyway flyway = Flyway.configure()
    .dataSource(dataSource)
    .load();
flyway.repair();
```

### Fix 2: Add placeholder support for environment-specific values

Use Flyway placeholders to inject environment-specific values like schema names or column defaults.

```java
# application.yml
spring:
  flyway:
    enabled: true
    locations: classpath:db/migration
    placeholders:
      schema: public
      defaultUser: system

# V1__init.sql
CREATE SCHEMA IF NOT EXISTS \${schema};
CREATE TABLE \${schema}.users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL DEFAULT '\${defaultUser}'
);
```

### Fix 3: Configure Flyway to handle out-of-order migrations

Enable out-of-order migrations for development environments while keeping strict ordering in production.

```java
# application.yml
spring:
  flyway:
    enabled: true
    out-of-order: true
    validate-on-migrate: true
    baseline-on-migrate: true
    baseline-version: 0

# For production, disable out-of-order
---
spring:
  config:
    activate:
      on-profile: production
  flyway:
    out-of-order: false
    validate-on-migrate: true
```

## Related Errors

- {{< relref "spring-boot-datasource" >}} — DataSource Configuration Error
- {{< relref "sql-exception" >}} — SQL Exception
