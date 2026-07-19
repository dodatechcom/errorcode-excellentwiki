---
title: "[Solution] PHP Enum Serialization Error Fix"
description: "Fix 'Enum cannot be serialized' errors in PHP 8.1+. Learn proper enum handling, backed enums, and serialization."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php81", "enums", "serialization", "runtime-error"]
severity: "error"
---

# Enum Cannot Be Serialized

## Error Message

```
Uncaught TypeError: Cannot serialize 'Color' enum in /path/to/file.php:12
```

## Common Causes

- Attempting to serialize a unit enum directly with serialize() or json_encode()
- Passing a unit enum to session storage which serializes values internally
- Using var_export() or print_r() on a unit enum which attempts serialization
- Storing enums in caches like Redis or Memcached that call serialize() internally

## Solutions

### Solution 1: Use backed enums for serialization

Backed enums carry a string or int value that can be serialized and stored easily.

```php
<?php
// WRONG: Unit enum cannot be serialized
enum Color {
    case Red;
    case Green;
    case Blue;
}

// CORRECT: Backed enum has a serializable value
enum Status: string {
    case Pending   = 'pending';
    case Active    = 'active';
    case Completed = 'completed';
}

$status = Status::Active;
echo $status->value; // 'active' — this can be serialized
echo json_encode($status); // '"active"'
?>
```

### Solution 2: Serialize the enum value, not the enum itself

When storing enums in databases or caches, store the ->value property instead of the enum object.

```php
<?php
enum Priority: int {
    case Low    = 1;
    case Medium = 2;
    case High   = 3;
}

$priority = Priority::High;

// Store in database
$db->save(['priority' => $priority->value]); // stores 3

// Retrieve and restore
$row = $db->load($id);
$restored = Priority::from($row['priority']); // Priority::High
?>
```

### Solution 3: Create a custom serialization interface

For complex enum usage, implement __serialize() and __unserialize() or use a wrapper class.

```php
<?php
enum Permission: string {
    case Read    = 'read';
    case Write   = 'write';
    case Execute = 'execute';
}

class EnumWrapper {
    public function __construct(
        public readonly string $enumClass,
        public readonly string $value,
    ) {}

    public static function fromEnum(Enum $e): self {
        return new self(get_class($e), $e->value);
    }

    public function toEnum(): Enum {
        return $this->enumClass::from($this->value);
    }
}

$wrapper = EnumWrapper::fromEnum(Permission::Write);
$serialized = serialize($wrapper);
$restored = unserialize($serialized)->toEnum();
var_dump($restored); // Permission::Write
?>
```

## Prevention Tips

- Prefer backed enums (string or int) for any enum that needs to be stored or transmitted
- Always use Enum::from() or Enum::tryFrom() to restore backed enums from stored values
- Avoid passing raw enum objects to session handlers, caches, or database layers
- Unit enums are best for internal state machines that don't need external persistence

## Related Errors

- [PHP Readonly Property Error]({{< relref "/languages/php/php81-readonly-property" >}})
- [PHP Fiber Error]({{< relref "/languages/php/php81-fiber-error" >}})
- [PHP Deprecated Function Usage]({{< relref "/languages/php/php-deprecated" >}})
