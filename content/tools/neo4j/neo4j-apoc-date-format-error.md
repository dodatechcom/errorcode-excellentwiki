---
title: "[Solution] Neo4j APOC Date Format Error"
description: "Fix Neo4j APOC date formatting errors when temporal conversion patterns are invalid"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Date Format Error

APOC date format errors occur when invalid format patterns are passed to APOC temporal functions.

## Common Causes

- Format string contains unrecognized pattern letters
- Timezone ID not valid
- Date is null when formatting
- Pattern syntax mismatch between parse and format

## Common Error Messages

```
apoc.exception.InvalidArgumentException: Unknown format pattern
```

## How to Fix It

### 1. Use Standard Patterns

```cypher
RETURN apoc.date.format(timestamp(), 'ms', 'yyyy-MM-dd HH:mm:ss') AS formatted;
```

### 2. Parse with Correct Pattern

```cypher
RETURN apoc.date.parse('2024-01-15', 'ms', 'yyyy-MM-dd') AS timestamp;
```

### 3. Handle Null Dates

```cypher
MATCH (n:User)
RETURN n.name,
  CASE WHEN n.createdAt IS NOT NULL
    THEN apoc.date.format(n.createdAt, 'ms', 'dd/MM/yyyy')
    ELSE 'N/A'
  END AS createdDate;
```

## Examples

```cypher
RETURN apoc.temporal.format(datetime(), 'yyyy-MM-dd HH:mm:ss') AS now;
```
