---
title: "PHP Warning: Trying to get property of non-object"
description: "Fix PHP Trying to get property of non-object warning. Learn why this occurs with null or non-object variables."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["warning", "non-object", "property-access", "null"]
weight: 5
---

# PHP Warning: Trying to get property of non-object

This warning occurs when you try to access a property on a variable that is not an object. In PHP 7.4+, this produces a warning; in PHP 8.0+, accessing a property on null throws a fatal error.

## Common Causes

- Variable is null instead of an expected object (e.g., failed database query)
- Function returns null or false instead of an object
- Array was passed where an object was expected
- Object not properly initialized before property access

## How to Fix

### Check Variable Type Before Access

```php
<?php
$user = getUserFromDatabase($id);
if (is_object($user)) {
    $name = $user->name;
}
?>
```

### Use the Null Operator (PHP 7.4+)

```php
<?php
$name = $user?->name ?? 'default';
?>
```

### Verify Database Query Results

```php
<?php
$result = $db->query("SELECT * FROM users WHERE id = 1");
$row = $result->fetchObject();
if ($row) {
    echo $row->name;
}
?>
```

### Use instanceof Check

```php
<?php
if ($obj instanceof User) {
    echo $obj->getFullName();
}
?>
```

## Examples

```php
<?php
// Example 1: Null variable
$user = null;
echo $user->name;
// Warning: Trying to get property 'name' of non-object
// Fix: check if user is not null first

// Example 2: Array passed instead of object
$config = ['host' => 'localhost'];
echo $config->host;
// Warning: Trying to get property 'host' of non-object
// Fix: use $config['host'] instead

// Example 3: Failed query
$result = $db->query("SELECT * FROM users WHERE id = 999");
$user = $result->fetchObject();
echo $user->name;
// Warning: Trying to get property 'name' of non-object (user is false)
// Fix: if ($user) { echo $user->name; }
?>
```

## Related Errors

- [PHP Notice: Undefined Variable]({{< relref "/languages/php/notice-undefined-variable" >}})
- [PHP Fatal error: Call to undefined function]({{< relref "/languages/php/call-to-undefined" >}})
- [PHP Fatal Error: Allowed memory size exhausted]({{< relref "/languages/php/fatal-error" >}})
