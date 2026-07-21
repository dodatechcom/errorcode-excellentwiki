---
title: "[Solution] Neo4j APOC Export CSV Error"
description: "Fix Neo4j APOC CSV export errors when exporting query results to CSV files"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Export CSV Error

APOC CSV export errors occur when export procedures cannot write CSV data to the filesystem.

## Common Causes

- Export path not whitelisted
- File already exists without overwrite flag
- Query produces inconsistent column count
- Special characters in data breaking CSV format

## Common Error Messages

```
apoc.exception.FileAlreadyExists: File already exists
```

## How to Fix It

### 1. Whitelist Export Directory

```properties
# neo4j.conf
apoc.export.file.enabled=true
apoc.export.file.allowlist=/tmp/,/export/
```

### 2. Export with Overwrite

```cypher
CALL apoc.export.csv.query(
  'MATCH (n:User) RETURN n.name, n.email',
  '/tmp/users.csv',
  {overwrite: true}
);
```

### 3. Handle Special Characters

```cypher
CALL apoc.export.csv.query(
  'MATCH (n:User) RETURN n.name, replace(n.bio, ",", ";") AS bio',
  '/tmp/users.csv'
);
```

## Examples

```cypher
CALL apoc.export.csv.data(
  [n1, n2],
  [r1],
  '/tmp/export.csv',
  {stream: true}
);
```
