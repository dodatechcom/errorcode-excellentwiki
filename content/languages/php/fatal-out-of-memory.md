---
title: "[Solution] PHP Fatal Error: Allowed Memory Size Exhausted — Fix Out of Memory"
description: "Fix PHP Fatal error: Allowed memory size exhausted. Increase memory_limit, use generators, and optimize database queries to prevent OOM."
languages: ["php"]
severities: ["error"]
error_types: ["runtime"]
date: 2026-07-15
---

# PHP Fatal Error: Allowed Memory Size Exhausted

This fatal error means your script has exceeded the `memory_limit` defined in `php.ini`. The most common trigger is loading a large dataset entirely into memory, such as fetching thousands of rows from a database or processing large files.

## Common Causes

- Fetching an entire large table with `SELECT *` without pagination
- Reading large files into memory with `file_get_contents()`
- Creating massive arrays or string concatenations in loops
- Memory leaks from circular references in long-running scripts

## Solutions

### 1. Increase the Memory Limit

The quickest fix — raise the limit for scripts that genuinely need more memory.

```php
// Increase to 256MB for this script
ini_set("memory_limit", "256M");

// Or set in php.ini
memory_limit = 256M
```

### 2. Use Generators for Large Datasets

Generators yield one item at a time instead of loading everything into memory.

```php
// Bad — loads all rows into memory
function getAllUsers() {
    $result = $pdo->query("SELECT * FROM users");
    return $result->fetchAll(PDO::FETCH_ASSOC);
}

// Good — yields one row at a time
function getAllUsers() {
    $stmt = $pdo->query("SELECT * FROM users");
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        yield $row;
    }
}

// Usage
foreach (getAllUsers() as $user) {
    echo $user["name"] . "\n";
}
```

### 3. Optimize Database Queries

Avoid loading unnecessary data and use pagination.

```php
// Bad — loads everything
$users = $pdo->query("SELECT * FROM users")->fetchAll();

// Good — paginated query
$perPage = 50;
$page = max(1, (int)($_GET["page"] ?? 1));
$offset = ($page - 1) * $perPage;

$stmt = $pdo->prepare("SELECT id, name, email FROM users LIMIT :limit OFFSET :offset");
$stmt->bindValue(":limit", $perPage, PDO::PARAM_INT);
$stmt->bindValue(":offset", $offset, PDO::PARAM_INT);
$stmt->execute();
$users = $stmt->fetchAll(PDO::FETCH_ASSOC);
```

### 4. Process Files in Chunks

Don't read entire large files into memory — process them line by line.

```php
// Bad — reads entire file into memory
$content = file_get_contents("huge_log.txt");

// Good — reads line by line
$handle = fopen("huge_log.txt", "r");
while (($line = fgets($handle)) !== false) {
    // Process each line
}
fclose($handle);
```

### 5. Free Memory Proactively

Unset large variables when they're no longer needed.

```php
$largeData = fetchLargeDataset();
processData($largeData);
unset($largeData); // Free the memory immediately
```

## Prevention Tips

- Profile memory usage with `memory_get_peak_usage(true)` during development
- Set a reasonable `memory_limit` in `php.ini` (128M is a common default)
- Use database pagination for any query that could return thousands of rows

## Related Errors

- [PHP Warning: Wrong Parameter Count](/languages/php/warning-count)
- [PHP Parse Error](/languages/php/parse-error)
