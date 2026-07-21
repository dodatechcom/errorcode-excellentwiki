---
title: "[Solution] Neo4j APOC Async Error"
description: "Fix Neo4j APOC async procedure errors when background operations fail"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Async Error

APOC async errors occur when asynchronous procedures fail during background execution.

## Common Causes

- Async job queue is full
- Background thread pool exhausted
- Async task references deleted node
- Network timeout in async HTTP call

## Common Error Messages

```
Neo.ClientError.General.OutOfMemoryError: Async job queue is full
```

## How to Fix It

### 1. Monitor Async Jobs

```cypher
CALL apoc.periodic.list() YIELD jobId, status, description;
```

### 2. Cancel Stuck Jobs

```cypher
CALL apoc.periodic.cancel('job-id');
```

### 3. Increase Thread Pool

```properties
# neo4j.conf
dbms.security.procedures.unrestricted=apoc.async.*
```

## Examples

```cypher
CALL apoc.periodic.submit('myJob', 'MATCH (n:User) SET n.processed = true');
```
