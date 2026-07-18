---
title: "[Solution] Neo4j Upgrade Error — How to Fix"
description: "Fix Neo4j upgrade errors including version migration failures, configuration changes, and compatibility issues between Neo4j versions"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Upgrade Error

Upgrade errors in Neo4j occur when migrating between major versions (e.g., 4.x to 5.x). These include configuration changes, syntax deprecations, and data format incompatibilities.

## Why It Happens

- Deprecated configuration settings are no longer supported
- The store format has changed between versions
- Cypher syntax from the old version is not supported in the new version
- Plugins are not compatible with the new version
- The Java version requirement has changed
- The backup format is not compatible between major versions

## Common Error Messages

```
Neo4j failed to start: Unrecognized setting 'dbms.xxx'
```

```
ERROR: Incompatible store version
```

```
Neo.ClientError.Statement.SyntaxError: Deprecated Cypher syntax
```

```
ERROR: Neo4j requires Java 17 or higher
```

## How to Fix It

### 1. Use neo4j-admin Database Migrate

```bash
# Stop Neo4j
sudo systemctl stop neo4j

# Migrate the database
neo4j-admin database migrate neo4j --from-version=4.4 --to-version=5.0

# Start Neo4j
sudo systemctl start neo4j
```

### 2. Fix Configuration Changes

```bash
# Common renames from 4.x to 5.x:
# dbms.connectors.default_listen_address -> server.bolt.listen_address
# dbms.connector.bolt.type -> (removed)
# dbms.connector.http.enabled -> server.http.enabled

# Check for deprecated settings
grep -r "deprecated\|unrecognized" /var/log/neo4j/neo4j.log
```

### 3. Fix Cypher Syntax Changes

```cypher
// Neo4j 4.x deprecated syntax
// CREATE INDEX ON :Person(name)  -- removed in 5.x

// Neo4j 5.x syntax
CREATE INDEX FOR (n:Person) ON (n.name);

// Remove unsigned integer syntax
// REMOVE: CREATE (n:Counter {val: 42UL});
// USE: CREATE (n:Counter {val: 42});
```

### 4. Fix Plugin Compatibility

```bash
# Check which plugins need updating
ls /var/lib/neo4j/plugins/

# Download compatible versions:
# - APOC 5.x for Neo4j 5.x
# - GDS 2.x for Neo4j 5.x

# Remove old plugin versions
rm /var/lib/neo4j/plugins/apoc-4.x.x-core.jar
cp apoc-5.x.x-core.jar /var/lib/neo4j/plugins/
```

## Common Scenarios

- **Upgrade fails with config error**: Update deprecated settings in neo4j.conf.
- **Store format incompatible**: Use `neo4j-admin database migrate` before starting.
- **Cypher queries break**: Update deprecated syntax for the new version.

## Prevent It

- Read the Neo4j upgrade guide for the target version before upgrading
- Back up the database before any upgrade attempt
- Test the upgrade on a staging server with production data

## Related Pages

- [Neo4j Kernel Error](/tools/neo4j/neo4j-kernel-error)
- [Neo4j Config Error](/tools/neo4j/neo4j-config-error)
- [Neo4j Backup Error](/tools/neo4j/neo4j-backup-error)
