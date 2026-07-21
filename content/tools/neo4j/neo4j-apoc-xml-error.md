---
title: "[Solution] Neo4j APOC XML Error"
description: "Fix Neo4j APOC XML parsing errors when importing or processing XML data"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC XML Error

APOC XML errors occur when APOC XML parsing procedures encounter malformed XML input.

## Common Causes

- XML document contains invalid characters
- XML namespace not declared
- XML entity expansion attack
- File encoding mismatch

## Common Error Messages

```
apoc.exception.InvalidArgumentException: Unable to parse XML
```

## How to Fix It

### 1. Validate XML Structure

```bash
xmllint --noout /import/data.xml
```

### 2. Parse XML with APOC

```cypher
CALL apoc.load.xml('file:///import/data.xml', '/root/element')
YIELD value AS node
RETURN node;
```

### 3. Handle Namespaces

```cypher
CALL apoc.load.xml('file:///import/data.xml')
YIELD value
UNWIND value._children AS child
RETURN child;
```

## Examples

```cypher
CALL apoc.xml.parse('file:///import/catalog.xml')
YIELD value
RETURN value;
```
