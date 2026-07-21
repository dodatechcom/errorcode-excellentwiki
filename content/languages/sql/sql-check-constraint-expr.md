---
title: "SQL CHECK Constraint Expression Error"
description: "Fix SQL CHECK constraint errors when constraint expressions use syntax not supported by the database engine."
languages: ["sql"]
error-types: ["constraint-error"]
severities: ["error"]
weight: 5
---

## Common Causes

- CHECK constraint uses functions not supported in constraints
- Constraint references other tables (not allowed in standard SQL)
- Circular dependency between CHECK constraints
- CHECK constraint evaluates to NULL instead of TRUE/FALSE
- Adding CHECK constraint when existing data violates it

## How to Fix

```sql
-- WRONG: CHECK with subquery (not allowed)
ALTER TABLE orders ADD CONSTRAINT chk_total
    CHECK (total > (SELECT AVG(total) FROM orders));
-- ERROR: subqueries not allowed in CHECK

-- CORRECT: Use trigger or application logic
CREATE TRIGGER chk_order_total
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE avg_val DECIMAL;
    SELECT AVG(total) INTO avg_val FROM orders;
    IF NEW.total <= avg_val THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Total must be above average';
    END IF;
END;
```

```sql
-- WRONG: CHECK with existing violating data
ALTER TABLE products ADD CONSTRAINT chk_price
    CHECK (price > 0);
-- ERROR: some products have price = 0 or NULL

-- CORRECT: Fix data first
UPDATE products SET price = 0.01 WHERE price <= 0;
ALTER TABLE products ADD CONSTRAINT chk_price CHECK (price > 0);
```

## Examples

```sql
-- Example 1: Basic CHECK constraint
ALTER TABLE employees ADD CONSTRAINT chk_age
    CHECK (age >= 18 AND age <= 120);

-- Example 2: CHECK with IN list
ALTER TABLE orders ADD CONSTRAINT chk_status
    CHECK (status IN ('pending', 'shipped', 'delivered', 'cancelled'));

-- Example 3: CHECK with LIKE pattern
ALTER TABLE users ADD CONSTRAINT chk_email_format
    CHECK (email LIKE '%_@_%.__%');
```

## Related Errors

- [Constraint error](sql-constraint-error) -- constraint violations
- [Check constraint violation](check-constraint-violation) -- CHECK failures
