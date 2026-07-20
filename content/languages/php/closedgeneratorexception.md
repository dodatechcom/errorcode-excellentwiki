---
title: "[Solution] PHP ClosedGeneratorException — Generator Already Returned"
description: "Fix PHP ClosedGeneratorException by checking generator state, not reusing generators, and collecting values properly."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 52
---

# ClosedGeneratorException — Generator Already Returned

ClosedGeneratorException is thrown when you attempt to iterate a generator that has already returned or been closed. Once a generator finishes execution (reaches a `return` statement or the end of its function body), it cannot be resumed.

## Common Causes

```php
<?php
// Cause 1: Trying to iterate a generator twice
function myGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

$gen = myGenerator();
foreach ($gen as $value) { echo $value; }
foreach ($gen as $value) { echo $value; } // ClosedGeneratorException

// Cause 2: Calling current() after generator is spent
$gen = myGenerator();
foreach ($gen as $value) {}
$current = $gen->current(); // ClosedGeneratorException

// Cause 3: Using generator after return value is consumed
$gen = (function () {
    yield 1;
    return 'done';
})();

$gen->current();
$gen->next();
$gen->current(); // ClosedGeneratorException

// Cause 4: Passing generator to function that iterates it multiple times
function doubleIterate($generator) {
    foreach ($generator as $v) {}
    foreach ($generator as $v) {} // ClosedGeneratorException
}
?>
```

## How to Fix

### Fix 1: Collect generator values into an array

```php
<?php
function myGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

$values = iterator_to_array(myGenerator(), false);

// Now you can iterate as many times as needed
foreach ($values as $value) { echo $value; }
foreach ($values as $value) { echo $value; }
?>
```

### Fix 2: Check generator validity before iterating

```php
<?php
function myGenerator() {
    yield 1;
    yield 2;
}

$gen = myGenerator();
foreach ($gen as $value) { echo $value; }

if ($gen->valid()) {
    foreach ($gen as $value) { echo $value; } // Safe
} else {
    echo "Generator already exhausted";
}
?>
```

### Fix 3: Recreate generator when needed

```php
<?php
function fetchData() {
    yield 1;
    yield 2;
    yield 3;
}

// Create new instance each time
foreach (fetchData() as $value) { echo $value; }
foreach (fetchData() as $value) { echo $value; } // Works fine
?>
```

## Examples

```php
<?php
// Proper generator usage with single pass
function countUp(int $max): Generator {
    for ($i = 1; $i <= $max; $i++) {
        yield $i => $i * $i;
    }
}

// Collect values for reuse
$squares = iterator_to_array(countUp(5));
print_r($squares);

// Use generator as single-pass stream
$stream = countUp(10);
foreach ($stream as $num => $square) {
    echo "$num: $square\n";
}
?>
```

## Related Errors

- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
- [PHP Warning]({{< relref "/languages/php/e-warning" >}}) — warning
- [PHP Notice]({{< relref "/languages/php/e-notice" >}}) — notice
