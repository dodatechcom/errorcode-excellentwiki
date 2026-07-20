---
title: "[Solution] PHP InvalidArgumentException — Function Argument Is Invalid"
description: "Fix PHP InvalidArgumentException by validating input, checking type and value, and using proper assertions."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# InvalidArgumentException — Function Argument Is Invalid

This exception is thrown when a function argument does not meet the expected type or value requirements. It indicates that the caller passed an argument that is semantically incorrect, such as a negative number where a positive one is required, an empty string where content is expected, or a wrong data type in non-strict mode.

## Common Causes

- Wrong data type passed to a function (e.g., string instead of int)
- Value is null when a non-null value is required
- Argument is empty when content is mandatory
- Number outside acceptable bounds passed as parameter

## How to Fix

### Fix 1: Validate Input Type and Value

Check both the type and the value of the argument before using it.

```php
<?php
function setAge(int $age): void
{
    if (!is_int($age) || $age < 0 || $age > 150) {
        throw new InvalidArgumentException("Invalid age: $age");
    }
    $this->age = $age;
}
?>
```

### Fix 2: Use Strict Type Declarations

Enable strict types to catch type mismatches automatically.

```php
<?php
declare(strict_types=1);

function processAmount(float $amount): float
{
    // Type is enforced — passing a string causes TypeError, not InvalidArgumentException
    return $amount * 1.1;
}
?>
```

### Fix 3: Use assert() for Precondition Checks

Use assertions during development to validate assumptions about input.

```php
<?php
function divide(float $a, float $b): float
{
    assert($b !== 0, "Divisor cannot be zero");
    return $a / $b;
}
?>
```

### Fix 4: Create a Validation Helper

Build reusable validation functions to reduce boilerplate.

```php
<?php
function requireNonEmpty(string $value, string $name): void
{
    if (trim($value) === '') {
        throw new InvalidArgumentException("$name cannot be empty");
    }
}

function requirePositive(int $value, string $name): void
{
    if ($value <= 0) {
        throw new InvalidArgumentException("$name must be positive, got $value");
    }
}

// Usage
requireNonEmpty($input, 'username');
requirePositive($quantity, 'quantity');
?>
```

## Examples

```php
<?php
// Example 1: Empty string where required
createUser('');
// InvalidArgumentException: Username cannot be empty
// Fix: validate non-empty before calling

// Example 2: Wrong type in non-strict mode
function add(int $a, int $b) { return $a + $b; }
add('hello', 5);
// InvalidArgumentException or TypeError depending on strict_types
// Fix: use declare(strict_types=1)

// Example 3: Null where non-null expected
saveRecord(null);
// InvalidArgumentException: Record cannot be null
// Fix: check $record !== null before passing
?>
```

## Related Errors

- [PHP DomainException]({{< relref "/languages/php/domainexception" >}})
- [PHP LengthException]({{< relref "/languages/php/lengthexception" >}})
- [PHP OutOfRangeException]({{< relref "/languages/php/outofrangeexception" >}})
