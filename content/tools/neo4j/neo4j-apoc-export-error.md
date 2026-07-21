---
title: "[Solution] Neo4j APOC Export Error"
description: "Fix Neo4j APOC export errors when exporting graph data to CSV or JSON files"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Export Error

APOC export errors occur when export procedures fail to write data to files.

## Common Causes

- Output directory not writable
- Export file already exists and overwrite disabled
- Query returning too many rows for export
- Disk space insufficient

## Common Error Messages

```
apoc.exception.FileAlreadyExists: File already exists
```

## How to Fix It

### 1. Enable Overwrite

```cypher
CALL apoc.export.csv.query(
  'MATCH (n:User) RETURN n.name, n.email',
  'users.csv',
  {overwrite: true}
);
```

### 2. Export to Different Directory

```cypher
CALL apoc.export.csv.all('/tmp/export.csv', {overwrite: true});
```

### 3. Limit Export Rows

```cypher
CALL apoc.export.csv.query(
  'MATCH (n:User) RETURN n.name LIMIT 1000',
  'users_subset.csv'
);
```

## Examples

```cypher
CALL apoc.export.json.data(
  MATCH (n:User) RETURN n,
  '/tmp/users.json',
  {format: 'ARRAY'}
);
```
