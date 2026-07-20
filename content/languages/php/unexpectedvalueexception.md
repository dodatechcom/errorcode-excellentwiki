---
title: "[Solution] PHP UnexpectedValueException — Unexpected Type or Value"
description: "Fix PHP UnexpectedValueException by validating input type, using type checking, and handling unexpected cases."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# UnexpectedValueException — Unexpected Type or Value

This exception is thrown when a value has an unexpected type or is not among the expected possible values. It commonly occurs when iterating over generators, parsing data, or processing collections where items do not match the expected schema or type.

## Common Causes

- Generator yields unexpected type of value
- Data from external source does not match expected schema
- Configuration value is not one of the allowed options
- Parsed data contains unexpected data types in expected positions

## How to Fix

### Fix 1: Validate Input Type Before Processing

Check the type of incoming data before using it.

```php
<?php
function processItem($item): string
{
    if (!is_string($item)) {
        throw new UnexpectedValueException(
            "Expected string, got " . gettype($item) .
            (is_object($item) ? " (" . get_class($item) . ")" : "")
        );
    }
    return strtoupper($item);
}
?>
```

### Fix 2: Use Type Checking in Generators

Validate types when consuming generator results.

```php
<?php
function getValidItems(Generator $generator): array
{
    $items = [];
    foreach ($generator as $key => $value) {
        if (!is_int($value)) {
            throw new UnexpectedValueException(
                "Generator yielded unexpected type at key '$key': " .
                "expected int, got " . gettype($value)
            );
        }
        $items[] = $value;
    }
    return $items;
}
?>
```

### Fix 3: Handle Unexpected Cases Gracefully

Use default cases in switches and fallbacks for unexpected values.

```php
<?php
function handleStatus(string $status): void
{
    switch ($status) {
        case 'pending':
            $this->handlePending();
            break;
        case 'active':
            $this->handleActive();
            break;
        case 'closed':
            $this->handleClosed();
            break;
        default:
            throw new UnexpectedValueException(
                "Unexpected status value: '$status'. " .
                "Expected: pending, active, or closed"
            );
    }
}
?>
```

### Fix 4: Validate Schema of Parsed Data

Check data structure after parsing from JSON or XML.

```php
<?php
function parseUser(string $json): array
{
    $data = json_decode($json, true);

    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new UnexpectedValueException("Invalid JSON: " . json_last_error_msg());
    }

    if (!is_array($data)) {
        throw new UnexpectedValueException(
            "Expected JSON object, got " . gettype($data)
        );
    }

    $required = ['name', 'email'];
    foreach ($required as $field) {
        if (!isset($data[$field]) || !is_string($data[$field])) {
            throw new UnexpectedValueException(
                "Missing or invalid field '$field' in user data"
            );
        }
    }

    return $data;
}
?>
```

## Examples

```php
<?php
// Example 1: Unexpected generator yield
function idGenerator(): Generator {
    yield 1;
    yield 'two'; // Unexpected type
    yield 3;
}
$items = array_iterator_to_array(idGenerator());
// UnexpectedValueException: expected int, got string at key 1
// Fix: validate types within generator

// Example 2: Unexpected JSON structure
$data = json_decode('[1, 2, 3]', true);
$result = processUser($data);
// UnexpectedValueException: Expected JSON object, got array
// Fix: check is_array($data) and validate structure

// Example 3: Unexpected enum value
$order->setStatus('invalid_status');
// UnexpectedValueException: Not a valid OrderStatus
// Fix: validate against allowed values before assignment
?>
```

## Related Errors

- [PHP InvalidArgumentException]({{< relref "/languages/php/invalidargumentexception" >}})
- [PHP DomainException]({{< relref "/languages/php/domainexception" >}})
- [PHP LogicException]({{< relref "/languages/php/logicexception" >}})
