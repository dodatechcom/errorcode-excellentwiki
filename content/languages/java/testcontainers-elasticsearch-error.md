---
title: "[Solution] Testcontainers Elasticsearch Container Failed Fix"
description: "Fix Testcontainers Elasticsearch container startup failures. Resolve image issues, memory limits, and cluster health problems."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["testcontainers", "elasticsearch", "docker", "integration-test", "search"]
weight: 5
---

# Testcontainers Elasticsearch Container Failed Fix

A Testcontainers Elasticsearch container failure occurs when the Elasticsearch container cannot start, form a cluster, or accept connections within the timeout.

## What This Error Means

Common messages:

- `ContainerLaunchException: Container failed to start`
- `Connection refused: localhost/127.0.0.1:9200`
- `ElasticsearchStatusException: Elasticsearch exception [cluster_block_exception]`
- `ResponseException: method [GET], host [localhost], URI [/]`

The Elasticsearch Docker container started but failed to initialize its cluster, or the client cannot connect to the containerized Elasticsearch instance.

## Common Causes

```java
// Cause 1: Docker not available
ElasticsearchContainer es = new ElasticsearchContainer(
    DockerImageName.parse("elasticsearch:8.11.0")
);
es.start();  // ContainerLaunchException

// Cause 2: Insufficient memory (Elasticsearch needs 2GB+)
// Default Docker memory 2GB may be too low

// Cause 3: Security settings blocking connections
// Elasticsearch 8.x enables security by default

// Cause 4: Cluster health not RED
// Single node cluster with shards not allocated
```

## How to Fix

### Fix 1: Use @Container for lifecycle management

```java
@Testcontainers
class ElasticsearchIntegrationTest {

    @Container
    static ElasticsearchContainer es = new ElasticsearchContainer(
        DockerImageName.parse("elasticsearch:8.11.0")
    ).withExposedPorts(9200)
     .withEnv("discovery.type", "single-node")
     .withEnv("xpack.security.enabled", "false");

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.elasticsearch.uris",
            () -> "http://" + es.getHost() + ":" + es.getMappedPort(9200));
    }
}
```

### Fix 2: Set sufficient memory

```java
ElasticsearchContainer es = new ElasticsearchContainer(
    DockerImageName.parse("elasticsearch:8.11.0")
).withCreateContainerCmdModifier(cmd -> {
    cmd.getHostConfig().withMemory(2L * 1024 * 1024 * 1024);  // 2GB
});
```

### Fix 3: Disable security for test environment

```java
ElasticsearchContainer es = new ElasticsearchContainer(
    DockerImageName.parse("elasticsearch:8.11.0")
).withEnv("xpack.security.enabled", "false")
 .withEnv("xpack.security.http.ssl.enabled", "false")
 .withEnv("xpack.security.transport.ssl.enabled", "false");
```

### Fix 4: Wait for cluster health

```java
ElasticsearchContainer es = new ElasticsearchContainer(
    DockerImageName.parse("elasticsearch:8.11.0")
).waitingFor(Wait.forHttp("/_cluster/health?wait_for_status=green")
    .forPort(9200)
    .withStartupTimeout(Duration.ofSeconds(120)));
```

### Fix 5: Use correct Elasticsearch client

```java
RestHighLevelClient client = new RestHighLevelClient(
    RestClient.builder(
        new HttpHost(es.getHost(), es.getMappedPort(9200), "http")
    )
);
```

## Related Errors

- {{< relref "elasticsearch-rest" >}} — Elasticsearch REST client error.
- {{< relref "testcontainers" >}} — Testcontainers general error.
