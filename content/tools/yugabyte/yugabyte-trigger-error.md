---
title: "[Solution] YugabyteDB Trigger Error — How to Fix"
description: "Fix YugabyteDB trigger errors by resolving trigger creation failures, fixing AFTER INSERT triggers, and handling trigger function issues"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Trigger Error

YugabyteDB trigger errors occur when triggers on tables fail to create, execute, or function correctly due to function issues, timing problems, or distributed execution limitations.

## Why It Happens

- Trigger function is not IMMUTABLE
- Trigger references a function that does not exist
- BEFORE INSERT trigger modifies the primary key
- Trigger conflicts with unique constraint enforcement
- Trigger function uses session-specific state that is not replicated
- Trigger on a distributed table has cross-tablet dependencies

## Common Error Messages

```
ERROR: trigger function must return NULL or NEW
```

```
ERROR: function does not exist
```

```
ERROR: trigger execution failed
```

```
ERROR: cannot modify primary key in trigger
```

## How to Fix It

### 1. Create Compatible Triggers

```sql
-- Create IMMUTABLE trigger function
CREATE OR REPLACE FUNCTION set_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create BEFORE UPDATE trigger
CREATE TRIGGER update_timestamp
  BEFORE UPDATE ON my_table
  FOR EACH ROW
  EXECUTE FUNCTION set_timestamp();
```

### 2. Fix Common Trigger Issues

```sql
-- WRONG: trigger tries to modify primary key
CREATE OR REPLACE FUNCTION fix_id()
RETURNS TRIGGER AS $$
BEGIN
  NEW.id = 1;  -- Will fail
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- CORRECT: trigger modifies non-key columns only
CREATE OR REPLACE FUNCTION set_defaults()
RETURNS TRIGGER AS $$
BEGIN
  NEW.status = 'pending';
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### 3. Handle Trigger Errors

```sql
-- Use EXCEPTION block in trigger function
CREATE OR REPLACE FUNCTION safe_trigger()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
EXCEPTION WHEN OTHERS THEN
  RAISE NOTICE 'Trigger error: %', SQLERRM;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### 4. Test Triggers

```sql
-- Insert test data
INSERT INTO my_table (name, value) VALUES ('test', 100);

-- Verify trigger fired
SELECT * FROM my_table WHERE name = 'test';
```

## Common Scenarios

- **Trigger fails on INSERT**: Ensure the function returns NEW or NULL.
- **Trigger function not found**: Create the function before creating the trigger.
- **Trigger modifies primary key**: Only modify non-key columns in triggers.

## Prevent It

- Always use IMMUTABLE functions in triggers
- Test triggers with various data scenarios
- Avoid modifying primary key columns in triggers

## Related Pages

- [YugabyteDB DDL Error](/tools/yugabyte/yugabyte-ddl-error)
- [YugabyteDB Table Error](/tools/yugabyte/yugabyte-tablet-error)
- [YugabyteDB Schema Error](/tools/yugabyte/yugabyte-schema-error)
