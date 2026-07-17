---
title: "[Solution] Elasticsearch ResponseException — ES REST Client Fix"
description: "Fix Elasticsearch ResponseException when REST client receives error responses. Handle ES connection and query errors."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["elasticsearch", "rest-client", "response-exception", "search", "http"]
weight: 5
---

# Elasticsearch ResponseException — ES REST Client Fix

A `ResponseException` from the Elasticsearch REST client is thrown when the client receives an error response from Elasticsearch. This includes connection failures, mapping errors, and query errors.

## What This Error Means

Common message:

- `ResponseException: method [GET], host [localhost:9200], URI [/my-index/_search]`
- `ResponseException: [mapper_parsing_exception]`

## Common Causes

```java
// Cause 1: Index does not exist
RestHighLevelClient client = ...;
client.get(new GetRequest("nonexistent-index", "1"), RequestOptions.DEFAULT);

// Cause 2: Mapping error
// Field type mismatch in indexing request

// Cause 3: Connection refused
// Elasticsearch not running on localhost:9200
```

## How to Fix

### Fix 1: Create index first

```java
CreateIndexRequest request = new CreateIndexRequest("my-index");
client.indices().create(request, RequestOptions.DEFAULT);
```

### Fix 2: Check Elasticsearch connectivity

```bash
curl -v http://localhost:9200/
curl http://localhost:9200/_cluster/health
```

### Fix 3: Handle errors gracefully

```java
try {
    GetResponse response = client.get(
        new GetRequest("my-index", "1"), RequestOptions.DEFAULT);
} catch (ResponseException e) {
    if (e.getResponse().getStatusLine().getStatusCode() == 404) {
        // Handle not found
    }
}
```

### Fix 4: Use correct mapping

```java
XContentBuilder mapping = XContentFactory.jsonBuilder()
    .startObject()
        .startObject("properties")
            .startObject("name")
                .field("type", "text")
            .endObject()
            .startObject("email")
                .field("type", "keyword")
            .endObject()
        .endObject()
    .endObject();
```

## Related Errors

- {{< relref "spring-data-elasticsearch" >}} — Spring Data Elasticsearch errors
- {{< relref "testcontainers-elasticsearch" >}} — ElasticsearchContainer startup failed
