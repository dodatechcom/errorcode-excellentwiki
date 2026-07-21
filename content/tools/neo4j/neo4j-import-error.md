---
title: "[Solution] Neo4j Import Error"
description: "Fix Neo4j import errors when using neo4j-admin import to load CSV data"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Import Error

Import errors occur when the neo4j-admin import tool encounters malformed data or configuration issues.

## Common Causes

- CSV delimiter mismatch between header and data
- Missing required ID field in import file
- Node ID references non-existent node
- Character encoding issues in CSV

## Common Error Messages

```
neo4j-admin import: Error in line X: Invalid CSV format
```

## How to Fix It

### 1. Validate CSV Format

```bash
head -5 /data/import/nodes.csv
```

### 2. Use Correct Delimiter

```bash
neo4j-admin database import full --nodes=Person=import/people.csv --delimiter=,
```

### 3. Check File Encoding

```bash
file -bi /data/import/nodes.csv
```

## Examples

```bash
neo4j-admin database import full --nodes=Movie=import/movies.csv --overwrite-destination
```
