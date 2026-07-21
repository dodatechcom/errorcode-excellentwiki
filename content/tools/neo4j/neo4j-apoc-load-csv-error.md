---
title: "[Solution] Neo4j APOC Load CSV Error"
description: "Fix Neo4j APOC load.csv errors when importing CSV data via APOC procedures"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Load CSV Error

APOC load.csv errors occur when the APOC CSV import procedure encounters invalid data or configuration.

## Common Causes

- File path not whitelisted in config
- CSV encoding mismatch
- Wrong delimiter configured
- File does not exist at specified path

## Common Error Messages

```
Failed to invoke procedure 'apoc.load.csv': File not whitelisted
```

## How to Fix It

### 1. Whitelist File Directory

```properties
# neo4j.conf
apoc.import.file.allowlist=/import/,/data/
apoc.import.file.enabled=true
```

### 2. Use Correct File URL

```cypher
CALL apoc.load.csv('file:///import/users.csv', {sep: ','})
YIELD map, lineNo
RETURN map, lineNo LIMIT 5;
```

### 3. Check File Encoding

```bash
file -bi /import/users.csv
```

## Examples

```cypher
CALL apoc.load.csv('file:///import/orders.csv', {header: true})
YIELD map
RETURN map.CustomerID, map.Total;
```
