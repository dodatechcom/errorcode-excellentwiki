---
title: "[Solution] ClickHouseContainer Startup Failed — Testcontainers ClickHouse Fix"
description: "Fix ClickHouseContainer startup failure in Testcontainers. Check Docker and ClickHouse configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ClickHouseContainer Startup Failed — Testcontainers ClickHouse Fix

A ClickHouseContainer fails to start in Testcontainers. This prevents integration tests from running against a real ClickHouse instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
ClickHouseContainer clickhouse = new ClickHouseContainer(DockerImageName.parse("clickhouse/clickhouse-server:23.8"));
clickhouse.start();

// Cause 2: Insufficient resources

// Cause 3: Port conflict
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class ClickHouseIntegrationTest {

    @Container
    static ClickHouseContainer clickhouse = new ClickHouseContainer(
        DockerImageName.parse("clickhouse/clickhouse-server:23.8"));

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", clickhouse::getJdbcUrl);
        registry.add("spring.datasource.username", clickhouse::getUsername);
        registry.add("spring.datasource.password", clickhouse::getPassword);
    }
}
```

### Fix 2: Configure with additional ports

```java
ClickHouseContainer clickhouse = new ClickHouseContainer(
    DockerImageName.parse("clickhouse/clickhouse-server:23.8"))
    .withExposedPorts(8123, 9000);
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "sql-exception" >}} — SQL exception
- {{< relref "testcontainers-mysql" >}} — MySQLContainer startup failed
