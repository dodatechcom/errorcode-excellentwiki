---
title: "PHP Cannot call method on null"
description: "Fix PHP Fatal error: Cannot call method on null. Learn why method calls on null values fail and how to prevent them."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["null", "method-call", "fatal-error", "type-error", "non-object"]
weight: 5
---

# PHP Cannot call method on null

This fatal error occurs when you try to call a method on a variable that is null. In PHP 7, this produced a warning; in PHP 8.0+, it throws a fatal error or TypeError.

## Common Causes

- Function returns null instead of an expected object
- Variable was not initialized or assigned before method call
- Method chain breaks when an intermediate call returns null
- Object was unset or overwritten with null

## How to Fix

### Check for Null Before Calling Method

```php
<?php
$user = getUser($id);
if ($user !== null) {
    $name = $user->getName();
}
?>
```

### Use Null Operator (PHP 7.4+)

```php
<?php
$name = $user?->getName() ?? 'unknown';
?>
```

### Initialize Variables Properly

```php
<?php
$service = new DatabaseService();
// Ensure $service is never null before using it
$service->connect();
?>
```

### Validate Method Chains

```php
<?php
$db = new Database();
$connection = $db->getConnection();
// getConnection() might return null
if ($connection !== null) {
    $result = $connection->query('SELECT ...');
}
?>
```

## Examples

```php
<?php
// Example 1: Null return from function
function findUser($id) {
    if ($id > 0) {
        return new User($id);
    }
    return null;
}
$user = findUser(-1);
$user->getName();
// Fatal error: Cannot call method getName() on null
// Fix: if ($user !== null) { $user->getName(); }

// Example 2: Broken method chain
$result = $db->getConnection()->query('SELECT 1');
// Fatal error if getConnection() returns null
// Fix: break the chain and check each step

// Example 3: Unset object
$obj = new stdClass();
unset($obj);
$obj->doSomething();
// Fatal error: Cannot call method doSomething() on null
?>
```

## Related Errors

- [PHP Warning: Trying to get property of non-object]({{< relref "/languages/php/trying-to-get-property" >}})
- [PHP Fatal error: Call to undefined function]({{< relref "/languages/php/call-to-undefined" >}})
- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
