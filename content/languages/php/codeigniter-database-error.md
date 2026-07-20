---
title: "[Solution] PHP CODEIGNITER_DATABASE_ERROR — Database Query Failed"
description: "Fix PHP CODEIGNITER_DATABASE_ERROR by checking config, query syntax, and error logging. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 100
---

# PHP CODEIGNITER_DATABASE_ERROR — Database Query Failed

A database query failed in CodeIgniter. This error occurs when the database connection cannot be established, the query syntax is invalid, or the target table/column does not exist.

## Common Causes

```php
// Wrong database config in application/config/database.php
$db['default'] = [
    'hostname' => 'localhost',
    'username' => 'wrong_user',
    'password' => 'wrong_pass',
    'database' => 'wrong_db',
    'dbdriver' => 'mysqli',
];
```

```php
// Invalid query syntax
$this->db->query("SELECT * FROM users WHERE id ="); // syntax error
```

```php
// Table does not exist
$this->db->query("SELECT * FROM nonexistent_table");
```

```php
// Using active record incorrectly
$this->db->select('*');
$this->db->from('users');
$this->db->where('id =', $id); // wrong syntax for where clause
$query = $this->db->get(); // may fail if chained incorrectly
```

```php
// Connection timeout or refused
// Database server is not running or unreachable
```

## How to Fix

### Fix 1: Check Database Configuration

Verify `application/config/database.php` credentials and settings.

```php
$db['default'] = [
    'hostname' => 'localhost',
    'username' => 'your_actual_user',
    'password' => 'your_actual_password',
    'database' => 'your_actual_database',
    'dbdriver' => 'mysqli',
    'dbprefix' => '',
    'pconnect' => false,
    'db_debug' => true,
    'cache_on' => false,
    'cachedir' => '',
    'char_set' => 'utf8mb4',
    'dbcollat' => 'utf8mb4_general_ci',
    'swap_pre' => '',
    'autoinit' => true,
    'stricton' => false,
    'failover' => [],
];
```

### Fix 2: Verify Query Syntax

Use proper query syntax or query builder methods.

```php
// Raw query with parameter binding
$query = $this->db->query("SELECT * FROM users WHERE id = ?", [$id]);

// Query builder equivalent
$query = $this->db->select('*')
    ->from('users')
    ->where('id', $id)
    ->get();

if ($query->num_rows() > 0) {
    foreach ($query->result() as $row) {
        echo $row->name;
    }
} else {
    echo "No results found.";
}
```

### Fix 3: Enable Error Logging and Debug Mode

Enable detailed error reporting to diagnose issues.

```php
// In index.php or environment config
error_reporting(E_ALL);
ini_set('display_errors', 1);

// In database config
'db_debug' => TRUE,

// Check application/logs/ for error logs
// Ensure log_threshold is set in application/config/config.php
$config['log_threshold'] = 1; // 0 = off, 1 = errors, 2 = debug
```

### Fix 4: Use Query Builder for Safety

```php
// Insert with query builder
$data = [
    'name'  => $name,
    'email' => $email,
    'created' => date('Y-m-d H:i:s'),
];
$this->db->insert('users', $data);

// Check for errors after operation
if ($this->db->affected_rows() === 0) {
    log_message('error', 'Insert failed: ' . $this->db->error()['message']);
}

// Update with query builder
$this->db->where('id', $id);
$this->db->update('users', $data);

// Transaction handling
$this->db->trans_start();
$this->db->query("UPDATE accounts SET balance = balance - 100 WHERE id = 1");
$this->db->query("UPDATE accounts SET balance = balance + 100 WHERE id = 2");
$this->db->trans_complete();

if ($this->db->trans_status() === false) {
    log_message('error', 'Transaction failed');
}
```

## Examples

```php
// Full example with error handling
class UserModel extends CI_Model {

    public function getUser($id) {
        $query = $this->db->get_where('users', ['id' => $id]);

        if ($query->num_rows() > 0) {
            return $query->row_array();
        }

        return null;
    }

    public function insertUser($data) {
        if ($this->db->insert('users', $data)) {
            return $this->db->insert_id();
        }

        log_message('error', 'Insert failed: ' . $this->db->error()['message']);
        return false;
    }
}
```

## Related Errors

- [PDO Connection Error](/languages/php/pdo-connection-error)
- [PDO Error](/languages/php/pdo-error)
- [Laravel Migration Error](/languages/php/laravel-migration-error)
- [Symfony Messenger Error](/languages/php/symfony-messenger-error)
