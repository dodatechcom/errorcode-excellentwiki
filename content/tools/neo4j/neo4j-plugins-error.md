---
title: "[Solution] Neo4j Plugins Error — How to Fix"
description: "Fix Neo4j plugin errors including installation failures, version compatibility issues, and plugin configuration problems"
tools: ["neo4j"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# Neo4j Plugins Error

Plugin errors in Neo4j occur when installing, loading, or using Neo4j plugins such as APOC, GDS (Graph Data Science), or custom plugins. These include version conflicts, configuration issues, and runtime errors.

## Why It Happens

- The plugin JAR is not in the correct plugins directory
- The plugin version is incompatible with the Neo4j version
- The plugin requires dependencies that are missing
- The security configuration restricts the plugin
- The plugin crashes during initialization
- The plugin directory has wrong permissions

## Common Error Messages

```
Neo.ClientError.Procedure.ProcedureNotFound:
There is no procedure with the name 'gds.pageRank' registered
```

```
ERROR: Failed to load plugin: java.lang.ClassNotFoundException
```

```
ERROR: Plugin initialization failed
```

```
Neo.ClientError.Security.Forbidden:
Insufficient privileges to execute procedure 'gds.*'
```

## How to Fix It

### 1. Install Plugins Correctly

```bash
# APOC plugin
cp apoc-5.12.0-core.jar /var/lib/neo4j/plugins/

# GDS plugin
cp neo4j-graph-data-science-2.6.0.jar /var/lib/neo4j/plugins/

# Set permissions
chown neo4j:neo4j /var/lib/neo4j/plugins/*.jar
chmod 644 /var/lib/neo4j/plugins/*.jar
```

### 2. Configure Plugin Security

```bash
# In neo4j.conf
dbms.security.procedures.unrestricted=apoc.*,gds.*
dbms.security.procedures.allowlist=apoc.*,gds.*
```

### 3. Fix Version Compatibility

```bash
# Check Neo4j version
neo4j --version

# Download compatible plugin versions
# APOC version must match Neo4j major version
# GDS version must match Neo4j major version

# Verify plugins are loaded
cypher-shell -u neo4j -p password "CALL dbms.procedures() YIELD name WHERE name STARTS WITH 'gds.' RETURN count(name);"
```

### 4. Debug Plugin Issues

```bash
# Check Neo4j logs for plugin errors
grep -i "plugin\|procedure\|apoc\|gds" /var/log/neo4j/neo4j.log

# Check if plugin directory is correct
ls -la /var/lib/neo4j/plugins/
```

## Common Scenarios

- **Plugin not found after installation**: Ensure the JAR is in the correct directory and Neo4j was restarted.
- **APOC version mismatch**: Download the APOC version that matches your Neo4j version.
- **GDS procedures restricted**: Add `gds.*` to the unrestricted list in neo4j.conf.

## Prevent It

- Always match plugin versions with the Neo4j version
- Test plugins on staging before deploying to production
- Keep plugins in a version-controlled directory

## Related Pages

- [Neo4j APOC Error](/tools/neo4j/neo4j-apoc-error)
- [Neo4j Procedure Error](/tools/neo4j/neo4j-procedure-error)
- [Neo4j Query Error](/tools/neo4j/neo4j-query-error)
