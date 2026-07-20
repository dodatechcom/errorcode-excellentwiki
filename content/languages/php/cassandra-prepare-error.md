---
title: "[Solution] PHP CASSANDRA_PREPARE_ERROR — Cassandra Prepared Statement Error"
description: "Fix PHP Cassandra prepared statement errors. Check parameter types, verify query, and handle binding. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 116
---

# PHP CASSANDRA_PREPARE_ERROR — Cassandra Prepared Statement Error

A Cassandra prepared statement failed. This error occurs when the CQL is invalid, parameter types are mismatched, the query cannot be prepared, or bound values do not match the prepared statement placeholders.

## Common Causes

### Invalid CQL in prepared statement

```php
<?php
$statement = $session->prepare(
    "INSERT INTO users (id, name) VALUES (?, ?)" // table does not exist
);
// Cassandra\Exception\InvalidQueryException
?>
```

### Wrong number of bind parameters

```php
<?php
$statement = $session->prepare(
    "INSERT INTO users (id, name, email) VALUES (?, ?)" // 3 placeholders, 2 params
);
$session->execute($statement, [Cassandra\UUID::uuid1(), 'Alice']);
// RuntimeException: Expected 3 bind variables, got 2
?>
```

### Type mismatch on bind

```php
<?php
$statement = $session->prepare(
    "SELECT * FROM users WHERE id = ?"
);
$session->execute($statement, ['not-a-uuid']);
// InvalidQueryException: cannot parse 'not-a-uuid' as a uuid
?>
```

### Preparing SELECT with invalid column

```php
<?php
$statement = $session->prepare(
    "SELECT nonexistent_column FROM users WHERE id = ?"
);
// InvalidQueryException: nonexistent_column does not exist
?>
```

### Re-preparing on closed session

```php
<?php
$session->close();
$statement = $session->prepare("SELECT * FROM users WHERE id = ?");
// SessionException: Session is closed
?>
```

## How to Fix

### Fix 1: Verify Table and Columns Before Preparing

```php
<?php
function safePrepare(Cassandra\Session $session, string $cql): Cassandra\Query\PreparedStatement
{
    try {
        return $session->prepare($cql);
    } catch (Cassandra\Exception\InvalidQueryException $e) {
        error_log("Failed to prepare statement: " . $e->getMessage());
        error_log("CQL: {$cql}");
        throw $e;
    }
}

$statement = safePrepare($session, "INSERT INTO users (id, name, email) VALUES (?, ?, ?)");
?>
```

### Fix 2: Match Bind Parameter Count

Ensure the number of `?` placeholders matches the bound values.

```php
<?php
// Correct — 3 placeholders, 3 values
$statement = $session->prepare(
    "INSERT INTO users (id, name, email) VALUES (?, ?, ?)"
);
$session->execute($statement, [
    Cassandra\UUID::uuid1(),
    'Alice',
    'alice@example.com',
]);

// Named parameters — use named placeholders
$statement = $session->prepare(
    "INSERT INTO users (id, name, email) VALUES (:id, :name, :email)"
);
$session->execute($statement, [
    'id' => Cassandra\UUID::uuid1(),
    'name' => 'Alice',
    'email' => 'alice@example.com',
]);
?>
```

### Fix 3: Use Correct Types for Bind Values

```php
<?php
use Cassandra\UUID;
use Cassandra\Timestamp;
use Cassandra\Varint;
use Cassandra\Decimal;
use Cassandra\Inet;

$statement = $session->prepare("
    INSERT INTO users (id, name, email, age, created_at, score, ip_address)
    VALUES (?, ?, ?, ?, ?, ?, ?)
");

$session->execute($statement, [
    UUID::uuid1(),           // UUID
    'Alice',                  // TEXT
    'alice@example.com',     // TEXT
    30,                       // INT
    new Timestamp(),         // TIMESTAMP
    95.5,                     // FLOAT/DOUBLE
    '192.168.1.100',          // INET
]);
?>
```

### Fix 4: Handle Reconnection and Re-preparation

```php
<?php
class CassandraStatementCache
{
    private Cassandra\Session $session;
    private array $cache = [];

    public function __construct(Cassandra\Session $session)
    {
        $this->session = $session;
    }

    public function prepare(string $cql): Cassandra\Query\PreparedStatement
    {
        $hash = md5($cql);

        if (!isset($this->cache[$hash])) {
            $this->cache[$hash] = $this->session->prepare($cql);
        }

        return $this->cache[$hash];
    }

    public function invalidate(): void
    {
        $this->cache = [];
    }
}

$cache = new CassandraStatementCache($session);

// Reuse prepared statements
$statement = $cache->prepare("SELECT * FROM users WHERE user_id = ?");
$result = $session->execute($statement, [Cassandra\UUID::uuid1()]);
?>
```

### Fix 5: Validate Prepared Statements

```php
<?php
function prepareAndValidate(
    Cassandra\Session $session,
    string $cql,
    array $expectedTypes
): Cassandra\Query\PreparedStatement {
    $statement = $session->prepare($cql);
    $metadata = $statement->bindings();

    $expectedCount = count($expectedTypes);
    $actualCount = count($metadata);

    if ($expectedCount !== $actualCount) {
        throw new RuntimeException(
            "Expected {$expectedCount} parameters, statement has {$actualCount}"
        );
    }

    return $statement;
}

$statement = prepareAndValidate($session,
    "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
    ['uuid', 'text', 'text']
);

$session->execute($statement, [
    Cassandra\UUID::uuid1(),
    'Alice',
    'alice@example.com',
]);
?>
```

## Examples

### Reusable Prepared Statement Pattern

```php
<?php
class UserRepository
{
    private Cassandra\Session $session;
    private Cassandra\Query\PreparedStatement $findByIdStmt;
    private Cassandra\Query\PreparedStatement $insertStmt;
    private Cassandra\Query\PreparedStatement $findByEmailStmt;

    public function __construct(Cassandra\Session $session)
    {
        $this->session = $session;
        $this->findByIdStmt = $session->prepare(
            "SELECT * FROM users WHERE user_id = ?"
        );
        $this->insertStmt = $session->prepare(
            "INSERT INTO users (user_id, name, email, created_at) VALUES (?, ?, ?, ?)"
        );
        $this->findByEmailStmt = $session->prepare(
            "SELECT * FROM users_by_email WHERE email = ?"
        );
    }

    public function findById(Cassandra\UUID $id): ?array
    {
        $result = $this->session->execute($this->findByIdStmt, [$id]);
        return $result->count() > 0 ? $result->first() : null;
    }

    public function findByEmail(string $email): ?array
    {
        $result = $this->session->execute($this->findByEmailStmt, [$email]);
        return $result->count() > 0 ? $result->first() : null;
    }

    public function create(string $name, string $email): Cassandra\UUID
    {
        $id = Cassandra\UUID::uuid1();
        $this->session->execute($this->insertStmt, [
            $id, $name, $email, new Cassandra\Timestamp(),
        ]);
        return $id;
    }
}

$repo = new UserRepository($session);
$user = $repo->findById(Cassandra\UUID::uuid1());
?>
```

## Related Errors

- [Cassandra Query Error]({{< relref "/languages/php/cassandra-query-error" >}})
- [Cassandra Connection Error]({{< relref "/languages/php/cassandra-connection-error" >}})
- [Cassandra Timeout Error]({{< relref "/languages/php/cassandra-timeout-error" >}})
