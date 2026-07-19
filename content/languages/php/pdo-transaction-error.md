---
title: "[Solution] PHP PDO Transaction Error"
description: "Fix PHP PDO SQLSTATE[HY000] Transaction errors. Learn to handle commit, rollback, and nested transaction issues."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "pdo", "database", "transaction", "commit", "rollback"]
severity: "error"
---

# SQLSTATE[HY000] Transaction Error

## Error Message

```
SQLSTATE[HY000] General error in transaction handling
```

## Common Causes

- Attempting to commit or roll back when no transaction is active
- Nested transactions are not supported by the database driver
- A query failed inside the transaction, putting it in an inconsistent state
- The connection was lost during a long-running transaction

## Solutions

### Solution 1: Track Transaction State Properly

Implement a transaction wrapper that tracks whether a transaction is currently active to prevent nesting issues.

```php
<?php
class DatabaseTransaction
{
    private PDO $pdo;
    private int $transactionCount = 0;

    public function __construct(PDO $pdo)
    {
        $this->pdo = $pdo;
    }

    public function begin(callable $callback): mixed
    {
        if ($this->transactionCount === 0) {
            $this->pdo->beginTransaction();
        }
        $this->transactionCount++;

        try {
            $result = $callback($this->pdo);
            $this->transactionCount--;

            if ($this->transactionCount === 0) {
                $this->pdo->commit();
            }
            return $result;
        } catch (Throwable $e) {
            $this->transactionCount = 0;
            $this->pdo->rollBack();
            throw $e;
        }
    }
}

// Usage
$db = new DatabaseTransaction($pdo);
$user = $db->begin(function (PDO $pdo) use ($userData) {
    $stmt = $pdo->prepare('INSERT INTO users (name, email) VALUES (:name, :email)');
    $stmt->execute([':name' => $userData['name'], ':email' => $userData['email']]);
    return $pdo->lastInsertId();
});
```

### Solution 2: Use Savepoints for Nested Transactions

Leverage savepoints to simulate nested transactions when your database driver does not support them natively.

```php
<?php
function withSavepoint(PDO $pdo, callable $callback): void
{
    $savepointName = 'sp_' . bin2hex(random_bytes(8));

    try {
        $pdo->exec("SAVEPOINT {$savepointName}");
        $callback($pdo);
        $pdo->exec("RELEASE SAVEPOINT {$savepointName}");
    } catch (Throwable $e) {
        try {
            $pdo->exec("ROLLBACK TO SAVEPOINT {$savepointName}");
        } catch (PDOException) {
            // Savepoint may not exist if connection was lost
        }
        throw $e;
    }
}

// Usage with nested savepoints
$pdo->beginTransaction();
try {
    $pdo->exec("INSERT INTO accounts (id, balance) VALUES (1, 1000)");

    withSavepoint($pdo, function (PDO $pdo) {
        $pdo->exec("INSERT INTO transactions (account_id, amount) VALUES (1, -500)");
        $pdo->exec("UPDATE accounts SET balance = balance - 500 WHERE id = 1");
    });

    $pdo->commit();
} catch (Throwable $e) {
    $pdo->rollBack();
    throw $e;
}
```

### Solution 3: Implement Transaction Retry Logic

Handle deadlocks and transient transaction errors with automatic retry mechanisms.

```php
<?php
function executeInTransaction(
    PDO $pdo,
    callable $callback,
    int $maxRetries = 3
): mixed {
    $attempt = 0;

    while ($attempt < $maxRetries) {
        try {
            $pdo->beginTransaction();
            $result = $callback($pdo);
            $pdo->commit();
            return $result;
        } catch (PDOException $e) {
            $pdo->rollBack();
            $attempt++;

            // MySQL deadlock error code 1213
            if ($e->getCode() == '40001' || $e->getCode() == '1213') {
                if ($attempt < $maxRetries) {
                    usleep(100000 * $attempt); // backoff in microseconds
                    continue;
                }
            }
            throw $e;
        }
    }

    throw new RuntimeException('Transaction failed after ' . $maxRetries . ' attempts');
}

// Usage
$result = executeInTransaction($pdo, function (PDO $pdo) {
    $stmt = $pdo->prepare(
        'UPDATE accounts SET balance = balance - :amount WHERE id = :id AND balance >= :amount'
    );
    $stmt->execute([':amount' => 100, ':id' => 1]);
    return $stmt->rowCount();
});
```

## Prevention Tips

- Always call rollBack() when a transaction fails to clean up the connection state
- Keep transactions as short as possible to reduce lock contention on the database
- Use the $pdo->inTransaction() method to check if a transaction is active before operating on it

## Related Errors

- [PHP PDOException: SQLSTATE[HY000]]({{< relref "/languages/php/pdo-error" >}})
- [PHP PDO Connection Refused Error]({{< relref "/languages/php/pdo-connection-error" >}})
- [PHP PDO inTransaction Error]({{< relref "/languages/php/pdo-in-transaction" >}})
