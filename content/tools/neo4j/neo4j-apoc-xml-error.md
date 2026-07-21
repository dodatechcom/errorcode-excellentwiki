---
title: "[Solution] Neo4j APOC XML Error"
description: "How to fix Neo4j APOC XML processing errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- XML malformed
- XPath expression wrong
- Namespace not registered

## How to Fix

```cypher
CALL apoc.load.xml('file:///data.xml') YIELD doc RETURN doc
```

## Examples

```cypher
RETURN apoc.xml.parse('<root><item id="1"/>')
```
