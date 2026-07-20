---
title: "[Solution] PHP OutOfRangeException — Argument Outside Valid Range"
description: "Fix PHP OutOfRangeException by validating range before use, using min/max, and checking boundaries."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# OutOfRangeException — Argument Outside Valid Range

This exception is thrown when an argument value is outside the acceptable range of valid values. Unlike OutOfBoundsException (which relates to index/key access), OutOfRangeException indicates that a scalar value (integer, float, enum, etc.) falls outside the permitted boundaries for a given operation.

## Common Causes

- Numeric value exceeds minimum or maximum allowed limits
- Enum or constant value not in the defined set of valid options
- Date or time value outside supported range
- Argument valid in type but outside acceptable numeric or categorical range

## How to Fix

### Fix 1: Validate Range Before Use

Check that values fall within the acceptable range before using them.

```php
<?php
function setVolume(int $level): void
{
    if ($level < 0 || $level > 100) {
        throw new OutOfRangeException(
            "Volume level must be between 0 and 100, got $level"
        );
    }
    $this->volume = $level;
}
?>
```

### Fix 2: Use min/max Clamping

Clamp values to the valid range to prevent out-of-range errors.

```php
<?php
function clamp(int $value, int $min, int $max): int
{
    return max($min, min($max, $value));
}

// Usage
$volume = clamp($input, 0, 100); // Always 0-100
?>
```

### Fix 3: Validate Against Allowed Constants or Enums

Check that values match one of the predefined valid options.

```php
<?php
const VALID_STATUSES = ['pending', 'active', 'closed'];

function setStatus(string $status): void
{
    if (!in_array($status, VALID_STATUSES, true)) {
        throw new OutOfRangeException(
            "Invalid status '$status'. Allowed: " . implode(', ', VALID_STATUSES)
        );
    }
    $this->status = $status;
}
?>
```

### Fix 4: Validate Date/Time Ranges

Check that date and time values fall within supported ranges.

```php
<?php
function setDate(int $year, int $month, int $day): void
{
    if ($year < 1900 || $year > 2100) {
        throw new OutOfRangeException("Year must be between 1900 and 2100, got $year");
    }

    if ($month < 1 || $month > 12) {
        throw new OutOfRangeException("Month must be between 1 and 12, got $month");
    }

    if ($day < 1 || $day > cal_days_in_month(CAL_GREGORIAN, $month, $year)) {
        throw new OutOfRangeException("Invalid day $day for month $month/$year");
    }
}
?>
```

## Examples

```php
<?php
// Example 1: Page number out of range
$pagination->getPage(0);
// OutOfRangeException: Page must be >= 1
// Fix: validate $page >= 1 && $page <= $totalPages

// Example 2: Month out of range
$date->setMonth(13);
// OutOfRangeException: Month must be between 1 and 12
// Fix: check $month >= 1 && $month <= 12

// Example 3: Invalid enum value
$order->setPriority(5);
// OutOfRangeException: Priority must be LOW, MEDIUM, or HIGH
// Fix: validate against allowed constant values
?>
```

## Related Errors

- [PHP OutOfBoundsException]({{< relref "/languages/php/outofboundsexception" >}})
- [PHP RangeException]({{< relref "/languages/php/rangeexception" >}})
- [PHP InvalidArgumentException]({{< relref "/languages/php/invalidargumentexception" >}})
