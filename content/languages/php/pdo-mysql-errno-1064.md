---
title: "[Solution] MySQL Error 1064 — SQL Syntax Error (PDO)"
description: "Fix MySQL PDO error 1064 SQL syntax errors. Check SQL syntax, verify table/column names, MySQL version compatibility. Copy-paste solutions."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 232
---

# MySQL Error 1064 — SQL Syntax Error (PDO)

MySQL error 1064 indicates a SQL syntax error in your query. This is one of the most common MySQL errors and typically results from typos, missing quotes, incorrect keywords, reserved word usage, or MySQL version compatibility issues.

## Common Causes

```php
// Missing quotes around string values
$stmt = $pdo->query("SELECT * FROM users WHERE name = John");
// Error 1064: You have an error in your SQL syntax near 'John'
```

```php
// Reserved word used without backticks
$stmt = $pdo->query("SELECT order FROM orders");
// Error 1064: You have an error in your SQL syntax near 'order'
```

```php
// Trailing comma in column list
$stmt = $pdo->query("SELECT name, email, FROM users");
// Error 1064: You have an error in your SQL syntax near 'FROM'
```

```php
// Wrong number of placeholders
$stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
$stmt->execute(['John']); // Missing second parameter
// Error 1064: Incorrect number of arguments
```

```php
// MySQL version syntax incompatibility
$stmt = $pdo->query("SELECT * FROM users USING INDEX FOR ORDER BY");
// Syntax not supported in older MySQL versions
```

## How to Fix

### Fix 1: Validate SQL Before Execution

```php
function debugQuery(PDO $pdo, string $sql, array $params = []): PDOStatement
{
    // Log the actual query for debugging
    $debugSql = $sql;
    foreach ($params as $i => $param) {
        $debugSql = preg_replace('/\?/', "'" . addslashes($param) . "'", $debugSql, 1);
    }
    error_log("SQL: $debugSql");

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($params);
        return $stmt;
    } catch (PDOException $e) {
        $info = $stmt->errorInfo();
        error_log("MySQL Error: " . ($info[2] ?? $e->getMessage()));
        throw $e;
    }
}

debugQuery($pdo, "SELECT * FROM users WHERE id = ?", [1]);
```

### Fix 2: Use Backticks for Reserved Words

```php
// Instead of:
$stmt = $pdo->query("SELECT order FROM orders WHERE order = 'pending'");

// Use backticks:
$stmt = $pdo->query("SELECT `order` FROM `orders` WHERE `order` = 'pending'");

// Or rename the column in your schema to avoid reserved words
```

### Fix 3: Fix Placeholder Count and Types

```php
// Ensure placeholders match parameter count
$columns = ['name', 'email', 'phone'];
$placeholders = array_fill(0, count($columns), '?');
$values = ['John', 'john@example.com', '555-0123'];

$stmt = $pdo->prepare(
    "INSERT INTO users (" . implode(', ', $columns) . ") VALUES (" . implode(', ', $placeholders) . ")"
);
$stmt->execute($values);

// For named placeholders
$params = [
    ':name' => 'John',
    ':email' => 'john@example.com',
    ':phone' => '555-0123',
];

$stmt = $pdo->prepare("INSERT INTO users (name, email, phone) VALUES (:name, :email, :phone)");
$stmt->execute($params);
```

### Fix 4: Check MySQL Version Compatibility

```php
// Check MySQL version
$version = $pdo->query("SELECT VERSION()")->fetchColumn();
error_log("MySQL version: $version");

// Use version-appropriate syntax
if (version_compare($version, '8.0.0', '>=')) {
    // MySQL 8.0+: window functions, CTEs, etc.
    $sql = "WITH cte AS (SELECT id, name FROM users) SELECT * FROM cte";
} else {
    // MySQL 5.7: subqueries instead
    $sql = "SELECT * FROM (SELECT id, name FROM users) AS cte";
}
```

### Fix 5: Use Query Builder for Complex Queries

```php
class QueryBuilder
{
    private PDO $pdo;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function select(string $table, array $columns, array $conditions): PDOStatement
    {
        $cols = array_map(fn($c) => "`$c`", $columns);
        $where = [];
        $params = [];

        foreach ($conditions as $col => $val) {
            $where[] = "`$col` = ?";
            $params[] = $val;
        }

        $sql = sprintf(
            "SELECT %s FROM `%s`%s",
            implode(', ', $cols),
            $table,
            $where ? ' WHERE ' . implode(' AND ', $where) : ''
        );

        $stmt = $this->pdo->prepare($sql);
        $stmt->execute($params);
        return $stmt;
    }
}

$builder = new QueryBuilder($pdo);
$stmt = $builder->select('users', ['id', 'name', 'email'], ['status' => 'active']);
```

## Examples

```php
// Common syntax error patterns and fixes
$queries = [
    // Wrong: Missing backtick for table with special chars
    // "SELECT * FROM user-data"  -> Error 1064
    "SELECT * FROM `user-data`",  // Correct

    // Wrong: Subquery without alias
    // "SELECT * FROM (SELECT id FROM users)" -> Error 1064
    "SELECT * FROM (SELECT id FROM users) AS sub",  // Correct

    // Wrong: GROUP BY position with LIMIT
    // MySQL 5.7 with ONLY_FULL_GROUP_BY
    "SELECT name, COUNT(*) FROM users GROUP BY name",
];
```

```php
// Auto-fix common syntax mistakes
function cleanSql(string $sql): string
{
    // Remove extra spaces
    $sql = preg_replace('/\s+/', ' ', trim($sql));

    // Add missing backticks for common reserved words
    $reserved = ['order', 'group', 'select', 'table', 'index', 'key', 'user', 'status'];
    foreach ($reserved as $word) {
        $sql = preg_replace("/\b$word\b/i", "`$word`", $sql);
    }

    // Fix trailing commas before FROM/JOIN/WHERE
    $sql = preg_replace('/,\s*(FROM|JOIN|WHERE|GROUP|ORDER|LIMIT)/i', ' $1', $sql);

    return $sql;
}

$fixedSql = cleanSql("SELECT * FROM user WHERE status = 'active',");
// Result: SELECT * FROM `user` WHERE `status` = 'active'
```

## Related Errors

- [pdo-error.md](/content/languages/php/pdo-error.md) — General PDO errors
- [pdo-sqlstate-errors.md](/content/languages/php/pdo-sqlstate-errors.md) — SQLSTATE error reference
- [pdo-mysql-errno-1045.md](/content/languages/php/pdo-mysql-errno-1045.md) — MySQL access denied
- [pdo-prepared-statement.md](/content/languages/php/pdo-prepared-statement.md) — Prepared statement issues
