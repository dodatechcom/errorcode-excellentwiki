---
title: "[Solution] PHP PDO Fetch Error"
description: "Fix PHP PDO SQLSTATE[HY000] Fetch error. Learn to resolve issues with fetching data from result sets."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "pdo", "database", "fetch", "result-set"]
severity: "error"
---

# SQLSTATE[HY000] Fetch Error

## Error Message

```
SQLSTATE[HY000] General error in fetch()
```

## Common Causes

- Calling fetch() on a statement that was not executed
- The statement handle has already been closed or freed
- Fetching after the result set has been fully consumed
- Using an invalid or unsupported fetch mode constant

## Solutions

### Solution 1: Verify Statement Execution Before Fetching

Always confirm that execute() was called successfully before attempting to fetch results.

```php
<?php
function fetchAllUsers(PDO $pdo): array
{
    $sql = 'SELECT id, name, email, created_at FROM users WHERE status = :status';
    $stmt = $pdo->prepare($sql);

    if (!$stmt->execute([':status' => 'active'])) {
        throw new RuntimeException('Failed to execute query');
    }

    // Verify rows exist before fetching
    if ($stmt->rowCount() === 0) {
        return [];
    }

    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Usage
try {
    $users = fetchAllUsers($pdo);
    foreach ($users as $user) {
        echo "{$user['name']} ({$user['email']})\n";
    }
} catch (PDOException $e) {
    error_log('Fetch error: ' . $e->getMessage());
}
```

### Solution 2: Use the Correct Fetch Mode

Choose the appropriate fetch mode for your use case and ensure it is compatible with your PDO driver.

```php
<?php
// Set default fetch mode in the PDO constructor to avoid mode issues
$pdo = new PDO($dsn, $user, $pass, [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);

// Fetch modes for different use cases
$stmt = $pdo->prepare('SELECT id, name, email FROM users WHERE id = :id');
$stmt->execute([':id' => 1]);

// Fetch as associative array (most common)
$row = $stmt->fetch(PDO::FETCH_ASSOC);

// Fetch as an object
$row = $stmt->fetch(PDO::FETCH_OBJ);

// Fetch into a specific class
class UserDTO
{
    public int $id;
    public string $name;
    public string $email;
}

$stmt->execute([':id' => 1]);
$user = $stmt->fetchObject(UserDTO::class);

// Fetch only a single column
$stmt->execute([':id' => 1]);
$name = $stmt->fetchColumn(); // returns the first column value
```

### Solution 3: Handle Large Result Sets with Cursors

Use unbuffered queries and fetch cursors to handle large datasets without exhausting memory.

```php
<?php
// Use unbuffered query for large result sets
$pdo->setAttribute(PDO::MYSQL_ATTR_USE_BUFFERED_QUERY, false);

$stmt = $pdo->prepare('SELECT id, name, email FROM users');
$stmt->execute();

// Fetch one row at a time to control memory usage
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
    // Process each row without loading entire result set
    processUserRow($row);
}

// Reset to buffered mode for normal queries
$pdo->setAttribute(PDO::MYSQL_ATTR_USE_BUFFERED_QUERY, true);

// Alternatively, use fetchAll() in chunks with LIMIT/OFFSET
function fetchUsersInChunks(PDO $pdo, int $chunkSize = 1000): Generator
{
    $offset = 0;

    do {
        $stmt = $pdo->prepare(
            'SELECT id, name, email FROM users ORDER BY id LIMIT :limit OFFSET :offset'
        );
        $stmt->bindValue(':limit', $chunkSize, PDO::PARAM_INT);
        $stmt->bindValue(':offset', $offset, PDO::PARAM_INT);
        $stmt->execute();

        $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
        if (empty($rows)) {
            break;
        }

        yield from $rows;
        $offset += $chunkSize;
    } while (count($rows) === $chunkSize);
}
```

## Prevention Tips

- Set PDO::ATTR_DEFAULT_FETCH_MODE in the constructor to avoid forgetting fetch modes on every call
- Use unbuffered queries (PDO::MYSQL_ATTR_USE_BUFFERED_QUERY = false) for large result sets
- Always check rowCount() or verify fetch() does not return false before using result data

## Related Errors

- [PHP PDOException: SQLSTATE[HY000]]({{< relref "/languages/php/pdo-error" >}})
- [PHP PDO Prepare Statement Error]({{< relref "/languages/php/pdo-prepared-statement" >}})
- [PHP PDO Column Not Found Error]({{< relref "/languages/php/pdo-column-error" >}})
