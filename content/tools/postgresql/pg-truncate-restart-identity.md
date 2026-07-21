---
title: "[Solution] PostgreSQL TRUNCATE RESTART IDENTITY Error"
description: "Fix PostgreSQL TRUNCATE RESTART IDENTITY errors. Resolve sequence reset issues during table truncation."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL TRUNCATE RESTART IDENTITY Error

ERROR: must be owner of table / permission denied for TRUNCATE

This error occurs when attempting to TRUNCATE a table with the RESTART IDENTITY option without the required privileges on the underlying sequence.

## Common Causes

- User lacks TRUNCATE privilege on the table
- User is not the owner of the sequence attached to the SERIAL column
- Foreign key constraints prevent TRUNCATE from completing
- TRUNCATE requires CASCADE when referenced by other tables

## How to Fix

1. Grant TRUNCATE privilege to the user:

```sql
GRANT TRUNCATE ON my_table TO app_user;
```

2. Grant usage and update on sequences:

```sql
GRANT USAGE, UPDATE ON SEQUENCE my_table_id_seq TO app_user;
```

3. Use CASCADE to handle foreign key dependencies:

```sql
TRUNCATE TABLE log_entries RESTART IDENTITY CASCADE;
```

4. Drop foreign key constraints temporarily:

```sql
ALTER TABLE child_table DROP CONSTRAINT fk_parent;
TRUNCATE TABLE parent_table RESTART IDENTITY;
ALTER TABLE child_table ADD CONSTRAINT fk_parent
  FOREIGN KEY (parent_id) REFERENCES parent_table(id);
```

## Examples

```sql
-- Check sequence ownership
SELECT sequencename, sequenceowner
FROM pg_sequences
WHERE schemaname = 'public';
```
