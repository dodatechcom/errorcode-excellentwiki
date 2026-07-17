---
title: "[Solution] ElasticsearchContainer Startup Failed — Testcontainers Elasticsearch Fix"
description: "Fix ElasticsearchContainer startup failure in Testcontainers. Check Docker and Elasticsearch configuration."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# ElasticsearchContainer Startup Failed — Testcontainers Elasticsearch Fix

An ElasticsearchContainer fails to start in Testcontainers. This prevents integration tests from running against a real Elasticsearch instance.

## What This Error Means

Common message:

- `Container startup failed`

## Common Causes

```java
// Cause 1: Image not available
ElasticsearchContainer es = new ElasticsearchContainer(DockerImageName.parse("elasticsearch:8.11.0"));
es.start();

// Cause 2: Insufficient resources
// Elasticsearch needs at least 512MB heap

// Cause 3: Security configuration
// Elasticsearch 8.x has security enabled by default
```

## How to Fix

### Fix 1: Use @Container annotation

```java
@Testcontainers
class ElasticsearchIntegrationTest {

    @Container
    static ElasticsearchContainer es = new ElasticsearchContainer(
        DockerImageName.parse("elasticsearch:8.11.0"))
        .withExposedPorts(9200)
        .withEnv("discovery.type", "single-node")
        .withEnv("xpack.security.enabled", "false");

    @DynamicPropertySource
    static void configure(DynamicPropertyRegistry registry) {
        registry.add("spring.elasticsearch.uris",
            () -> "http://" + es.getHost() + ":" + es.getMappedPort(9200));
    }
}
```

### Fix 2: Use OpenSearch instead

```java
GenericContainer<?> opensearch = new GenericContainer<>(DockerImageName.parse("opensearchproject/opensearch:2.11.0"))
    .withExposedPorts(9200)
    .withEnv("discovery.type", "single-node")
    .withEnv("plugins.security.disabled", "true");
```

### Fix 3: Set memory limits

```java
ElasticsearchContainer es = new ElasticsearchContainer(DockerImageName.parse("elasticsearch:8.11.0"))
    .withCreateContainerCmdModifier(cmd -> {
        cmd.getHostConfig().withMemory(1024L * 1024 * 1024);
    });
```

## Related Errors

- {{< relref "testcontainers" >}} — General Testcontainers failure
- {{< relref "spring-data-elasticsearch" >}} — ElasticsearchException
- {{< relref "elasticsearch-rest" >}} — ResponseException
