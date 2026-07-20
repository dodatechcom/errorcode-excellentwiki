---
title: "[Solution] MySQL Error 1452 — Foreign Key Constraint Fails (PDO)"
description: "Fix MySQL PDO error 1452 foreign key constraint fails. Check referenced table, verify values, handle referential integrity. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 235
---

# MySQL Error 1452 — Foreign Key Constraint Fails (PDO)

MySQL error 1452 occurs when an INSERT or UPDATE violates a foreign key constraint. The referenced value in the child table doesn't exist in the parent table, or a DELETE/UPDATE on the parent table would leave orphaned rows in the child table.

## Common Causes

```php
// Insert with non-existent foreign key
$stmt = $pdo->prepare("INSERT INTO orders (user_id, product_id) VALUES (?, ?)");
$stmt->execute([999, 1]); // user_id 999 doesn't exist in users table
// Error 1452: Cannot add or update a child row: foreign key constraint fails
```

```php
// Delete parent row with existing children
$stmt = $pdo->exec("DELETE FROM users WHERE id = 1");
// Error 1452: Cannot delete or update a parent row: foreign key constraint fails
```

```php
// Update primary key that is referenced
$stmt = $pdo->prepare("UPDATE users SET id = ? WHERE id = ?");
$stmt->execute([999, 1]); // ID 1 is referenced by orders table
// Error 1452: Cannot delete or update a parent row
```

```php
// Bulk insert with some invalid foreign keys
foreach ($orders as $order) {
    $stmt = $pdo->prepare("INSERT INTO orders (user_id) VALUES (?)");
    $stmt->execute([$order['user_id']]); // Some user_ids don't exist
}
```

```php
// Wrong order of inserts (child before parent)
$stmt = $pdo->prepare("INSERT INTO order_items (order_id, product_id) VALUES (?, ?)");
$stmt->execute([1, 10]); // order_id 1 doesn't exist yet
```

## How to Fix

### Fix 1: Validate Foreign Keys Before Insert

```php
function insertOrder(PDO $pdo, int $userId, int $productId): bool
{
    // Validate user exists
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE id = ?");
    $stmt->execute([$userId]);
    if ($stmt->fetchColumn() == 0) {
        throw new InvalidArgumentException("User $userId does not exist");
    }

    // Validate product exists
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM products WHERE id = ?");
    $stmt->execute([$productId]);
    if ($stmt->fetchColumn() == 0) {
        throw new InvalidArgumentException("Product $productId does not exist");
    }

    // Safe to insert
    $stmt = $pdo->prepare("INSERT INTO orders (user_id, product_id) VALUES (?, ?)");
    return $stmt->execute([$userId, $productId]);
}
```

### Fix 2: Use ON DELETE CASCADE

```php
// Create table with cascade delete
$pdo->exec("
    CREATE TABLE orders (
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE
            ON UPDATE RESTRICT
    )
");

// Now deleting a user automatically deletes their orders
$pdo->exec("DELETE FROM users WHERE id = 1");
```

### Fix 3: Handle Foreign Key Errors Gracefully

```php
function insertWithForeignKeyCheck(PDO $pdo, string $sql, array $params): bool
{
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($params);
        return true;
    } catch (PDOException $e) {
        if ($pdo->errorCode() === '23000') {
            $info = $e->errorInfo[2];

            if (str_contains($info, 'foreign key constraint')) {
                error_log("Foreign key violation: " . $info);
                return false;
            }
        }
        throw $e;
    }
}

$success = insertWithForeignKeyCheck(
    $pdo,
    "INSERT INTO orders (user_id, product_id) VALUES (?, ?)",
    [999, 1]
);
```

### Fix 4: Insert in Correct Order

```php
function insertOrderWithItems(PDO $pdo, array $orderData, array $items): void
{
    $pdo->beginTransaction();

    try {
        // Insert parent first
        $stmt = $pdo->prepare("INSERT INTO orders (user_id, total) VALUES (?, ?)");
        $stmt->execute([$orderData['user_id'], $orderData['total']]);
        $orderId = $pdo->lastInsertId();

        // Then insert children
        $stmt = $pdo->prepare("INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)");
        foreach ($items as $item) {
            $stmt->execute([$orderId, $item['product_id'], $item['quantity']]);
        }

        $pdo->commit();
    } catch (Exception $e) {
        $pdo->rollBack();
        throw $e;
    }
}
```

