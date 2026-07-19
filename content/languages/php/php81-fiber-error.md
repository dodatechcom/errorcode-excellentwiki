---
title: "[Solution] PHP Fiber Creation and Suspension Error Fix"
description: "Fix 'Fiber error: cannot suspend' errors in PHP 8.1+. Learn proper Fiber lifecycle, start, and resume patterns."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "php"
tags: ["php", "php81", "fibers", "concurrency", "runtime-error"]
severity: "error"
---

# Fiber Error: Cannot Suspend

## Error Message

```
Uncaught FiberError: Cannot suspend from fiber shutdown function in /path/to/file.php:15
```

## Common Causes

- Attempting to suspend a fiber from inside a fiber shutdown function or destructor
- Calling Fiber::suspend() from the fiber's main function instead of from a callback
- Nesting fiber suspensions incorrectly — trying to suspend a fiber that is already suspended
- Using Fiber::suspend() inside a finally block during fiber destruction

## Solutions

### Solution 1: Suspend fibers from within a callback, not the main function

The fiber's main function must return a value; use a callback passed to the fiber for suspension.

```php
<?php
// WRONG: Calling suspend from the main callable
$fiber = new Fiber(function (Fiber $fiber): void {
    Fiber::suspend('starting'); // FiberError
    echo 'resumed';
});

// CORRECT: Suspend via Fiber::suspend in a callback
$fiber = new Fiber(function (Fiber $fiber): string {
    $fiber->suspend('paused');
    return 'done';
});

$value = $fiber->start();    // 'paused'
$value = $fiber->resume();   // 'done'
echo $fiber->getReturn();     // 'done'
?>
```

### Solution 2: Manage fiber lifecycle with proper error handling

Wrap fiber operations in try/catch to handle FiberError and FiberExit gracefully.

```php
<?php
function safeFiberRun(callable $fn): mixed {
    $fiber = new Fiber($fn);

    try {
        $fiber->start();
        while ($fiber->isSuspended()) {
            $fiber->resume();
        }
        return $fiber->getReturn();
    } catch (FiberError $e) {
        error_log("Fiber error: " . $e->getMessage());
        return null;
    } catch (\Throwable $e) {
        error_log("Unexpected fiber error: " . $e->getMessage());
        return null;
    }
}

$result = safeFiberRun(function (Fiber $fiber): string {
    return 'completed safely';
});

echo $result; // 'completed safely'
?>
```

### Solution 3: Use fibers for cooperative multitasking with a scheduler

Fibers are designed for cooperative scheduling — use a scheduler pattern to manage multiple fibers.

```php
<?php
$ fibers = [];
$results = [];

// Create multiple fibers
for ($i = 0; $i < 3; $i++) {
    $fibers[] = new Fiber(function (Fiber $fiber) use ($i): void {
        for ($j = 0; $j < 3; $j++) {
            $fiber->suspend("fiber-$i-iter-$j");
        }
    });
}

// Start all fibers
foreach ($fibers as $fiber) {
    $fiber->start();
}

// Round-robin resume
while (count($fibers) > 0) {
    foreach ($fibers as $key => $fiber) {
        if ($fiber->isTerminated()) {
            unset($fibers[$key]);
            continue;
        }
        $value = $fiber->resume();
        if ($value !== null) {
            $results[] = $value;
        }
    }
}

print_r($results);
?>
```

## Prevention Tips

- Never call Fiber::suspend() from a fiber's shutdown function or destructor
- Always check isStarted(), isSuspended(), and isTerminated() before calling resume()
- Use Fiber::getReturn() to retrieve the return value after the fiber terminates
- Fibers are cooperative — each fiber must explicitly yield via suspend() for others to run

## Related Errors

- [PHP Enum Error]({{< relref "/languages/php/php81-enum-error" >}})
- [PHP Readonly Property Error]({{< relref "/languages/php/php81-readonly-property" >}})
- [PHP Fatal Error]({{< relref "/languages/php/fatal-error" >}})
