---
title: "[Solution] Neo4j Procedure Not Found Error"
description: "Fix Neo4j procedure not found errors when calling APOC or custom procedures"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Procedure Not Found Error

Procedure not found errors occur when a Cypher query calls a stored procedure that is not registered.

## Common Causes

- APOC plugin not installed
- Procedure JAR not in plugins directory
- Neo4j restarted without loading plugin
- Custom procedure classpath misconfigured

## Common Error Messages

```
Neo.ClientError.Statement.ProcedureCallFailed: There is no procedure with the name 'apoc.load.json' registered
```

## How to Fix It

### 1. Check Installed Procedures

```cypher
CALL dbms.procedures() YIELD name WHERE name STARTS WITH 'apoc' RETURN name;
```

### 2. Install APOC

```bash
cp apoc-5.12.0.jar /var/lib/neo4j/plugins/
systemctl restart neo4j
```

### 3. Configure Plugin Path

```properties
# neo4j.conf
dbms.security.procedures.unrestricted=apoc.*
dbms.security.procedures.allowlist=apoc.*
```

## Examples

```cypher
RETURN apoc.version();
```
