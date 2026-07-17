---
title: "[Solution] Testcontainers LocalStack Container Failed Fix"
description: "Fix Testcontainers LocalStack container startup failures. Resolve AWS service emulation issues, image problems, and port conflicts."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Testcontainers LocalStack Container Failed Fix

A Testcontainers LocalStack container failure occurs when the LocalStack container cannot start, initialize AWS services, or accept client connections.

## What This Error Means

Common messages:

- `ContainerLaunchException: Container failed to start`
- `LocalStackConnectionException: Could not connect to LocalStack`
- `AmazonServiceException: The bucket you are attempting to access must be addressed using the specified endpoint`
- `SdkClientException: Unable to execute HTTP request`

The LocalStack container either failed to start within the timeout, its services are not ready, or the AWS SDK client is pointing to the wrong endpoint.

## Common Causes

```java
// Cause 1: Docker not available or wrong image
GenericContainer<?> localstack = new GenericContainer<>(
    DockerImageName.parse("localstack/localstack:2.3")
).withExposedPorts(4566);
localstack.start();  // ContainerLaunchException

// Cause 2: Services not initialized
// Client connects before S3/DynamoDB/etc. is ready

// Cause 3: Wrong endpoint configuration
// Client points to localhost:4566 instead of container mapped port

// Cause 4: Region mismatch
// Client configured for us-east-1, bucket in us-west-2
```

## How to Fix

### Fix 1: Use LocalStack testcontainers module

```xml
<dependency>
    <groupId>org.testcontainers</groupId>
    <artifactId>localstack</artifactId>
    <version>1.19.3</version>
</dependency>
```

### Fix 2: Configure LocalStack with services

```java
@Testcontainers
class S3IntegrationTest {

    @Container
    static LocalStackContainer localstack = new LocalStackContainer(
        DockerImageName.parse("localstack/localstack:2.3")
    ).withServices(LocalStackContainer.Service.S3);

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("aws.endpoint", () -> localstack.getEndpointOverride(LocalStackContainer.Service.S3));
        registry.add("aws.region", () -> localstack.getRegion());
    }
}
```

### Fix 3: Create S3 bucket with correct client

```java
S3Client s3 = S3Client.builder()
    .endpointOverride(localstack.getEndpointOverride(LocalStackContainer.Service.S3))
    .credentialsProvider(StaticCredentialsProvider.create(
        AwsBasicCredentials.create(localstack.getAccessKey(), localstack.getSecretKey())
    ))
    .region(Region.of(localstack.getRegion()))
    .forcePathStyle(true)
    .build();

s3.createBucket(CreateBucketRequest.builder().bucketName("test-bucket").build());
```

### Fix 4: Add startup readiness check

```java
LocalStackContainer localstack = new LocalStackContainer(
    DockerImageName.parse("localstack/localstack:2.3")
).withServices(LocalStackContainer.Service.S3)
 .waitingFor(Wait.forLogMessage(".*Ready.*\\n", 1)
    .withStartupTimeout(Duration.ofSeconds(60)));
```

### Fix 5: Set resource limits

```java
GenericContainer<?> localstack = new GenericContainer<>(
    DockerImageName.parse("localstack/localstack:2.3")
).withExposedPorts(4566)
 .withEnv("SERVICES", "s3,dynamodb,sqs")
 .withCreateContainerCmdModifier(cmd -> {
     cmd.getHostConfig().withMemory(1024L * 1024 * 1024);  // 1GB
 });
```

## Related Errors

- {{< relref "testcontainers" >}} — Testcontainers general error.
- {{< relref "testcontainers-redis" >}} — Testcontainers Redis error.
