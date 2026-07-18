---
title: "[Solution] MariaDB Stored Procedure Error — How to Fix"
description: "Fix MariaDB stored procedure errors including syntax problems, variable scope issues, cursor handling bugs, and privilege requirements"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Stored Procedure Error

Stored procedure errors occur when CREATE PROCEDURE has syntax errors, variables conflict with column names, cursors are misused, or the user lacks EXECUTE privileges.

## Why It Happens

- The procedure body has syntax errors caught only at runtime
- Local variables conflict with column names
- A cursor is opened twice without being closed
- The DELIMITER is not set correctly
- The procedure references a table or column that does not exist

## Common Error Messages

```
ERROR 1064 (42000): You have an error in your SQL syntax
```

```
ERROR 1304 (42000): Procedure proc_name does not exist
```

```
ERROR 1337 (42000): Variable or condition declaration after cursor or handler declaration
```

```
ERROR 1457 (HY000): Failed to populate variables from the result set of cursor 'c1'
```

## How to Fix It

### 1. Set DELIMITER Correctly

```sql
DELIMITER //
CREATE PROCEDURE get_users()
BEGIN
  SELECT * FROM users;
END//
DELIMITER ;
```

### 2. Fix Variable Scope and Naming Conflicts

```sql
DELIMITER //
CREATE PROCEDURE update_user(IN p_id INT, IN p_name VARCHAR(100))
BEGIN
  DECLARE v_name VARCHAR(100);
  SET v_name = p_name;
  UPDATE users SET name = v_name WHERE id = p_id;
END//
DELIMITER ;
```

### 3. Fix Cursor Handling

```sql
DELIMITER //
CREATE PROCEDURE process_orders()
BEGIN
  DECLARE v_id INT;
  DECLARE v_done INT DEFAULT 0;
  DECLARE cur CURSOR FOR SELECT id FROM orders WHERE status = 'pending';
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET v_done = 1;

  OPEN cur;
  read_loop: LOOP
    FETCH cur INTO v_id;
    IF v_done THEN LEAVE read_loop; END IF;
    UPDATE orders SET status = 'processed' WHERE id = v_id;
  END LOOP;
  CLOSE cur;
END//
DELIMITER ;
```

### 4. Set OUT Parameters

```sql
DELIMITER //
CREATE PROCEDURE get_user_count(OUT total INT)
BEGIN
  SELECT COUNT(*) INTO total FROM users;
END//
DELIMITER ;

CALL get_user_count(@total);
SELECT @total;
```

### 5. Add Error Handling

```sql
DELIMITER //
CREATE PROCEDURE safe_insert(IN p_name VARCHAR(100))
BEGIN
  DECLARE EXIT HANDLER FOR 1062
  BEGIN
    SELECT CONCAT('User ', p_name, ' already exists') AS error;
  END;
  INSERT INTO users (name) VALUES (p_name);
END//
DELIMITER ;
```

## Common Scenarios

- **Procedure works in phpMyAdmin but not CLI**: phpMyAdmin handles delimiters automatically.
- **Cursor fetch returns NULL**: SELECT types do not match DECLARE types.
- **"PROCEDURE does not exist"**: Created in different database. Use `database.procedure_name`.

## Prevent It

- Test stored procedures in transactions for rollback safety
- Add condition handlers for common error codes
- Keep stored procedure logic simple

## Related Pages

- [MariaDB Trigger Error](/tools/mariadb/mariadb-trigger-error)
- [MariaDB User Error](/tools/mariadb/mariadb-user-error)
- [MySQL Stored Procedure Error](/tools/mysql/mysql-stored-proc-error)
