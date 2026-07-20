---
title: "[Solution] PHP 8.1 Fiber Error — Invalid Fiber Operation"
description: "Fix PHP 8.1 Fiber Error by checking fiber state, not resuming completed fibers, and handling fiber lifecycle. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 308
---

# PHP 8.1 Fiber Error — Invalid Fiber Operation

A Fiber Error occurs when an invalid operation is performed on a Fiber, such as starting an already-started fiber, resuming a completed fiber, or calling `getReturn()` before the fiber finishes. PHP 8.1 introduced Fibers — lightweight, interruptible functions for cooperative multitasking within a single thread.

## Common Causes

```php
<?php
// Cause 1: Starting an already-started fiber
$fiber = new Fiber(function () {
    Fiber::suspend('paused');
    return 'done';
});

$fiber->start();
$fiber->start(); // Error — cannot start an already-started fiber

// Cause 2: Resuming a completed fiber
$fiber = new Fiber(function () {
    return 'done';
});

$fiber->start();
$fiber->getReturn(); // 'done'
$fiber->resume();    // Error — cannot resume a completed fiber

// Cause 3: Getting return value before fiber completes
$fiber = new Fiber(function () {
    Fiber::suspend('middle');
    return 'done';
});

$fiber->start();
$fiber->getReturn(); // Error — fiber hasn't returned yet

// Cause 4: Suspending outside of a fiber
Fiber::suspend(); // Error — must be called within a fiber

// Cause 5: Fiber throwing unhandled exception
$fiber = new Fiber(function () {
    throw new RuntimeException('fail');
});
$fiber->start(); // Exception propagates if not handled
?>
```

## How to Fix

### Fix 1: Check fiber state before operations

```php
<?php
$fiber = new Fiber(function () {
    Fiber::suspend('yielded');
    return 'done';
});

echo $fiber->isStarted();  // false
echo $fiber->isSuspended(); // false
echo $fiber->isTerminated(); // false

$fiber->start();
echo $fiber->isStarted();   // true
echo $fiber->isSuspended(); // true

$value = $fiber->getResumeValue(); // 'yielded'
$fiber->resume();
echo $fiber->isTerminated(); // true
?>
```

### Fix 2: Use proper fiber lifecycle management

```php
<?php
function runFiber(callable $callback): mixed {
    $fiber = new Fiber($callback);
    $fiber->start();

    while ($fiber->isSuspended()) {
        $value = $fiber->getResumeValue();
        $fiber->resume($value);
    }

    if ($fiber->isTerminated()) {
        try {
            return $fiber->getReturn();
        } catch (FiberError $e) {
            return null;
        }
    }

    return null;
}
?>
```

### Fix 3: Handle fiber exceptions properly

```php
<?php
$fiber = new Fiber(function () {
    try {
        Fiber::suspend('working');
        throw new RuntimeException('Something went wrong');
    } catch (RuntimeException $e) {
        return 'caught: ' . $e->getMessage();
    }
});

$fiber->start();
$value = $fiber->getResumeValue(); // 'working'
$fiber->resume();
echo $fiber->getReturn(); // 'caught: Something went wrong'
?>
```

### Fix 4: Use fibers with channels for communication

```php
<?php
class Channel {
    private array $buffer = [];
    private ?Fiber $receiver = null;

    public function send(mixed $value): void {
        $this->buffer[] = $value;
        if ($this->receiver !== null && $this->receiver->isSuspended()) {
            $this->receiver->resume();
        }
    }

    public function receive(Fiber $fiber): mixed {
        if (empty($this->buffer)) {
            $this->receiver = $fiber;
            Fiber::suspend();
            $this->receiver = null;
        }
        return array_shift($this->buffer);
    }
}
?>
```

## Examples

```php
<?php
// Basic fiber usage
$fiber = new Fiber(function (string $greeting) {
    $name = Fiber::suspend($greeting);   // Suspend with value
    return "$greeting, $name!";          // Return final result
});

$fiber->start('Hello');
$recipient = $fiber->getResumeValue();   // 'Hello'
$recipient = $fiber->resume('World');    // Resume with 'World'
echo $fiber->getReturn();                // 'Hello, World!'

// Fiber for async I/O simulation
function asyncFetch(string $url): Fiber {
    return new Fiber(function () use ($url) {
        // Simulate async operation
        Fiber::suspend(['url' => $url, 'action' => 'request']);
        $response = ['status' => 200, 'body' => 'data'];
        return $response;
    });
}

$fiber = asyncFetch('https://example.com');
$fiber->start();
$instruction = $fiber->getResumeValue();
$fiber->resume();
$response = $fiber->getReturn();
?>
```

## Related Errors

- [PHP 8.0 Match Expression Error](/languages/php/php80-match-expression/) — Related control flow errors
- [PHP 8.1 Enum Error](/languages/php/php81-enums/) — PHP 8.1 feature errors
- [PHP 8.1 Readonly Property Error](/languages/php/php81-readonly-properties/) — PHP 8.1 feature errors
