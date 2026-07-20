---
title: "[Solution] PHP CASSANDRA_KEYSPACE_ERROR — Cassandra Keyspace Error"
description: "Fix PHP Cassandra keyspace errors. Check keyspace name, verify replication, and create keyspace. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 115
---

# PHP CASSANDRA_KEYSPACE_ERROR — Cassandra Keyspace Error

A Cassandra keyspace operation failed. This error occurs when the keyspace does not exist, replication configuration is invalid, the keyspace name is incorrect, or permissions are insufficient for keyspace operations.

## Common Causes

### Keyspace does not exist

```php
<?php
$cluster = Cassandra::cluster()
    ->withContactPoints('127.0.0.1')
    ->withPort(9042)
    ->build();
$session = $cluster->connect('nonexistent_keyspace');
// Cassandra\Exception\InvalidKeyspaceException
?>
```

### Invalid replication strategy

```php
<?php
$session->execute(new Cassandra\Query\SimpleQuery("
    CREATE KEYSPACE mykeyspace WITH replication = {
        'class': 'NetworkTopologyStrategy'
    }
"));
// InvalidRequestException — NetworkTopologyStrategy requires datacenter configuration
?>
```

### Wrong keyspace name case

```php
<?php
$session->execute(new Cassandra\Query\SimpleQuery(
    "SELECT * FROM MyKeyspace.users"
));
// InvalidRequestException — keyspace names are case-sensitive when quoted
?>
```

### Insufficient permissions

```php
<?php
$session->execute(new Cassandra\Query\SimpleQuery("
    CREATE KEYSPACE admin_keyspace WITH replication = {
        'class': 'SimpleStrategy', 'replication_factor': 3
    }
"));
// UnauthorizedException — user does not have CREATE permission
?>
```

### Replication factor exceeds node count

```php
<?php
$session->execute(new Cassandra\Query\SimpleQuery("
    CREATE KEYSPACE mykeyspace WITH replication = {
        'class': 'SimpleStrategy', 'replication_factor': 5
    }
"));
// Warning: RF 5 with only 3 nodes — data availability risk
?>
```

## How to Fix

### Fix 1: Create Keyspace If Not Exists

```php
<?php
function ensureKeyspace(Cassandra\Session $session, string $keyspace): void
{
    $rows = $session->execute(new Cassandra\Query\SimpleQuery(
        "SELECT keyspace_name FROM system_schema.keyspaces WHERE keyspace_name = ?",
        [$keyspace]
    ));

    if ($rows->count() === 0) {
        $session->execute(new Cassandra\Query\SimpleQuery("
            CREATE KEYSPACE IF NOT EXISTS {$keyspace}
            WITH replication = {
                'class': 'SimpleStrategy',
                'replication_factor': 1
            }
        "));
        error_log("Created keyspace: {$keyspace}");
    }
}

ensureKeyspace($session, 'myapp');
$session = $cluster->connect('myapp');
?>
```

### Fix 2: Use Correct Replication Strategy

```php
<?php
// SimpleStrategy — for single datacenter
$session->execute(new Cassandra\Query\SimpleQuery("
    CREATE KEYSPACE IF NOT EXISTS myapp
    WITH replication = {
        'class': 'SimpleStrategy',
        'replication_factor': 3
    }
"));

// NetworkTopologyStrategy — for multi-datacenter
$session->execute(new Cassandra\Query\SimpleQuery("
    CREATE KEYSPACE IF NOT EXISTS myapp
    WITH replication = {
        'class': 'NetworkTopologyStrategy',
        'us-east': 3,
        'eu-west': 2
    }
"));
?>
```

### Fix 3: Verify Keyspace Before Use

```php
<?php
function getKeyspaces(Cassandra\Session $session): array
{
    $result = $session->execute(new Cassandra\Query\SimpleQuery(
        "SELECT keyspace_name FROM system_schema.keyspaces"
    ));
    $keyspaces = [];
    foreach ($result as $row) {
        $keyspaces[] = $row['keyspace_name'];
    }
    return $keyspaces;
}

function useKeyspace(Cassandra\Session $session, string $keyspace): void
{
    $available = getKeyspaces($session);
    if (!in_array($keyspace, $available)) {
        throw new RuntimeException(
            "Keyspace '{$keyspace}' does not exist. Available: " . implode(', ', $available)
        );
    }
    $session->execute(new Cassandra\Query\SimpleQuery("USE {$keyspace}"));
}

useKeyspace($session, 'myapp');
?>
```

### Fix 4: Handle Keyspace Name Correctly

```php
<?php
// Keyspace names should be lowercase and use underscores
$validName = 'my_app_keyspace';
$invalidName = 'MyAppKeyspace'; // avoid mixed case

// If you must use case-sensitive names, quote them
$session->execute(new Cassandra\Query\SimpleQuery(
    'USE "MyCaseSensitiveKeyspace"'
));

// Best practice: use lowercase with underscores
$session->execute(new Cassandra\Query\SimpleQuery(
    'USE my_app_keyspace'
));
?>
```

### Fix 5: Alter Existing Keyspace

```php
<?php
function updateKeyspaceReplication(Cassandra\Session $session, string $keyspace, array $replication): void
{
    $replicationStr = "'class': '{$replication['class']}'";
    foreach ($replication as $key => $value) {
        if ($key !== 'class') {
            $replicationStr .= ", '{$key}': {$value}";
        }
    }

    $session->execute(new Cassandra\Query\SimpleQuery(
        "ALTER KEYSPACE {$keyspace} WITH replication = { {$replicationStr} }"
    ));
    error_log("Updated keyspace {$keyspace} replication");
}

updateKeyspaceReplication($session, 'myapp', [
    'class' => 'NetworkTopologyStrategy',
    'us-east' => 3,
    'eu-west' => 2,
]);
?>
```

## Examples

### Complete Keyspace Management

```php
<?php
class KeyspaceManager
{
    private Cassandra\Session $session;

    public function __construct(Cassandra\Session $session)
    {
        $this->session = $session;
    }

    public function createIfNotExists(string $name, array $replication): void
    {
        $existing = $this->list();
        if (in_array($name, $existing)) {
            return;
        }

        $replicationStr = "'class': '{$replication['class']}'";
        foreach ($replication as $key => $value) {
            if ($key !== 'class') {
                $replicationStr .= ", '{$key}': {$value}";
            }
        }

        $this->session->execute(new Cassandra\Query\SimpleQuery(
            "CREATE KEYSPACE {$name} WITH replication = { {$replicationStr} }"
        ));
    }

    public function list(): array
    {
        $result = $this->session->execute(new Cassandra\Query\SimpleQuery(
            "SELECT keyspace_name FROM system_schema.keyspaces"
        ));
        $keyspaces = [];
        foreach ($result as $row) {
            $keyspaces[] = $row['keyspace_name'];
        }
        return $keyspaces;
    }

    public function drop(string $name): void
    {
        $this->session->execute(new Cassandra\Query\SimpleQuery(
            "DROP KEYSPACE IF EXISTS {$name}"
        ));
    }
}

$manager = new KeyspaceManager($session);
$manager->createIfNotExists('myapp', [
    'class' => 'SimpleStrategy',
    'replication_factor' => 3,
]);
?>
```

## Related Errors

- [Cassandra Connection Error]({{< relref "/languages/php/cassandra-connection-error" >}})
- [Cassandra Query Error]({{< relref "/languages/php/cassandra-query-error" >}})
- [Cassandra Prepare Error]({{< relref "/languages/php/cassandra-prepare-error" >}})
