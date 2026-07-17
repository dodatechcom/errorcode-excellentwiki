---
title: "Oracle - ORA-08004: sequence exceeds MAXVALUE"
description: "Oracle sequence has reached its maximum value and cannot generate new values"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

ORA-08004: sequence exceeds MAXVALUE occurs when a sequence has reached its defined maximum value and cannot generate a new number. This typically happens with sequences that have CYCLE disabled or when the MAXVALUE is too small for the workload.

## Common Causes

- Sequence MAXVALUE reached
- NOCYCLE option set on the sequence
- MAXVALUE set too low during creation
- Large batch inserts consuming sequence values rapidly
- Sequence not configured with sufficient range

## How to Fix

1. Check current sequence value:

```sql
SELECT sequence_name, last_number, max_value, increment_by
FROM user_sequences
WHERE sequence_name = 'MY_SEQ';
```

2. Alter the sequence to increase MAXVALUE:

```sql
ALTER SEQUENCE my_seq MAXVALUE 999999999;
```

3. Reset the sequence value:

```sql
ALTER SEQUENCE my_seq INCREMENT BY -1000;
SELECT my_seq.NEXTVAL FROM dual; -- adjust current value
ALTER SEQUENCE my_seq INCREMENT BY 1;
```

4. Recreate sequence with higher MAXVALUE:

```sql
DROP SEQUENCE my_seq;
CREATE SEQUENCE my_seq
  START WITH 1
  INCREMENT BY 1
  MAXVALUE 9999999999
  NOCYCLE
  CACHE 20;
```

5. Use CYCLE option for sequences that should wrap around:

```sql
ALTER SEQUENCE my_seq CYCLE MAXVALUE 999999;
```

6. Use identity columns (Oracle 12c+):

```sql
CREATE TABLE users (
  id NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
  name VARCHAR2(100)
);
```

## Examples

```sql
-- Error: ORA-08004: sequence MY_SEQ exceeds MAXVALUE
SELECT my_seq.NEXTVAL FROM dual;
-- ORA-08004: sequence MY_SEQ exceeds MAXVALUE and cannot be instantiated

-- Fix: increase MAXVALUE
ALTER SEQUENCE my_seq MAXVALUE 99999999;
SELECT my_seq.NEXTVAL FROM dual;
-- 10001
```

## Related Errors

- [Trigger error]({{< relref "/tools/oracle/oracle-trigger-error" >}})
- [Tablespace error]({{< relref "/tools/oracle/oracle-tablespace-error" >}})
