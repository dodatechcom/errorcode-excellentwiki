---
title: "[Solution] YugabyteDB Enum Error — How to Fix"
description: "Fix YugabyteDB enum errors by resolving enum type failures, fixing enum value issues, and handling enum modification problems in distributed tables"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Enum Error

YugabyteDB enum errors occur when creating, modifying, or using enum types fails due to value conflicts, modification restrictions, or distributed execution issues.

## Why It Happens

- Enum value already exists when adding new value
- Enum is used in a column that already has invalid data
- Enum type is referenced by multiple tables
- Adding enum value fails on distributed tables
- Enum value is used in a CHECK constraint
- Enum type name conflicts with an existing type

## Common Error Messages

```
ERROR: enum value already exists
```

```
ERROR: invalid input value for enum
```

```
ERROR: cannot alter enum type
```

```
ERROR: enum type does not exist
```

## How to Fix It

### 1. Create Enum Type

```sql
-- Create enum type
CREATE TYPE status_type AS ENUM ('active', 'inactive', 'pending');

-- Use enum in table
CREATE TABLE my_table (
  id INT PRIMARY KEY,
  status status_type DEFAULT 'pending'
);
```

### 2. Add Enum Values

```sql
-- Add new enum value
ALTER TYPE status_type ADD VALUE 'archived';

-- Add value before existing value
ALTER TYPE status_type ADD VALUE 'suspended' BEFORE 'inactive';
```

### 3. Fix Invalid Enum Values

```sql
-- Find rows with invalid enum values
SELECT * FROM my_table
WHERE status::TEXT NOT IN ('active', 'inactive', 'pending');

-- Update invalid values
UPDATE my_table SET status = 'pending'
WHERE status::TEXT NOT IN ('active', 'inactive', 'pending');
```

### 4. Handle Enum on Distributed Tables

```sql
-- Create enum type on master node first
CREATE TYPE device_status AS ENUM ('online', 'offline');

-- Use in distributed table
CREATE TABLE devices (
  id INT PRIMARY KEY,
  status device_status
) SPLIT INTO 4 TABLETS;
```

## Common Scenarios

- **Cannot add enum value**: Ensure the value does not already exist.
- **Invalid enum value in column**: Update the column to a valid enum value.
- **Enum modification fails on distributed table**: Create the enum type on the master node first.

## Prevent It

- Plan enum values carefully before creating the type
- Use CHECK constraints for flexible value sets
- Test enum operations in staging before production

## Related Pages

- [YugabyteDB Schema Error](/tools/yugabyte/yugabyte-schema-error)
- [YugabyteDB DDL Error](/tools/yugabyte/yugabyte-ddl-error)
- [YugabyteDB Table Error](/tools/yugabyte/yugabyte-tablet-error)
