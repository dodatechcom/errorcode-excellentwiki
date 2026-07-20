---
title: "[Solution] PHP 8.0 First Class Callable Syntax Error — Invalid Callable Syntax"
description: "Fix PHP 8.0 First Class Callable Syntax Error by using Closure::fromCallable(), correct syntax, and verifying function exists. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 320
---

# PHP 8.0 First Class Callable Syntax Error — Invalid Callable Syntax

A First Class Callable Syntax Error occurs when using the PHP 8.0 callable syntax incorrectly, passing invalid callable values, or using the syntax on PHP versions that don't support it. PHP 8.0 introduced first-class callable syntax using `strlen(...)`, `MyClass::method(...)`, etc., to create `Closure` objects from functions and methods.

## Common Causes

```php
<?php
// Cause 1: Wrong syntax — missing parentheses
$fn = strlen; // This is a string 'strlen', not a Closure
$fn = strlen(...); // Correct — creates Closure

// Cause 2: Using first-class callable with nonexistent function
$fn = nonExistentFunction(...); // Error — function doesn't exist

// Cause 3: Static method callable with wrong syntax
class MyClass {
    public static function compute(int $x): int { return $x * 2; }
}

$fn = MyClass::compute; // String, not Closure
$fn = MyClass::compute(...); // Correct

// Cause 4: Instance method — can't use first-class callable on instance
$obj = new MyClass();
$fn = $obj->compute(...); // Error — not supported on instances

// Cause 5: Using on built-in functions without parentheses
$fn = array_map; // Just a string
$fn = array_map(...); // Correct
?>
```

## How to Fix

### Fix 1: Use parentheses `(...)` to create Closure

```php
<?php
// Wrong — this is just a string
// $fn = strlen;

// Correct — first-class callable syntax (PHP 8.0+)
$fn = strlen(...);

echo $fn('hello'); // 5
?>
```

### Fix 2: Use for static methods correctly

```php
<?php
class MathUtils {
    public static function square(int $x): int {
        return $x * $x;
    }

    public static function add(int $a, int $b): int {
        return $a + $b;
    }
}

// Correct — static method callable
$square = MathUtils::square(...);
echo $square(5); // 25

$add = MathUtils::add(...);
echo $add(3, 4); // 7
?>
```

### Fix 3: Use Closure::fromCallable() for backward compatibility

```php
<?php
// PHP 7.1+ approach
$fn = Closure::fromCallable('strlen');
echo $fn('hello'); // 5

// PHP 8.0+ approach (equivalent)
$fn = strlen(...);
echo $fn('hello'); // 5

// For methods (works in PHP 7.1+)
$obj = new MyClass();
$fn = Closure::fromCallable([$obj, 'method']);

// PHP 8.0+ for static methods
$fn = MyClass::compute(...);
?>
```

### Fix 4: Use with array functions properly

```php
<?php
// Using first-class callable with array functions
$numbers = [1, 2, 3, 4, 5];

// Wrong — passing function name as string
// $squared = array_map('MathUtils::square', $numbers);

// Correct — first-class callable syntax
$squared = array_map(MathUtils::square(...), $numbers);
// [1, 4, 9, 16, 25]

// Using with array_filter
$isEven = function (int $n): bool {
    return $n % 2 === 0;
};

$evens = array_filter($numbers, $isEven);
// [2, 4]
?>
```

### Fix 5: Verify callable exists before using

```php
<?php
function safeCallable(string $functionName): Closure {
    if (!function_exists($functionName)) {
        throw new InvalidArgumentException("Function not found: $functionName");
    }

    return Closure::fromCallable($functionName);
}

try {
    $strlen = safeCallable('strlen');
    echo $strlen('hello'); // 5
} catch (InvalidArgumentException $e) {
    echo $e->getMessage();
}
?>
```

## Examples

```php
<?php
// Practical first-class callable usage
class EventDispatcher {
    private array $listeners = [];

    public function on(string $event, callable $listener): void {
        $this->listeners[$event][] = $listener;
    }

    public function dispatch(string $event, mixed $data): void {
        foreach ($this->listeners[$event] ?? [] as $listener) {
            $listener($data);
        }
    }
}

// Using first-class callable for event handlers
class UserEvents {
    public static function onCreated(array $user): void {
        echo "User created: {$user['name']}\n";
    }

    public static function onDeleted(array $user): void {
        echo "User deleted: {$user['name']}\n";
    }
}

$dispatcher = new EventDispatcher();
$dispatcher->on('user.created', UserEvents::onCreated(...));
$dispatcher->on('user.deleted', UserEvents::onDeleted(...));

$dispatcher->dispatch('user.created', ['name' => 'Alice']);

// Using with pipeline/pipe patterns
function pipe(mixed $value, callable ...$transforms): mixed {
    foreach ($transforms as $transform) {
        $value = $transform($value);
    }
    return $value;
}

$result = pipe(
    'Hello World',
    strtolower(...),
    str_replace(' ', '-', ...),
    strtoupper(...)
);
// HELLO-WORLD
?>
```

## Related Errors

- [PHP 8.0 Named Argument Error](/languages/php/php80-named-argument/) — Callable argument syntax
- [PHP 8.0 Match Expression Error](/languages/php/php80-match-expression/) — PHP 8.0 syntax features
- [PHP 8.0 Union Type Error](/languages/php/php80-union-type-error/) — Type system in PHP 8.0
