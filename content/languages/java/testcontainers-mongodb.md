---
title: "[Solution] MongoDBContainer Startup Failed — Testcontainers MongoDB Fix"
description: "Fix MongoDBContainer startup failure in Testcontainers. Check Docker and MongoDB configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# MongoDBContainer Startup Failed — Testcontainers MongoDB Fix

A MongoDBContainer fails to start in Testcontainers. This prevents integration tests from running against a real MongoDB instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
MongoDBContainer mongo = new MongoDBContainer(DockerImageName.parse("mongo:7.0"));
mongo.start();

// Cause 2: Insufficient disk space

// Cause 3: Port conflict
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class MongoDBIntegrationTest {

    @Container
    static MongoDBContainer mongo = new MongoDBContainer(
        DockerImageName.parse("mongo:7.0"));

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.data.mongodb.uri", mongo::getReplicaSetUrl);
    }
}
```

### Fix 2: Use with authentication

```java
MongoDBContainer mongo = new MongoDBContainer(DockerImageName.parse("mongo:7.0"))
    .withUsername("admin")
    .withPassword("password");
```

### Fix 3: Initialize with replica set

```java
MongoDBContainer mongo = new MongoDBContainer(DockerImageName.parse("mongo:7.0"))
    .withReplicaSet("rs0");
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "importerror-pymongo" >}} — ImportError: pymongo (Python)
- {{< relref "spring-data-r2dbc" >}} — DataIntegrityViolationException R2DBC
