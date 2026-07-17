---
title: "Oracle Sequence Error"
description: "Oracle sequence encounters errors during value generation."
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# Oracle Sequence Error

An Oracle sequence error occurs when a sequence fails to generate the next value. Sequences are used for auto-incrementing primary keys in Oracle.

## Common Causes

- Sequence exhausted (reached MAXVALUE)
- Sequence cache issue
- Sequence does not exist
- ORDER/NOCORDER mismatch in RAC

## How to Fix

### Check Sequence Status

```sql
SELECT sequence_name, last_number, increment_by, max_value
FROM user_sequences;
```

### Get Next Value

```sql
SELECT myseq.NEXTVAL FROM dual;
```

### Reset Sequence

```sql
ALTER SEQUENCE myseq INCREMENT BY -100;
SELECT myseq.NEXTVAL FROM dual;  -- Go back
ALTER SEQUENCE myseq INCREMENT BY 1;
```

### Create New Sequence

```sql
CREATE SEQUENCE myseq
  START WITH 1
  INCREMENT BY 1
  NOCACHE
  NOCYCLE;
```

### Fix Cache Issues

```sql
ALTER SEQUENCE myseq CACHE 20;
```

### Handle MAXVALUE

```sql
-- Check current value
SELECT myseq.CURRVAL FROM dual;

-- Reset if exhausted
ALTER SEQUENCE myseq RESTART START WITH 1;
```

## Examples

```sql
INSERT INTO users (id, name) VALUES (myseq.NEXTVAL, 'Alice');
ORA-08004: sequence MYSEQ.NEXTVAL exceeds MAXVALUE

-- Fix: alter sequence
ALTER SEQUENCE myseq MAXVALUE 999999999;
```

## Related Errors

- [Constraint Error]({{< relref "/tools/oracle/ora-00001" >}}) — unique constraint violation
- [Tablespace Error]({{< relref "/tools/oracle/oracle-tablespace-error" >}}) — tablespace issues
