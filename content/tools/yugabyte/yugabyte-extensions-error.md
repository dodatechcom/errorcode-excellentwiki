---
title: "[Solution] YugabyteDB Extensions Error — How to Fix"
description: "Fix YugabyteDB extension errors by resolving CREATE EXTENSION failures, fixing missing extensions, and handling extension compatibility issues"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Extensions Error

YugabyteDB extension errors occur when creating or using PostgreSQL extensions fails because the extension is not installed, incompatible, or has missing dependencies.

## Why It Happens

- Extension is not installed in the YugabyteDB installation
- Extension version is incompatible with YugabyteDB version
- Extension depends on shared libraries not present
- Extension is created in the wrong database
- Extension conflicts with another loaded extension
- Extension SQL files are missing or corrupted

## Common Error Messages

```
ERROR: extension "extension_name" does not exist
```

```
ERROR: could not open extension control file
```

```
ERROR: extension version mismatch
```

```
ERROR: missing dependency for extension
```

## How to Fix It

### 1. Check Available Extensions

```sql
-- List installed extensions
SELECT * FROM pg_extension;

-- List available extensions
SELECT * FROM pg_available_extensions;
```

### 2. Install Required Extension

```sql
-- Create extension
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Create extension with specific version
CREATE EXTENSION IF NOT EXISTS pg_trgm VERSION '1.5';

-- Check extension status
SELECT extname, extversion FROM pg_extension;
```

### 3. Fix Extension Compatibility

```sql
-- Update extension to latest version
ALTER EXTENSION pgcrypto UPDATE;

-- Check compatible versions
SELECT * FROM pg_available_extensions
WHERE name = 'pgcrypto';
```

### 4. Handle Missing Extensions

```bash
# Check if extension files exist
ls /opt/yugabyte/postgres/share/extension/

# Install missing extension
sudo apt-get install postgresql-14-pgcrypto

# Copy extension files to YugabyteDB
cp /usr/share/postgresql/14/extension/pgcrypto* \
  /opt/yugabyte/postgres/share/extension/
```

## Common Scenarios

- **Extension not found**: Install the extension or check if it is available for YugabyteDB.
- **Extension version mismatch**: Update the extension or install the correct version.
- **Extension missing dependencies**: Install the required shared libraries.

## Prevent It

- Test extension installation in staging before production
- Check extension compatibility with YugabyteDB version
- Keep extensions updated to the latest supported version

## Related Pages

- [YugabyteDB Config Error](/tools/yugabyte/yugabyte-config-error)
- [YugabyteDB Schema Error](/tools/yugabyte/yugabyte-schema-error)
- [YugabyteDB DDL Error](/tools/yugabyte/yugabyte-ddl-error)
