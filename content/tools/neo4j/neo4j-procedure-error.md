---
title: "[Solution] Neo4j Procedure Error — How to Fix"
description: "Fix Neo4j stored procedure errors including creation failures, permission issues, and procedure execution problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Procedure Error

Procedure errors in Neo4j occur when custom procedures fail to load, execute, or when permissions prevent their use. Neo4j supports Java-based procedures and functions.

## Why It Happens

- The procedure JAR is not in the plugins directory
- The procedure class has compilation errors
- The procedure is not annotated correctly with @Procedure
- The security configuration restricts procedure execution
- The procedure throws an exception during execution
- The Neo4j version is incompatible with the procedure

## Common Error Messages

```
Neo.ClientError.Procedure.ProcedureNotFound:
There is no procedure with the name 'my.proc' registered
```

```
Neo.ClientError.Procedure.ProcedureCallFailed:
Failed to invoke procedure 'my.proc': java.lang.ClassNotFoundException
```

```
Neo.ClientError.Security.Forbidden:
Executing procedure 'my.proc' is not allowed for user 'reader'
```

```
Neo.TransientError.Procedure.ProcedureTimedOut:
Procedure execution timed out
```

## How to Fix It

### 1. Install Procedure Plugin

```bash
# Copy the procedure JAR to the plugins directory
cp my-procedure-1.0.jar /var/lib/neo4j/plugins/

# Set permissions
chmod 644 /var/lib/neo4j/plugins/my-procedure-1.0.jar
chown neo4j:neo4j /var/lib/neo4j/plugins/my-procedure-1.0.jar

# In neo4j.conf, whitelist the procedure
dbms.security.procedures.allowlist=my.*

# Restart Neo4j
sudo systemctl restart neo4j
```

### 2. Fix Procedure Security Configuration

```bash
# In neo4j.conf
dbms.security.procedures.unrestricted=my.*
dbms.security.procedures.allowlist=apoc.*,my.*

# Or restrict to specific users
# Use role-based access control in Neo4j Enterprise
```

### 3. Verify Procedure is Loaded

```cypher
// List all procedures
CALL dbms.procedures()
YIELD name, description
WHERE name CONTAINS 'my.'
RETURN name, description;

// Check for errors in the log
// tail -f /var/log/neo4j/neo4j.log | grep -i "procedure"
```

### 4. Debug Procedure Execution

```cypher
// Test procedure with minimal parameters
CALL my.procedure()
YIELD result
RETURN result;

// Check procedure signature
SHOW PROCEDURES
YIELD name, signature
WHERE name CONTAINS 'my.';
```

## Common Scenarios

- **Procedure not found after installation**: The JAR is in the wrong directory or Neo4j was not restarted.
- **Procedure fails with ClassNotFoundException**: The JAR is compiled for a different Java version.
- **Permission denied on procedure**: Add the procedure to the unrestricted list or grant appropriate role.

## Prevent It

- Test custom procedures on a staging server before deploying to production
- Ensure the procedure JAR is compiled for the same Java version as Neo4j
- Use `SHOW PROCEDURES` to verify all expected procedures are loaded

## Related Pages

- [Neo4j APOC Error](/tools/neo4j/neo4j-apoc-error)
- [Neo4j Plugins Error](/tools/neo4j/neo4j-plugins-error)
- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
