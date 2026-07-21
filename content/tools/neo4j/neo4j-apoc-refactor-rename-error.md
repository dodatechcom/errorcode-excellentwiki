---
title: "[Solution] Neo4j APOC Refactor Rename Error"
description: "Fix Neo4j APOC label and type rename errors when modifying schema"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Refactor Rename Error

APOC refactor rename errors occur when renaming labels or relationship types fails.

## Common Causes

- Renaming label that has unique constraint
- New label name contains invalid characters
- Rename operation timing out on large graph
- Old label has many indexes to rebuild

## Common Error Messages

```
Neo.ClientError.Schema.SchemaRuleAllocationFailed: Schema rule already exists
```

## How to Fix It

### 1. Rename Label

```cypher
CALL apoc.refactor.rename.label('OldLabel', 'NewLabel');
```

### 2. Rename Relationship Type

```cypher
CALL apoc.refactor.rename.type('OLD_REL', 'NEW_REL');
```

### 3. Rename with Label Filter

```cypher
CALL apoc.refactor.rename.label('OldLabel', 'NewLabel', ['OldLabel']);
```

## Examples

```cypher
CALL apoc.refactor.rename.type('FOLLOWS', 'CONNECTED_TO');
MATCH ()-[r:CONNECTED_TO]->() RETURN count(r);
```
