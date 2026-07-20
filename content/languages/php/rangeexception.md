---
title: "[Solution] PHP RangeException — Value Outside Valid Range"
description: "Fix PHP RangeException by validating input range, using proper bounds checking, and handling edge cases."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# RangeException — Value Outside Valid Range

This exception is thrown when a value falls outside the valid range for a given operation. It indicates that the argument is within the correct type but its value is not in the acceptable range. RangeException is commonly used for domain-specific range violations, distinguishing it from OutOfRangeException which typically relates to index or key operations.

## Common Causes

- Value is below the minimum threshold
- Value exceeds the maximum allowed limit
- Date or time outside supported range
- Percentage, ratio, or proportion outside 0-1 bounds

## How to Fix

### Fix 1: Validate Input Range

Check that values fall within acceptable boundaries before using them.

```php
<?php
function setDiscount(float $percentage): void
{
    if ($percentage < 0 || $percentage > 100) {
        throw new RangeException(
            "Discount must be between 0% and 100%, got {$percentage}%"
        );
    }
    $this->discount = $percentage;
}
?>
```

### Fix 2: Use Proper Bounds Checking with Tolerance

For floating-point comparisons, use a small tolerance for precision.

```php
<?php
function setRatio(float $ratio): void
{
    $epsilon = 0.0001;
    if ($ratio < -$epsilon || $ratio > (1.0 + $epsilon)) {
        throw new RangeException(
            "Ratio must be between 0.0 and 1.0, got $ratio"
        );
    }
    $this->ratio = $ratio;
}
?>
```

### Fix 3: Validate Against Constraints

Check multiple constraints simultaneously.

```php
<?php
function createEvent(DateTime $start, DateTime $end): void
{
    $now = new DateTime();

    if ($start < $now) {
        throw new RangeException("Event start must be in the future");
    }

    if ($end <= $start) {
        throw new RangeException("Event end must be after start");
    }

    $maxDuration = new DateInterval('P30D');
    $duration = $start->diff($end);

    if ($duration > $maxDuration) {
        throw new RangeException("Event cannot last more than 30 days");
    }
}
?>
```

### Fix 4: Handle Edge Cases at Boundaries

Define explicit behavior for boundary values.

```php
<?php
function normalizeIndex(int $index, int $count): int
{
    if ($count === 0) {
        throw new RangeException("Cannot normalize index for empty collection");
    }

    if ($index < 0 || $index >= $count) {
        throw new RangeException(
            "Index $index out of range for collection of size $count"
        );
    }

    return $index;
}
?>
```

## Examples

```php
<?php
// Example 1: Percentage out of range
$slider->setValue(150);
// RangeException: Value must be between 0 and 100
// Fix: validate $value >= 0 && $value <= 100

// Example 2: Date range violation
$scheduler->schedule($pastDate, $futureDate);
// RangeException: Start date cannot be in the past
// Fix: check $start >= new DateTime()

// Example 3: Numeric range for configuration
$config->setRetries(-1);
// RangeException: Retries must be between 0 and 10
// Fix: validate $retries >= 0 && $retries <= 10
?>
```

## Related Errors

- [PHP OutOfRangeException]({{< relref "/languages/php/outofrangeexception" >}})
- [PHP InvalidArgumentException]({{< relref "/languages/php/invalidargumentexception" >}})
- [PHP DomainException]({{< relref "/languages/php/domainexception" >}})
