---
title: "[Solution] PHP PDO Exec Error"
description: "Fix PHP PDO SQLSTATE[HY000] Exec error. Learn to handle failures with exec() and multi-statement queries."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "pdo", "database", "exec", "execute", "multi-statement"]
severity: "error"
---

# SQLSTATE[HY000] Exec Error

## Error Message

```
SQLSTATE[HY000] General error in exec()
```

## Common Causes

- The SQL statement contains syntax errors or invalid operations
- Multi-statement execution is not enabled in the PDO driver
- The statement affects rows that violate constraints (unique, foreign key, not null)
- Insufficient privileges for the database user on the targeted table

## Solutions

### Solution 1: Enable Multi-Statement Queries When Needed

Enable the PDO::MYSQL_ATTR_MULTI_STATEMENTS option if you need to run multiple SQL statements in one call.

```php
<?php
// Enable multi-statement execution for MySQL
$pdo = new PDO(
    'mysql:host=localhost;dbname=myapp;charset=utf8mb4',
    'dbuser',
    'dbpassword',
    [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::MYSQL_ATTR_MULTI_STATEMENTS => true,
    ]
);

// Now you can execute multiple statements
$sql = "
    INSERT INTO audit_log (action, user_id, created_at) VALUES ('login', 1, NOW());
    INSERT INTO login_history (user_id, ip_address, logged_in_at) VALUES (1, '192.168.1.1', NOW());
";
$affectedRows = $pdo->exec($sql);
echo "Statements executed, rows affected: {$affectedRows}";
```

### Solution 2: Use rowCount() to Verify Exec Results

Check the return value of exec() to verify the number of rows affected and handle zero-row scenarios.

```php
<?php
function executeUpdate(PDO $pdo, string $table, array $data, string $where, array $whereParams): int
{
    $setClause = implode(', ', array_map(fn($col) => "{$col} = :{$col}", array_keys($data)));
    $sql = "UPDATE {$table} SET {$setClause} WHERE {$where}";

    $stmt = $pdo->prepare($sql);
    $stmt->execute(array_merge($data, $whereParams));

    $affected = $stmt->rowCount();

    if ($affected === 0) {
        error_log("Update query affected 0 rows. Query: {$sql}");
    }

    return $affected;
}

// Usage
$updated = executeUpdate(
    $pdo,
    'users',
    ['status' => 'inactive', 'updated_at' => date('Y-m-d H:i:s')],
    'last_login < :cutoff',
    ['cutoff' => '2025-01-01']
);

echo "Updated {$updated} user(s)";
```

### Solution 3: Validate SQL Before Execution

Use a helper function to validate and sanitize SQL input to prevent exec() failures.

```php
<?php
function safeExec(PDO $pdo, string $sql, array $allowedTables = []): int
{
    // Optional: Validate against a whitelist of allowed tables
    if (!empty($allowedTables)) {
        preg_match_all('/\b(?:FROM|INTO|UPDATE|JOIN)\s+`?(\w+)`?/', $sql, $matches);
        foreach ($matches[1] as $table) {
            if (!in_array($table, $allowedTables, true)) {
                throw new InvalidArgumentException("Table '{$table}' is not in the allowed list");
            }
        }
    }

    try {
        $affected = $pdo->exec($sql);
        error_log("Query executed successfully. Rows affected: {$affected}");
        return $affected;
    } catch (PDOException $e) {
        error_log("exec() failed: {$e->getMessage()}");
        error_log("SQL was: {$sql}");
        throw $e;
    }
}

// Usage
$allowed = ['users', 'sessions', 'audit_log'];
$count = safeExec($pdo, 'DELETE FROM sessions WHERE expires_at < NOW()', $allowed);
```

## Prevention Tips

- Avoid enabling multi-statement queries unless absolutely necessary due to SQL injection risks
- Always validate table and column names against an allowlist when building dynamic SQL
- Use PDO::ERRMODE_EXCEPTION to get clear error messages when exec() fails

## Related Errors

- [PHP PDOException: SQLSTATE[HY000]]({{< relref "/languages/php/pdo-error" >}})
- [PHP PDO Prepare Statement Error]({{< relref "/languages/php/pdo-prepared-statement" >}})
- [PHP PDO Transaction Error]({{< relref "/languages/php/pdo-transaction-error" >}})
