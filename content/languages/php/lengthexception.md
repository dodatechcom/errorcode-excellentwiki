---
title: "[Solution] PHP LengthException — Invalid Length or Size"
description: "Fix PHP LengthException by validating array/string length, checking boundaries, and using proper length validation."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# LengthException — Invalid Length or Size

This exception is thrown when a length or size parameter is invalid, such as an array with too few or too many elements, a string that exceeds maximum allowed length, or a buffer that is the wrong size. It is commonly used when data does not meet required size constraints.

## Common Causes

- Array has fewer or more elements than expected
- Input string exceeds maximum allowed length
- Buffer size does not match required dimensions
- Collection size violates minimum or maximum constraints

## How to Fix

### Fix 1: Validate Array Length Before Use

Check `count()` before processing arrays with expected sizes.

```php
<?php
function processCoordinates(array $points): void
{
    if (count($points) !== 3) {
        throw new LengthException(
            "Expected exactly 3 coordinates, got " . count($points)
        );
    }

    [$x, $y, $z] = $points;
}
?>
```

### Fix 2: Check String Length Constraints

Validate string length before storing or processing.

```php
<?php
function setUsername(string $username): void
{
    $length = strlen($username);

    if ($length < 3) {
        throw new LengthException("Username must be at least 3 characters, got $length");
    }

    if ($length > 50) {
        throw new LengthException("Username must not exceed 50 characters, got $length");
    }

    $this->username = $username;
}
?>
```

### Fix 3: Enforce Collection Size Boundaries

Use min/max constraints on collections.

```php
<?php
function createTeam(array $members): Team
{
    $count = count($members);

    if ($count < 2) {
        throw new LengthException("Team requires at least 2 members, got $count");
    }

    if ($count > 10) {
        throw new LengthException("Team cannot have more than 10 members, got $count");
    }

    return new Team($members);
}
?>
```

### Fix 4: Validate Binary Data Length

Ensure binary or encoded data has the expected length.

```php
<?php
function decodeMessage(string $encoded): string
{
    $length = strlen($encoded);

    if ($length % 4 !== 0) {
        throw new LengthException(
            "Encoded message length must be divisible by 4, got $length"
        );
    }

    return base64_decode($encoded);
}
?>
```

## Examples

```php
<?php
// Example 1: Array with wrong number of elements
$rgb = [255, 128]; // Missing third value
new Color($rgb);
// LengthException: Expected exactly 3 RGB values, got 2
// Fix: validate count($rgb) === 3

// Example 2: Password too short
setPassword('abc');
// LengthException: Password must be at least 8 characters, got 3
// Fix: check strlen($password) >= 8

// Example 3: Too many arguments in matrix
$matrix = [[1, 2, 3], [4, 5]];
validateMatrix($matrix);
// LengthException: All rows must have equal length
// Fix: check count of each row
?>
```

## Related Errors

- [PHP InvalidArgumentException]({{< relref "/languages/php/invalidargumentexception" >}})
- [PHP OutOfBoundsException]({{< relref "/languages/php/outofboundsexception" >}})
- [PHP RangeException]({{< relref "/languages/php/rangeexception" >}})
