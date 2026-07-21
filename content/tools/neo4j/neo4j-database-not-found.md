---
title: "[Solution] Neo4j Database Not Found Error"
description: "How to fix Neo4j database not found errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Database name misspelled
- Database not created
- Multi-database not enabled

## How to Fix

List databases:

```cypher
SHOW DATABASES;
```

Create database:

```cypher
CREATE DATABASE mydb;
```

## Examples

```cypher
SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;
```
