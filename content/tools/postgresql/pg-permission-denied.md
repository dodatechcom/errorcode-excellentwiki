---
title: "[Solution] PostgreSQL Permission Denied for Table - Fix Access Privileges"
description: "Fix PostgreSQL permission denied errors by granting table privileges, fixing ownership, and setting default privileges for future objects"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# PostgreSQL Permission Denied for Table

This error occurs when a database role attempts to perform an operation on a table (or other object) without the required privilege. PostgreSQL enforces a strict privilege model where no role can access another role's objects unless explicitly granted.

## What This Error Means

PostgreSQL returns this error when your role lacks the necessary privilege:

```
ERROR: permission denied for table mytable
```

The error message specifies the object type (table, sequence, function, schema) and the object name. In PostgreSQL, object privileges are separate from login privileges -- having `LOGIN` does not grant access to any user-created objects.

Privileges include `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `TRUNCATE`, `REFERENCES`, and `TRIGGER` for tables, plus `USAGE` and `CREATE` for schemas.

## Why It Happens

- The table was created by a different role and no privileges were granted
- A migration creates objects as `postgres` or `root` but the application connects as a different user
- `REVOKE` was run and removed expected privileges
- Default privileges were not set, so new objects are created with no public access
- The role needs `USAGE` on a schema before it can access objects within it
- Sequence ownership is required for `nextval()` -- `SELECT` alone is not enough

## How to Fix It

### 1. Grant Privileges on the Table

```sql
-- Grant SELECT to a specific role
GRANT SELECT ON mytable TO myuser;

-- Grant all privileges
GRANT ALL PRIVILEGES ON mytable TO myuser;

-- Grant specific privileges
GRANT SELECT, INSERT, UPDATE ON mytable TO myuser;
```

### 2. Grant Usage on the Schema

```sql
-- The role needs schema access before it can see tables
GRANT USAGE ON SCHEMA public TO myuser;

-- Grant CREATE so the role can create objects
GRANT CREATE ON SCHEMA public TO myuser;
```

### 3. Set Default Privileges for Future Objects

```sql
-- Grant privileges automatically on future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public
    GRANT SELECT ON TABLES TO myuser;

-- For all new tables created by the current role
ALTER DEFAULT PRIVILEGES
    GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO myuser;
```

### 4. Fix Sequence Permissions

```sql
-- The role needs USAGE on the sequence to use nextval()
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO myuser;

-- Set default for future sequences
ALTER DEFAULT PRIVILEGES IN SCHEMA public
    GRANT USAGE ON SEQUENCES TO myuser;
```

### 5. Transfer Ownership

```sql
-- Change the table owner to the role that needs full access
ALTER TABLE mytable OWNER TO myuser;

-- Transfer ownership of all tables in a schema
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN SELECT tablename FROM pg_tables WHERE schemaname = 'public' LOOP
        EXECUTE 'ALTER TABLE public.' || quote_ident(r.tablename) || ' OWNER TO myuser';
    END LOOP;
END $$;
```

## Common Mistakes

- Running migrations as `root` or `postgres` without considering which role the application uses
- Granting privileges on tables but forgetting the schema `USAGE` privilege
- Not setting `ALTER DEFAULT PRIVILEGES`, so every new table requires manual grants
- Assuming `PUBLIC` grants exist by default -- they do not in newer PostgreSQL versions
- Forgetting that `TRUNCATE` requires a separate privilege from `DELETE`

## Related Pages

- [PostgreSQL Role Does Not Exist](/tools/postgresql/pg-role-does-not-exist)
- [PostgreSQL Duplicate Key](/tools/postgresql/pg-duplicate-key)
- [PostgreSQL Foreign Key Violation](/tools/mysql/mysql-foreign-key-constraint)
- [MySQL Access Denied](/tools/mysql/mysql-access-denied)
