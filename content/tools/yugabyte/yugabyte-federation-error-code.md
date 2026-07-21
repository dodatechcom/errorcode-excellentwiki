---
title: "YugabyteDB Federation Error Code"
description: "Federation error with specific code"
tools:
  - yugabyte
error-types: ["tool-error"]
severities: ["error"]
---
## Error Description
Federation returning specific error code.

## Common Causes
- Remote table not found
- Connection to remote DB failed
- Schema mismatch

## How to Fix
```sql
-- Check foreign tables
SELECT * FROM information_schema.foreign_tables;

-- Create foreign table
CREATE FOREIGN TABLE remote_table (id INT, val TEXT) SERVER myserver OPTIONS (table_name 'remotetable');
```

## Examples
```sql
-- Check foreign data wrapper
SELECT * FROM information_schema.foreign_data_wrappers;
-- Create server
CREATE SERVER myserver FOREIGN DATA WRAPPER postgresql OPTIONS (host 'remote-host', port '5432', dbname 'remotedb');
```

