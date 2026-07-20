---
title: "[Solution] MySQL Error 1062 — Duplicate Entry (PDO)"
description: "Fix MySQL PDO error 1062 duplicate entry. Use INSERT IGNORE, handle unique constraints, check duplicate values. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 234
---

# MySQL Error 1062 — Duplicate Entry (PDO)

MySQL error 1062 occurs when an INSERT or UPDATE violates a UNIQUE constraint. This happens when you try to insert a row with a value that already exists in a unique index or primary key column.

## Common Causes

```php
// Inserting duplicate primary key
$stmt = $pdo->prepare("INSERT INTO users (id, name) VALUES (?, ?)");
$stmt->execute([1, 'John']); // ID 1 already exists
// Error 1062: Duplicate entry '1' for key 'PRIMARY'
```

```php
// Duplicate value in unique column
$stmt = $pdo->prepare("INSERT INTO users (email) VALUES (?)");
$stmt->execute(['john@example.com']); // Email already registered
// Error 1062: Duplicate entry 'john@example.com' for key 'email'
```

```php
// Race condition in concurrent requests
// Two requests check if email exists, both insert
// First succeeds, second gets error 1062
```

```php
// Composite unique key violation
$stmt = $pdo->prepare("INSERT INTO user_roles (user_id, role_id) VALUES (?, ?)");
$stmt->execute([1, 2]); // User-role combination already exists
// Error 1062: Duplicate entry '1-2' for key 'user_role_unique'
```

```php
// Auto-increment ID collision after manual ID assignment
$stmt = $pdo->query("ALTER TABLE users AUTO_INCREMENT = 100");
$stmt = $pdo->prepare("INSERT INTO users (id, name) VALUES (?, ?)");
$stmt->execute([100, 'Test']); // Conflict with existing row
```

## How to Fix

### Fix 1: Check Before Inserting

```php
function insertUser(PDO $pdo, string $email, string $name): bool
{
    // Check if email already exists
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE email = ?");
    $stmt->execute([$email]);
    $exists = $stmt->fetchColumn() > 0;

    if ($exists) {
        return false;
    }

    // Insert new user
    $stmt = $pdo->prepare("INSERT INTO users (email, name) VALUES (?, ?)");
    return $stmt->execute([$email, $name]);
}
```

### Fix 2: Use INSERT IGNORE

```php
// Silently skip duplicate inserts
$stmt = $pdo->prepare("INSERT IGNORE INTO users (email, name) VALUES (?, ?)");
$stmt->execute(['john@example.com', 'John']);

// Check if row was actually inserted
if ($stmt->rowCount() === 0) {
    echo "Email already exists";
}
```

### Fix 3: Use REPLACE INTO (Delete + Insert)

```php
// Replace existing row or insert new
$stmt = $pdo->prepare("REPLACE INTO users (email, name, status) VALUES (?, ?, ?)");
$stmt->execute(['john@example.com', 'John', 'active']);

// Warning: This deletes the old row and creates a new one
// Auto-increment ID will change
```

### Fix 4: Use ON DUPLICATE KEY UPDATE

```php
// Update if exists, insert if not
$stmt = $pdo->prepare("
    INSERT INTO users (email, name, login_count, last_login)
    VALUES (?, ?, 1, NOW())
    ON DUPLICATE KEY UPDATE
        login_count = login_count + 1,
        last_login = NOW()
");
$stmt->execute(['john@example.com', 'John']);

// MySQL returns affected rows: 1 = inserted, 2 = updated
```

### Fix 5: Handle Race Conditions With Transactions

```php
function safeInsertUser(PDO $pdo, string $email, string $name): int
{
    $pdo->beginTransaction();

    try {
        // Lock table for exclusive access
        $pdo->exec("LOCK TABLES users WRITE");

        // Check if email exists
        $stmt = $pdo->prepare("SELECT id FROM users WHERE email = ?");
        $stmt->execute([$email]);
        $existing = $stmt->fetch();

        if ($existing) {
            $pdo->exec("UNLOCK TABLES");
            $pdo->rollBack();
            return $existing['id'];
        }

        // Insert new user
        $stmt = $pdo->prepare("INSERT INTO users (email, name) VALUES (?, ?)");
        $stmt->execute([$email, $name]);
        $newId = (int) $pdo->lastInsertId();

        $pdo->exec("UNLOCK TABLES");
        $pdo->commit();

        return $newId;
    } catch (Exception $e) {
        $pdo->exec("UNLOCK TABLES");
        $pdo->rollBack();
        throw $e;
    }
}

$userId = safeInsertUser($pdo, 'john@example.com', 'John');
```

## Examples

```php
// Upsert with PDO (MySQL 8.0.19+)
function upsertUser(PDO $pdo, string $email, string $name): void
{
    $stmt = $pdo->prepare("
        INSERT INTO users (email, name)
        VALUES (?, ?)
        AS new_row
        ON DUPLICATE KEY UPDATE
            name = new_row.name
    ");
    $stmt->execute([$email, $name]);
}
```

```php
// Batch insert with duplicate handling
function batchInsertProducts(PDO $pdo, array $products): array
{
    $inserted = 0;
    $duplicates = 0;

    foreach ($products as $product) {
        $stmt = $pdo->prepare("
            INSERT IGNORE INTO products (sku, name, price)
            VALUES (?, ?, ?)
        ");
        $stmt->execute([$product['sku'], $product['name'], $product['price']]);

        if ($stmt->rowCount() > 0) {
            $inserted++;
        } else {
            $duplicates++;
        }
    }

    return compact('inserted', 'duplicates');
}
```

```php
// Handle duplicate with user-friendly message
function registerUser(PDO $pdo, array $data): array
{
    try {
        $stmt = $pdo->prepare("INSERT INTO users (email, username, password_hash) VALUES (?, ?, ?)");
        $stmt->execute([
            $data['email'],
            $data['username'],
            password_hash($data['password'], PASSWORD_DEFAULT),
        ]);

        return [
            'success' => true,
            'user_id' => $pdo->lastInsertId(),
        ];
    } catch (PDOException $e) {
        if ($pdo->errorCode() === '23000') {
            $info = $e->errorInfo[2];

            if (str_contains($info, 'email')) {
                return ['success' => false, 'error' => 'Email already registered'];
            }
            if (str_contains($info, 'username')) {
                return ['success' => false, 'error' => 'Username already taken'];
            }

            return ['success' => false, 'error' => 'Account already exists'];
        }

        throw $e;
    }
}

$result = registerUser($pdo, [
    'email' => 'john@example.com',
    'username' => 'johndoe',
    'password' => 'securepass123',
]);
```

## Related Errors

- [pdo-error.md](/content/languages/php/pdo-error.md) — General PDO errors
- [pdo-mysql-errno-1452.md](/content/languages/php/pdo-mysql-errno-1452.md) — Foreign key constraint fails
- [pdo-sqlstate-errors.md](/content/languages/php/pdo-sqlstate-errors.md) — SQLSTATE error reference
- [pdo-prepared-statement.md](/content/languages/php/pdo-prepared-statement.md) — Prepared statement issues
