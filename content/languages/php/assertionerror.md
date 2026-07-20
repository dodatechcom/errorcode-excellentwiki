---
title: "[Solution] PHP AssertionError — Assertion Failed"
description: "Fix PHP AssertionError by checking assertion conditions, enabling assertions in php.ini, and using proper validation."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 54
---

# AssertionError — Assertion Failed

AssertionError is thrown when `assert()` evaluates to `false`. Assertions are used during development to verify assumptions about code behavior. In PHP 8.0+, this became a proper Error subclass rather than a warning.

## Common Causes

```php
<?php
// Cause 1: Assertion condition evaluates to false
$value = -1;
assert($value >= 0); // AssertionError: -1 >= 0 is false

// Cause 2: Assertion with expression that fails
function divide(float $a, float $b): float {
    assert($b !== 0); // AssertionError if $b is 0
    return $a / $b;
}
divide(10, 0);

// Cause 3: Assertions disabled in production but used for validation
assert(in_array($status, ['active', 'inactive'])); // AssertionError if $status is unexpected

// Cause 4: Using assertion for type checking that fails
$data = getArray();
assert(is_array($data) && count($data) > 0); // AssertionError on empty array
?>
```

## How to Fix

### Fix 1: Enable assertions in php.ini

```ini
; php.ini - ensure assertions are enabled
assert.active = 1
assert.warning = 1
assert.bail = 0
assert.quiet_eval = 0
```

```php
<?php
// Check assertion status at runtime
if (ini_get('assert.active') !== '1') {
    error_log('Warning: Assertions are disabled');
}
?>
```

### Fix 2: Use proper validation instead of assertions

```php
<?php
// WRONG — using assert for input validation
function processAge(int $age): string {
    assert($age >= 0 && $age <= 150);
    return "Age is $age";
}

// CORRECT — use proper validation
function processAge(int $age): string {
    if ($age < 0 || $age > 150) {
        throw new ValueError("Age must be between 0 and 150, got $age");
    }
    return "Age is $age";
}
?>
```

### Fix 3: Handle assertion errors gracefully

```php
<?php
set_exception_handler(function (Throwable $e) {
    if ($e instanceof AssertionError) {
        error_log("Assertion failed: " . $e->getMessage());
        http_response_code(500);
        echo json_encode(['error' => 'Internal server error']);
        return;
    }
    throw $e;
});

// Assertions for development debugging
$debug = true;
assert($debug === true || isProduction());
?>
```

## Examples

```php
<?php
// Using assertions for development-only checks
function transferFunds(float $from, float $to, float $amount): bool {
    // Development-only assertions (stripped in production with opcache)
    assert($amount > 0, 'Transfer amount must be positive');
    assert($from >= $amount, 'Insufficient funds');

    // Real validation
    if ($amount <= 0) {
        throw new ValueError('Amount must be positive');
    }
    return true;
}
?>
```

## Related Errors

- [PHP ValueError]({{< relref "/languages/php/valueerror" >}}) — invalid value
- [PHP TypeError]({{< relref "/languages/php/typeerror" >}}) — type mismatch
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
