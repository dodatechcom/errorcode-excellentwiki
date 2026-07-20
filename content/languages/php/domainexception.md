---
title: "[Solution] PHP DomainException — Function Argument Doesn't Match Domain Rules"
description: "Fix PHP DomainException by validating input against domain rules, checking constraints, and using proper validation."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# DomainException — Function Argument Doesn't Match Domain Rules

This exception is thrown when a value does not adhere to the defined domain rules or business constraints. It indicates that an argument is valid in type but violates domain-specific invariants, such as an invalid email format, a negative price, or a username that doesn't meet policy requirements.

## Common Causes

- Input passes type checks but violates business rules (e.g., negative quantity)
- Value is semantically invalid within the application's domain
- Validation rules are not enforced at boundaries
- Configuration values outside acceptable parameters

## How to Fix

### Fix 1: Validate Input Against Domain Rules

Create validation methods that enforce domain-specific constraints.

```php
<?php
class Price
{
    public function __construct(float $amount)
    {
        if ($amount < 0) {
            throw new DomainException("Price cannot be negative: $amount");
        }
        $this->amount = $amount;
    }
}
?>
```

### Fix 2: Use Value Objects with Built-in Validation

Encapsulate domain validation inside value objects to ensure invariants.

```php
<?php
class Email
{
    private string $address;

    public function __construct(string $address)
    {
        if (!filter_var($address, FILTER_VALIDATE_EMAIL)) {
            throw new DomainException("Invalid email address: $address");
        }
        $this->address = $address;
    }
}
?>
```

### Fix 3: Validate at System Boundaries

Always validate external input at the entry points of your application.

```php
<?php
function processOrder(array $data): Order
{
    if ($data['quantity'] <= 0) {
        throw new DomainException("Order quantity must be positive");
    }

    if ($data['total'] > 1000000) {
        throw new DomainException("Order total exceeds maximum allowed");
    }

    return new Order($data);
}
?>
```

### Fix 4: Use Constraint Assertions for Complex Rules

Chain multiple domain validations for complex business logic.

```php
<?php
class UserProfile
{
    public function __construct(string $username, int $age)
    {
        if (strlen($username) < 3 || strlen($username) > 50) {
            throw new DomainException("Username must be between 3 and 50 characters");
        }

        if (!preg_match('/^[a-zA-Z0-9_]+$/', $username)) {
            throw new DomainException("Username can only contain alphanumeric characters and underscores");
        }

        if ($age < 13 || $age > 150) {
            throw new DomainException("Age must be between 13 and 150");
        }
    }
}
?>
```

## Examples

```php
<?php
// Example 1: Negative price in e-commerce
$price = new Price(-10.00);
// DomainException: Price cannot be negative: -10
// Fix: validate $amount >= 0

// Example 2: Invalid date range
$dateRange = new DateRange('2026-12-31', '2026-01-01');
// DomainException: End date must be after start date
// Fix: check $end >= $start

// Example 3: Invalid status transition
$order->transitionTo('shipped');
// DomainException: Cannot transition from 'pending' to 'shipped'
// Fix: define valid state machine transitions
?>
```

## Related Errors

- [PHP InvalidArgumentException]({{< relref "/languages/php/invalidargumentexception" >}})
- [PHP RangeException]({{< relref "/languages/php/rangeexception" >}})
- [PHP OutOfRangeException]({{< relref "/languages/php/outofrangeexception" >}})
