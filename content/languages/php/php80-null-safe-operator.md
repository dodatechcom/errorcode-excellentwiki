---
title: "[Solution] PHP 8.0 Null Safe Operator Error — Method Call on Null with ?->"
description: "Fix PHP 8.0 Null Safe Operator Error by checking object state and handling null properly. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 304
---

# PHP 8.0 Null Safe Operator Error — Method Call on Null with ?->

The Null Safe Operator Error occurs when using the `?->` operator in contexts where the result is still null and further chained calls fail, or when the operator is misused. PHP 8.0 introduced the null safe operator `?->` to simplify nullable object method/property access, replacing verbose null checks.

## Common Causes

```php
<?php
// Cause 1: Chaining after null safe returns null
$zipCode = $user?->getAddress()?->getZipCode(); // null if any step is null
echo strlen($zipCode); // TypeError — strlen() expects string, null given

// Cause 2: Using ?-> on non-nullable object (unnecessary but not an error)
$user = new User();
$name = $user?->getName(); // Works but ?-> is unnecessary

// Cause 3: Mixing ?-> with regular -> after null
$order = getOrder();
$city = $order?->getCustomer()?->getAddress()->getCity();
// If getAddress() returns null, ->getCity() will fail

// Cause 4: Using ?-> on a variable that isn't an object at all
$value = null;
$result = $value?->someMethod(); // Works — returns null, but may cause confusion

// Cause 5: Property access after null safe returns null
$phone = $user?->getContact()?->phone;
$dialCode = $phone->dialCode; // TypeError if $phone is null
?>
```

## How to Fix

### Fix 1: Handle null at the end of the chain

```php
<?php
$zipCode = $user?->getAddress()?->getZipCode();
echo $zipCode ?? 'N/A'; // Use null coalescing to provide default
?>
```

### Fix 2: Apply ?-> to every potentially null link in the chain

```php
<?php
$city = $order?->getCustomer()?->getAddress()?->getCity();
echo $city ?? 'Unknown city';
?>
```

### Fix 3: Use null safe operator with type checking

```php
<?php
function getDialCode(?User $user): ?string {
    $phone = $user?->getContact()?->phone;

    if ($phone === null) {
        return null;
    }

    return $phone->dialCode;
}
?>
```

### Fix 4: Combine with null coalescing and null casting

```php
<?php
// Use null coalescing for scalar defaults
$street = $user?->getAddress()?->street ?? 'No address';

// Use match for complex fallbacks
$status = match(true) {
    $user?->isActive() === true  => 'Active',
    $user?->isBanned() === true  => 'Banned',
    default                      => 'Unknown',
};
?>
```

## Examples

```php
<?php
class User {
    private ?Address $address = null;

    public function getAddress(): ?Address {
        return $this->address;
    }
}

class Address {
    public function __construct(
        public ?string $street,
        public ?string $city,
    ) {}
}

// Safe navigation through nullable chain
$user = getUserFromDatabase(); // ?User
$city = $user?->getAddress()?->city ?? 'Unknown';

// Null safe with array access equivalent
$settings = getSettings(); // ?Settings
$theme = $settings?->get('theme') ?? 'default';

// Chained null safe in conditionals
if ($user?->getAddress()?->city === 'New York') {
    echo "Welcome, New Yorker!";
}

// Null safe in expression context
$length = strlen($user?->getAddress()?->street ?? '');
?>
```

## Related Errors

- [PHP 8.0 Union Type Error](/languages/php/php80-union-type-error/) — Handling union types with null
- [PHP 8.0 Typed Property Error](/languages/php/php80-typed-property-error/) — Nullable typed properties
- [PHP 8.1 Readonly Property Error](/languages/php/php81-readonly-properties/) — Readonly properties with nullable types
