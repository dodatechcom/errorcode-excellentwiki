---
title: "[Solution] PHP Warning: count() — Parameter Must Be Array or Countable"
description: "Fix PHP Warning: count() parameter must be an array or Countable. Check variable type, use is_countable() (PHP 7.3+), handle null."
languages: ["php"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 7
---

# PHP Warning: count() — Parameter Must Be Array or Countable

This warning occurs when `count()` receives a parameter that is not an array and does not implement the `Countable` interface. In PHP 7.2+, passing `null` or non-countable types to `count()` triggers this warning instead of silently returning 0 or 1.

## Common Causes

```php
<?php
// Example 1: Passing null to count()
$data = null;
echo count($data);
// Warning: count(): Parameter must be an array or an object that implements Countable
```

```php
<?php
// Example 2: Function returns non-array
$result = databaseQuery(); // Returns string on error
echo count($result);
// Warning: count(): Parameter must be an array or Countable
```

```php
<?php
// Example 3: Variable accidentally reassigned
$items = [1, 2, 3];
$items = reset($items); // Now it's an integer
echo count($items);
// Warning: count(): Parameter must be an array or Countable
```

```php
<?php
// Example 4: stdClass object passed to count()
$obj = new stdClass();
echo count($obj);
// Warning: count(): Parameter must be an array or Countable
```

```php
<?php
// Example 5: Boolean value
$flag = false;
echo count($flag);
// Warning: count(): Parameter must be an array or Countable
```

## How to Fix

### Fix 1: Check Variable Type Before Counting

Always verify the variable is an array or Countable before calling `count()`.

```php
<?php
$data = getDataFromApi();

if (is_array($data) || $data instanceof Countable) {
    echo count($data);
} else {
    echo 0;
}
```

### Fix 2: Use the Null Coalescing Operator

Provide a default empty array for potentially null values.

```php
<?php
$data = getItems(); // May return null
echo count($data ?? []);
```

### Fix 3: Use is_countable() (PHP 7.3+)

The `is_countable()` function checks whether a value can be counted.

```php
<?php
$data = getValue();

if (is_countable($data)) {
    echo count($data);
} else {
    echo 0;
}
```

### Fix 4: Create a Safe Count Wrapper

Centralize count logic with fallback handling.

```php
<?php
function safeCount(mixed $value): int {
    if (is_array($value) || $value instanceof Countable) {
        return count($value);
    }
    return 0;
}

echo safeCount(null);     // 0
echo safeCount([1, 2]);   // 2
echo safeCount("hello");  // 0
```

### Fix 5: Use Countable Interface for Custom Objects

Implement `Countable` on your own classes to make them work with `count()`.

```php
<?php
class ItemCollection implements Countable {
    private array $items = [];

    public function add(mixed $item): void {
        $this->items[] = $item;
    }

    public function count(): int {
        return count($this->items);
    }
}

$collection = new ItemCollection();
$collection->add("item1");
$collection->add("item2");
echo count($collection); // 2
```

## Examples

```php
<?php
// Scenario: Counting database results
function getUserCount(mixed $users): int {
    return safeCount($users);
}

// Works with array
echo getUserCount(["alice", "bob"]); // 2

// Works with null
echo getUserCount(null); // 0

// Works with Countable object
$collection = new ItemCollection();
echo getUserCount($collection); // 0
```

## Related Errors

- [PHP Warning: strlen() Expects String](/languages/php/warning-strlen-expects)
- [PHP Warning: foreach() Cannot Iterate](/languages/php/warning-foreach-cannot-iterate)
- [PHP Warning: in_array() Expects Array](/languages/php/warning-in-array-expects)
