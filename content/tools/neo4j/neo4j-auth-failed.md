---
title: "[Solution] Neo4j Authentication Failed Error"
description: "How to fix Neo4j authentication failures"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Wrong username or password
- Default password not changed
- User locked after failed attempts

## How to Fix

Reset password:

```bash
neo4j-admin dbms set-initial-password newpassword
sudo systemctl restart neo4j
```

## Examples

```bash
neo4j-admin dbms set-initial-password mypassword
sudo systemctl restart neo4j
cypher-shell -u neo4j -p mypassword
```