### Fix 5: Temporarily Disable Foreign Key Checks

```php
function bulkInsertWithCheckDisable(PDO $pdo, string $table, array $rows): void
{
    $pdo->beginTransaction();

    try {
        // Disable foreign key checks for this session
        $pdo->exec("SET FOREIGN_KEY_CHECKS = 0");

        foreach ($rows as $row) {
            $columns = implode(', ', array_keys($row));
            $placeholders = implode(', ', array_fill(0, count($row), '?'));
            $sql = "INSERT INTO $table ($columns) VALUES ($placeholders)";

            $stmt = $pdo->prepare($sql);
            $stmt->execute(array_values($row));
        }

        // Re-enable and verify
        $pdo->exec("SET FOREIGN_KEY_CHECKS = 1");

        $pdo->commit();
    } catch (Exception $e) {
        $pdo->exec("SET FOREIGN_KEY_CHECKS = 1");
        $pdo->rollBack();
        throw $e;
    }
}

// Insert data that may reference non-existent parent rows
bulkInsertWithCheckDisable($pdo, 'orders', [
    ['user_id' => 999, 'product_id' => 1],
    ['user_id' => 1000, 'product_id' => 2],
]);
```

## Examples

```php
// Complete CRUD with foreign key handling
class OrderRepository
{
    private PDO $pdo;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function create(int $userId, array $items): int
    {
        $this->pdo->beginTransaction();

        try {
            // Validate user
            $stmt = $this->pdo->prepare("SELECT id FROM users WHERE id = ?");
            $stmt->execute([$userId]);
            if (!$stmt->fetch()) {
                throw new InvalidArgumentException("Invalid user ID: $userId");
            }

            // Validate products
            $productIds = array_column($items, 'product_id');
            $placeholders = implode(',', array_fill(0, count($productIds), '?'));
            $stmt = $this->pdo->prepare("SELECT id FROM products WHERE id IN ($placeholders)");
            $stmt->execute($productIds);
            $validIds = array_column($stmt->fetchAll(), 'id');

            $invalid = array_diff($productIds, $validIds);
            if (!empty($invalid)) {
                throw new InvalidArgumentException("Invalid product IDs: " . implode(', ', $invalid));
            }

            // Create order
            $total = array_sum(array_map(fn($i) => $i['price'] * $i['quantity'], $items));
            $stmt = $this->pdo->prepare("INSERT INTO orders (user_id, total) VALUES (?, ?)");
            $stmt->execute([$userId, $total]);
            $orderId = $this->pdo->lastInsertId();

            // Create order items
            $stmt = $this->pdo->prepare("INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)");
            foreach ($items as $item) {
                $stmt->execute([$orderId, $item['product_id'], $item['quantity'], $item['price']]);
            }

            $this->pdo->commit();
            return $orderId;
        } catch (Exception $e) {
            $this->pdo->rollBack();
            throw $e;
        }
    }

    public function delete(int $orderId): bool
    {
        $this->pdo->beginTransaction();

        try {
            // Delete children first
            $stmt = $this->pdo->prepare("DELETE FROM order_items WHERE order_id = ?");
            $stmt->execute([$orderId]);

            // Then delete parent
            $stmt = $this->pdo->prepare("DELETE FROM orders WHERE id = ?");
            $stmt->execute([$orderId]);

            $deleted = $stmt->rowCount() > 0;
            $this->pdo->commit();

            return $deleted;
        } catch (Exception $e) {
            $this->pdo->rollBack();
            throw $e;
        }
    }
}
```

## Related Errors

- [pdo-mysql-errno-1062.md](/content/languages/php/pdo-mysql-errno-1062.md) — MySQL duplicate entry error
- [pdo-transaction-error.md](/content/languages/php/pdo-transaction-error.md) — PDO transaction errors
- [pdo-error.md](/content/languages/php/pdo-error.md) — General PDO errors
- [pdo-sqlstate-errors.md](/content/languages/php/pdo-sqlstate-errors.md) — SQLSTATE error reference
