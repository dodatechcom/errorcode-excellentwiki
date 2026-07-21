---
title: "[Solution] Neo4j APOC Temporal Error"
description: "Fix Neo4j APOC temporal calculation errors when working with dates and times"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Temporal Error

APOC temporal errors occur when APOC time calculation functions receive invalid temporal input.

## Common Causes

- Subtracting incompatible temporal types
- Temporal unit not recognized
- Duration overflow from large calculations
- Null temporal value in calculation

## Common Error Messages

```
apoc.exception.InvalidArgumentException: Cannot subtract temporal values
```

## How to Fix It

### 1. Use Compatible Temporal Types

```cypher
RETURN duration.between(date('2024-01-01'), date('2024-12-31')) AS diff;
```

### 2. Calculate Date Differences

```cypher
MATCH (n:User)
WHERE n.createdAt IS NOT NULL
RETURN n.name,
  duration.between(n.createdAt, datetime()).days AS daysSinceCreation;
```

### 3. Add Duration to Date

```cypher
RETURN date('2024-01-01') + duration({days: 30}) AS oneMonthLater;
```

## Examples

```cypher
RETURN duration({hours: 2, minutes: 30}) AS timeDuration;
```
