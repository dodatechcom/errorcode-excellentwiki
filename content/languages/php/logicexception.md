---
title: "[Solution] PHP LogicException — Logic Error in Program"
description: "Fix PHP LogicException by reviewing program logic, fixing algorithms, and handling edge cases properly."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# LogicException — Logic Error in Program

This exception indicates a logic error in the program — a bug that should never occur if the code is working correctly. Unlike RuntimeException, which represents errors caused by external factors, LogicException signals problems in the program's logic itself, such as invalid state transitions, broken invariants, or unreachable code paths.

## Common Causes

- Invalid object state when a method is called
- Broken invariants after operations (e.g., a sorted array that is not sorted)
- Invalid state transitions in state machines
- Unreachable code paths reached due to logic bugs

## How to Fix

### Fix 1: Review Program Logic and State

Ensure objects are in valid states before performing operations.

```php
<?php
class Order
{
    private string $status = 'pending';

    public function ship(): void
    {
        if ($this->status !== 'paid') {
            throw new LogicException(
                "Cannot ship an order that is not paid. Current status: {$this->status}"
            );
        }
        $this->status = 'shipped';
    }
}
?>
```

### Fix 2: Fix Algorithm and Invariant Violations

Validate that invariants hold after operations.

```php
<?php
function sortAndVerify(array &$data): void
{
    sort($data);

    for ($i = 1; $i < count($data); $i++) {
        if ($data[$i] < $data[$i - 1]) {
            throw new LogicException(
                "Array is not sorted correctly at index $i"
            );
        }
    }
}
?>
```

### Fix 3: Handle Edge Cases Properly

Account for boundary conditions and edge cases in your logic.

```php
<?php
function getMiddleElement(array $items)
{
    if (empty($items)) {
        throw new LogicException("Cannot get middle element of empty array");
    }

    $index = (int) (count($items) / 2);
    return $items[$index];
}
?>
```

### Fix 4: Use Assertions During Development

Add assertions to catch logic errors early during development.

```php
<?php
function processBuffer(string $buffer, int $expectedSize): void
{
    assert(strlen($buffer) === $expectedSize, "Buffer size mismatch");

    // Process buffer
    for ($i = 0; $i < $expectedSize; $i++) {
        assert(isset($buffer[$i]), "Buffer index $i should exist");
    }
}
?>
```

## Examples

```php
<?php
// Example 1: Invalid state transition
$order = new Order();
$order->ship();
// LogicException: Cannot ship an order that is not paid
// Fix: check order state before transition

// Example 2: Broken invariant
$cache = new SortedCache();
$cache->add(5);
$cache->add(3);
$cache->getMin();
// LogicException: Cache is not sorted after insert
// Fix: maintain sorted invariant during insert

// Example 3: Impossible condition
function calculateDiscount(float $rate): float
{
    if ($rate < 0 || $rate > 1) {
        throw new LogicException("Discount rate must be between 0 and 1, got $rate");
    }
    // If this point is reached with invalid $rate, logic is broken
}
?>
```

## Related Errors

- [PHP RuntimeException]({{< relref "/languages/php/runtimeexception" >}})
- [PHP BadMethodCallException]({{< relref "/languages/php/badmethodcallexception" >}})
- [PHP DomainException]({{< relref "/languages/php/domainexception" >}})
