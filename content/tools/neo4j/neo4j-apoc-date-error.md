---
title: "[Solution] Neo4j APOC Date Error"
description: "Fix Neo4j APOC date parsing and formatting errors when working with temporal values"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Date Error

APOC date errors occur when APOC temporal functions receive invalid date strings or formats.

## Common Causes

- Date string format does not match specified pattern
- Invalid date values (month 13, day 32)
- Timezone not recognized
- Null date passed to formatting function

## Common Error Messages

```
apoc.exception.DateTimeException: Invalid date format
```

## How to Fix It

### 1. Use Correct Date Format

```cypher
RETURN apoc.temporal.format(date('2024-01-15'), 'dd/MM/yyyy') AS formatted;
```

### 2. Parse Date with Pattern

```cypher
RETURN apoc.date.parse('15/01/2024', 'ms', 'dd/MM/yyyy') AS timestamp;
```

### 3. Convert Between Formats

```cypher
RETURN date('2024-01-15') AS isoDate,
       datetime('2024-01-15T10:30:00Z') AS fullDatetime;
```

## Examples

```cypher
RETURN apoc.date.format(timestamp(), 'ms', 'yyyy-MM-dd HH:mm:ss') AS now;
```
