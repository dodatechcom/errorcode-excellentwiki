---
title: "[Solution] GCP Cloud Spanner Interleaved Table Error"
description: "Fix Cloud Spanner interleaved table errors. Resolve schema conflicts, foreign key constraints, and parent-child table issues in Spanner."
cloud: ["gcp"]
error-types: ["cloud-error"]
severities: ["error"]
weight: 5
---

# GCP Cloud Spanner Interleaved Table Error

The Cloud Spanner Interleaved Table error occurs when table interleaving operations fail due to schema design issues or constraint violations.

## Common Causes

- Parent table is not created before the interleaved child table
- Primary key columns of parent are missing in child table
- Foreign key constraint references a non-existent table
- Interleave directive references wrong parent table name
- Cascade delete rules conflict with existing data

## How to Fix

### 1. Create parent table first
```sql
CREATE TABLE Authors (
  AuthorId INT64 NOT NULL,
  Name STRING(255),
) PRIMARY KEY (AuthorId);
```

### 2. Create interleaved child table
```sql
CREATE TABLE Books (
  AuthorId INT64 NOT NULL,
  BookId INT64 NOT NULL,
  Title STRING(255),
) PRIMARY KEY (AuthorId, BookId),
  INTERLEAVE IN PARENT Authors ON DELETE CASCADE;
```

### 3. Check schema status
```bash
gcloud spanner databases describe DATABASE_ID \
  --instance=INSTANCE_ID \
  --format="value(schema)"
```

### 4. Update schema
```bash
gcloud spanner databases ddl update DATABASE_ID \
  --instance=INSTANCE_ID \
  --ddl="ALTER TABLE Books ADD COLUMN Genre STRING(50)"
```

## Examples

### Three-level interleaving
```sql
CREATE TABLE Departments (
  DeptId INT64 NOT NULL,
) PRIMARY KEY (DeptId);

CREATE TABLE Employees (
  DeptId INT64 NOT NULL,
  EmpId INT64 NOT NULL,
) PRIMARY KEY (DeptId, EmpId),
  INTERLEAVE IN PARENT Departments ON DELETE CASCADE;
```

### Verify interleaving
```sql
SELECT TABLE_NAME, PARENT_TABLE_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE CONSTRAINT_TYPE = 'INTERLEAVE';
```

## Related Errors

- [GCP Spanner Error]({{< relref "/cloud/gcp/gcp-spanner-error" >}})
- [GCP Instance Spanner]({{< relref "/cloud/gcp/gcp-instance-(spanner)" >}})
