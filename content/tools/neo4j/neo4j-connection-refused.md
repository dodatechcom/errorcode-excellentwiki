---
title: "[Solution] Neo4j Connection Refused Error"
description: "How to fix Neo4j connection refused errors"
tools: ["neo4j"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Neo4j not running
- Wrong port (default 7687 Bolt, 7474 HTTP)
- Bind address restricting connections
- Firewall blocking ports

## How to Fix

Check status:

```bash
sudo systemctl status neo4j
neo4j status
```

Start Neo4j:

```bash
sudo systemctl start neo4j
```

## Examples

```bash
neo4j status
sudo systemctl start neo4j
ss -tlnp | grep -E '(7687|7474)'
```
