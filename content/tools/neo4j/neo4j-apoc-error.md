---
title: "[Solution] Neo4j APOC Plugin Error — How to Fix"
description: "Fix Neo4j APOC plugin errors including installation failures, procedure not found issues, and APOC function execution problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j APOC Plugin Error

APOC (Awesome Procedures On Cypher) is a collection of procedures and functions for Neo4j. Errors occur when APOC is not installed, misconfigured, or when procedure calls fail.

## Why It Happens

- APOC is not installed or not loaded by Neo4j
- The APOC version is incompatible with the Neo4j version
- The procedure is not whitelisted in the security configuration
- The APOC procedure requires parameters that are missing
- The APOC function encounters an error during execution
- APOC configuration in neo4j.conf is missing

## Common Error Messages

```
Neo.ClientError.Procedure.ProcedureNotFound:
There is no procedure with the name 'apoc.load.csv' registered
```

```
Neo.ClientError.Procedure.ProcedureCallFailed:
Failed to invoke procedure 'apoc.load.jdbc'
```

```
Neo.ClientError.Security.Forbidden:
Insufficient privileges to execute procedure 'apoc.*'
```

```
Neo.ClientError.Statement.ExternalResourceFailed:
Could not load CSV from URL
```

## How to Fix It

### 1. Install APOC Plugin

```bash
# Download the correct APOC version for your Neo4j version
# Neo4j 5.x: apoc-5.x.x-core.jar
# Neo4j 4.x: apoc-4.x.x-core.jar

# Copy to plugins directory
cp apoc-5.12.0-core.jar /var/lib/neo4j/plugins/

# Set APOC procedures as unrestricted in neo4j.conf
dbms.security.procedures.unrestricted=apoc.*

# Restart Neo4j
sudo systemctl restart neo4j
```

### 2. Fix APOC Configuration

```bash
# In neo4j.conf
dbms.security.procedures.unrestricted=apoc.*
dbms.security.procedures.allowlist=apoc.*

# For APOC extended (additional features)
dbms.security.procedures.unrestricted=apoc.*,apoc.ext.*
```

### 3. Verify APOC is Loaded

```cypher
// Check if APOC procedures are available
CALL dbms.procedures()
YIELD name
WHERE name STARTS WITH 'apoc.'
RETURN name ORDER BY name;

// Check APOC version
CALL apoc.help('load')
YIELD name, description
RETURN name, description LIMIT 10;
```

### 4. Fix APOC Procedure Errors

```cypher
// Common APOC procedures and correct syntax

// Load CSV
CALL apoc.load.csv('/path/to/file.csv')
YIELD map RETURN map;

// Load JDBC
CALL apoc.load.jdbc('jdbc:postgresql://host/db', 'SELECT * FROM users')
YIELD row RETURN row;

// Export to CSV
CALL apoc.export.csv.query('MATCH (n:Person) RETURN n.name', '/tmp/export.csv')
YIELD cypherInstructions, time, rows, data RETURN time, rows;
```

## Common Scenarios

- **APOC not found after installation**: Check the plugins directory and restart Neo4j.
- **APOC version mismatch**: Download the APOC version that matches your Neo4j version.
- **APOC procedures restricted by security**: Add `dbms.security.procedures.unrestricted=apoc.*` to neo4j.conf.

## Prevent It

- Always match APOC version with Neo4j version
- Test APOC procedures on staging before using in production
- Use `CALL dbms.procedures()` to verify available APOC functions

## Related Pages

- [Neo4j Procedure Error](/tools/neo4j/neo4j-procedure-error)
- [Neo4j Plugins Error](/tools/neo4j/neo4j-plugins-error)
- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
