---
title: "[Solution] Neo4j Shell Error — How to Fix"
description: "Fix Neo4j shell errors including cypher-shell connection issues, neo4j-shell deprecation, and interactive shell problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Shell Error

Shell errors in Neo4j occur when using `cypher-shell` or the deprecated `neo4j-shell` command-line tools. These include connection issues, authentication problems, and command execution failures.

## Why It Happens

- The shell cannot connect to the Neo4j server
- Authentication credentials are incorrect
- The shell is using the wrong Bolt or HTTP port
- The cypher-shell version does not match the Neo4j version
- The query is too large for the shell buffer
- The shell encounters a network timeout

## Common Error Messages

```
Failed to connect to neo4j at bolt://localhost:7687
```

```
Neo.ClientError.Security.Unauthorized: The client is unauthorized
```

```
Error: Unable to establish connection to bolt://localhost:7687
```

```
cypher-shell: error: Could not connect to server
```

## How to Fix It

### 1. Fix cypher-shell Connection

```bash
# Connect with explicit host and credentials
cypher-shell -u neo4j -p password bolt://localhost:7687

# Connect via HTTP
cypher-shell -u neo4j -p password http://localhost:7474

# Run a query non-interactively
cypher-shell -u neo4j -p password "MATCH (n) RETURN count(n);"
```

### 2. Fix Authentication Issues

```bash
# Reset password
sudo systemctl stop neo4j
neo4j-admin dbms set-initial-password newpassword
sudo systemctl start neo4j

# Test connection
cypher-shell -u neo4j -p newpassword "RETURN 1;"
```

### 3. Fix cypher-shell Version Mismatch

```bash
# Check cypher-shell version
cypher-shell --version

# Check Neo4j version
neo4j --version

# Ensure versions are compatible
# cypher-shell should match the Neo4j version
```

### 4. Fix Network/Timeout Issues

```bash
# Increase timeout
cypher-shell -u neo4j -p password --connection-timeout 30s bolt://localhost:7687

# Check network connectivity
nc -zv localhost 7687
nc -zv localhost 7474
```

## Common Scenarios

- **cypher-shell cannot connect**: Ensure Neo4j is running and the port is correct.
- **Password authentication fails**: Reset the password using `neo4j-admin`.
- **cypher-shell hangs**: Check network connectivity and increase timeout.

## Prevent It

- Use cypher-shell instead of the deprecated neo4j-shell
- Store credentials securely (environment variables, not command line)
- Test shell connectivity as part of deployment validation

## Related Pages

- [Neo4j Connection Error](/tools/neo4j/neo4j-connection-error)
- [Neo4j Auth Error](/tools/neo4j/neo4j-auth-error)
- [Neo4j Bolt Error](/tools/neo4j/neo4j-bolt-error)
