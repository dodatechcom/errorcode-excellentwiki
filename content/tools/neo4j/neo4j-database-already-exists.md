---
title: "[Solution] Neo4j Database Already Exists Error"
description: "How to fix Neo4j database already exists errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Database creation called twice
- Naming collision

## How to Fix

Use IF NOT EXISTS:

```cypher
CREATE DATABASE IF NOT EXISTS mydb;
```

## Examples

```cypher
SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS mydb;
```
