---
title: "[Solution] LocalStackContainer Startup Failed — Testcontainers LocalStack Fix"
description: "Fix LocalStackContainer startup failure in Testcontainers. Check Docker and LocalStack configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["testcontainers", "localstack", "docker", "container", "aws"]
weight: 5
---

# LocalStackContainer Startup Failed — Testcontainers LocalStack Fix

A LocalStackContainer fails to start in Testcontainers. This prevents integration tests from running against a real LocalStack (AWS mock) instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
LocalStackContainer localstack = new LocalStackContainer(DockerImageName.parse("localstack/localstack:2.3"));
localstack.start();

// Cause 2: Insufficient resources

// Cause 3: Port conflict
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class LocalStackIntegrationTest {

    @Container
    static LocalStackContainer localstack = new LocalStackContainer(
        DockerImageName.parse("localstack/localstack:2.3"))
        .withServices(LocalStackContainer.Service.S3, LocalStackContainer.Service.SQS);

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.cloud.aws.endpoint", localstack::getEndpointOverride);
        registry.add("spring.cloud.aws.region.static", () -> "us-east-1");
    }
}
```

### Fix 2: Configure specific services

```java
LocalStackContainer localstack = new LocalStackContainer(
    DockerImageName.parse("localstack/localstack:2.3"))
    .withServices(
        LocalStackContainer.Service.S3,
        LocalStackContainer.Service.SQS,
        LocalStackContainer.Service.SNS,
        LocalStackContainer.Service.DYNAMODB);
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "importerror-boto3" >}} — ImportError: boto3 (Python)
- {{< relref "importerror-docker" >}} — ImportError: docker (Python)
