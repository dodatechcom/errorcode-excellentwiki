---
title: "Oracle - ORA-00942: table or view does not exist"
description: "Oracle query references a table or view that does not exist in the current schema or database"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

ORA-00942: table or view does not exist occurs when a SQL statement references a table, view, or synonym that cannot be found. This can be caused by missing schema qualification, typos, or insufficient privileges.

## Common Causes

- Table or view does not exist in the current schema
- Missing schema prefix (e.g., `HR.employees` vs `employees`)
- Table was dropped or renamed
- Synonym points to non-existent object
- Missing SELECT privilege on the table

## How to Fix

1. Verify the table exists:

```sql
SELECT table_name FROM user_tables WHERE table_name = 'EMPLOYEES';
-- Or check all schemas
SELECT owner, table_name FROM all_tables WHERE table_name = 'EMPLOYEES';
```

2. Use fully qualified table names:

```sql
-- Instead of
SELECT * FROM employees;

-- Use
SELECT * FROM hr.employees;
```

3. Check for typos in table/view names:

```sql
-- Case-sensitive names must be quoted
SELECT * FROM "MyTable";
```

4. Check synonyms:

```sql
SELECT synonym_name, table_owner, table_name
FROM user_synonyms
WHERE synonym_name = 'EMPLOYEES';
```

5. Verify object privileges:

```sql
SELECT grantee, table_name, privilege
FROM user_tab_privs
WHERE table_name = 'EMPLOYEES';
```

6. Create missing table or synonym:

```sql
-- Create synonym
CREATE PUBLIC SYNONYM employees FOR hr.employees;

-- Or grant access
GRANT SELECT ON hr.employees TO myuser;
```

## Examples

```sql
-- Error: ORA-00942: table or view does not exist
SELECT * FROM employees;
-- If table is in HR schema

-- Fix: qualify with schema
SELECT * FROM hr.employees;
```

```sql
-- Error can also indicate insufficient privileges
SELECT * FROM v$session;
-- ORA-00942: table or view does not exist
-- (actually means no SELECT on v$session)

-- Fix: grant access
GRANT SELECT ON v_$session TO myuser;
```

## Related Errors

- [Permission error]({{< relref "/tools/oracle/oracle-permission-error" >}})
- [Partition error]({{< relref "/tools/oracle/oracle-partition-error" >}})
