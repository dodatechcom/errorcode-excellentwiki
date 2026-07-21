---
title: "[Solution] Neo4j APOC Config Error"
description: "Fix Neo4j APOC configuration errors when APOC settings are invalid or missing"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Config Error

APOC config errors occur when APOC configuration parameters are missing or invalid.

## Common Causes

- APOC config key not recognized
- Wrong value type for config parameter
- Config file syntax error
- APOC version mismatch with config options

## Common Error Messages

```
Neo.ClientError.Configuration.InvalidConfiguration: Unrecognized config option
```

## How to Fix It

### 1. Check APOC Config Keys

```properties
# neo4j.conf
apoc.import.file.enabled=true
apoc.import.file.allowlist=/import/
```

### 2. Remove Invalid Config

```bash
grep -n "apoc\." /etc/neo4j/neo4j.conf
```

### 3. Validate Config Syntax

```bash
neo4j-admin server memory-recommendation
```

## Examples

```properties
apoc.temporary.fulltext.enabled=true
apoc.uuid.enabled=true
```
