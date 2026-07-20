---
title: "[Solution] PHP FiberError — Fiber Operation Failed"
description: "Fix PHP FiberError by checking fiber state, not resuming completed fibers, and handling fiber lifecycle properly."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 62
---

# FiberError — Fiber Operation Failed

FiberError is thrown when a fiber operation fails, such as resuming a fiber that is not in the suspended state, or starting a fiber that is already running. Fibers were introduced in PHP 8.1 for cooperative multitasking.

## Common Causes

```php
<?php
// Cause 1: Resuming an already completed fiber
$fiber = new Fiber(function () {
    return 42;
});
$fiber->start();
$fiber->resume(); // FiberError: fiber is not suspended

// Cause 2: Starting a fiber that is already running
$fiber = new Fiber(function (Fiber $fiber) {
    $fiber->start(); // FiberError: cannot start from within a fiber
});

// Cause 3: Resuming a fiber that hasn't started
$fiber = new Fiber(function () {
    Fiber::suspend();
});
$fiber->resume(); // FiberError: fiber has not been started

// Cause 4: Suspending from the main fiber
Fiber::suspend(); // FiberError: cannot suspend the main fiber

// Cause 5: Getting/setting value on wrong fiber state
$fiber = new Fiber(function () {
    Fiber::suspend('value');
});
$fiber->start();
$fiber->getReturn(); // FiberError: fiber has not returned yet
?>
```

## How to Fix

### Fix 1: Check fiber state before operations

```php
<?php
$fiber = new Fiber(function () {
    Fiber::suspend();
    return 42;
});

// Check state before resuming
if ($fiber->isStarted() && !$fiber->isTerminated() && !$fiber->isRunning()) {
    $fiber->resume();
}

// After completion
if ($fiber->isTerminated()) {
    $value = $fiber->getReturn();
    echo $value; // 42
}
?>
```

### Fix 2: Use proper fiber lifecycle management

```php
<?php
function runFiber(callable $callback): mixed {
    $fiber = new Fiber($callback);

    try {
        $fiber->start();

        while ($fiber->isSuspended()) {
            $value = $fiber->getReturn();
            $fiber->resume($value);
        }

        if ($fiber->isTerminated()) {
            return $fiber->getReturn();
        }
    } catch (FiberError $e) {
        error_log("Fiber error: " . $e->getMessage());
        return null;
    }

    return null;
}

// Usage
$result = runFiber(function () {
    $value = Fiber::suspend('first');
    return $value + 10;
});
echo $result;
?>
```

### Fix 3: Don't resume from within a fiber

```php
<?php
$fiber = new Fiber(function () {
    // Don't call $otherFiber->resume() from here
    // Instead, suspend and let the scheduler handle it
    $value = Fiber::suspend('waiting');
    return "Got: $value";
});

$fiber->start();

// Resume from the main context
$fiber->resume('hello');
echo $fiber->getReturn(); // "Got: hello"
?>
```

## Examples

```php
<?php
// Safe fiber usage pattern
function createSafeFiber(): Fiber {
    return new Fiber(function (Fiber $fiber) {
        $input = $fiber->getReturn();
        $result = strtoupper($input);
        Fiber::suspend($result);
        return "Done: $result";
    });
}

$fiber = createSafeFiber();
$fiber->start();
$suspended = $fiber->suspend('hello');
echo $suspended; // "HELLO"

// Properly check state before each operation
if ($fiber->isSuspended()) {
    $fiber->resume();
}

if ($fiber->isTerminated()) {
    echo $fiber->getReturn(); // "Done: HELLO"
}
?>
```

## Related Errors

- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}}) — fatal error
- [PHP TypeError]({{< relref "/languages/php/typeerror" >}}) — type mismatch
- [PHP ClosedGeneratorException]({{< relref "/languages/php/closedgeneratorexception" >}}) — generator already returned
