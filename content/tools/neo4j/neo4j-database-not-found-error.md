---
title: "[Solution] Neo4j Database Not Found Error"
description: "Fix Neo4j database not found errors when connecting to a named database that does not exist"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Database Not Found Error

Database not found errors occur when a query targets a named database that does not exist.

## Common Causes

- Database name typo in connection string
- Database was dropped during maintenance
- Multi-database setup with missing database
- Default database changed in configuration

## Common Error Messages

```
Neo.ClientError.Statement.DatabaseNotFound: Database 'analytics' does not exist
```

## How to Fix It

### 1. List Available Databases

```cypher
SHOW DATABASES;
```

### 2. Create Missing Database

```cypher
CREATE DATABASE analytics;
```

### 3. Use Correct Database Name

```python
from neo4j import GraphDatabase
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
with driver.session(database="analytics") as session:
    result = session.run("MATCH (n) RETURN count(n)")
```

## Examples

```cypher
SHOW DATABASES YIELD name;
```
