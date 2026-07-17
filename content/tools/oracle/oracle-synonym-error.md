---
title: "Oracle Synonym Error"
description: "Oracle synonym fails to resolve or compile."
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oracle", "synonym", "alias", "object", "reference"]
weight: 5
---

# Oracle Synonym Error

An Oracle synonym error occurs when a synonym fails to resolve to its base object. Synonyms are aliases for database objects.

## Common Causes

- Base object does not exist or has been dropped
- Synonym points to wrong schema
- Synonym is not public and user lacks access
- Object name changed after synonym creation

## How to Fix

### Check Synonym Status

```sql
SELECT synonym_name, table_owner, table_name
FROM user_synonyms;
```

### Check Public Synonyms

```sql
SELECT synonym_name, table_owner, table_name
FROM dba_synonyms
WHERE owner = 'PUBLIC';
```

### Create Synonym

```sql
-- Private synonym
CREATE SYNONYM mytable FOR schema.table_name;

-- Public synonym
CREATE PUBLIC SYNONYM mytable FOR schema.table_name;
```

### Drop and Recreate Synonym

```sql
DROP SYNONYM mytable;
CREATE SYNONYM mytable FOR new_schema.new_table;
```

### Check Object Exists

```sql
SELECT object_name, object_type, owner
FROM all_objects
WHERE object_name = 'TABLE_NAME';
```

## Examples

```sql
CREATE SYNONYM emp FOR hr.employees;
SELECT * FROM emp;
-- Works if hr.employees exists

DROP TABLE hr.employees;
SELECT * FROM emp;
-- ORA-00942: table or view does not exist
```

## Related Errors

- [View Error]({{< relref "/tools/oracle/view-error" >}}) — view issues
- [Permission Error]({{< relref "/tools/oracle/permission-error" >}}) — permission denied
