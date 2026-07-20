---
title: "[Solution] PHP debug_backtrace() — Function Call Tracing"
description: "Fix PHP debug_backtrace() issues by tracing function calls, using DEBUG_BACKTRACE_IGNORE_ARGS, limiting depth, and logging for debugging. Copy-paste solutions with code examples."
languages: ["php"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 108
---

# PHP debug_backtrace() — Function Call Tracing

The `debug_backtrace()` function generates a backtrace of function calls, returning an array of stack frames. It is invaluable for debugging but can cause performance issues or memory exhaustion if used carelessly. The related `debug_print_backtrace()` outputs the trace directly to the browser.

## Common Causes

```php
// Cause 1: Returning full trace with arguments (memory intensive)
$trace = debug_backtrace();
// Includes arguments for every function call

// Cause 2: Using debug_print_backtrace() in production
debug_print_backtrace();
// Exposes internal code structure to users

// Cause 3: No depth limit
$trace = debug_backtrace();
// Traces all the way back to the start of the script

// Cause 4: Not filtering irrelevant frames
$trace = debug_backtrace();
// Includes autoloader, framework, and library frames
```

## How to Fix

### Fix 1: Use DEBUG_BACKTRACE_IGNORE_ARGS

```php
// Ignore arguments to reduce memory usage
$trace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS);
```

### Fix 2: Limit Depth

```php
// Only get the last 10 frames
$trace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS, 10);
```

### Fix 3: Use debug_print_backtrace() Only for Local Debugging

```php
function debug() {
    debug_print_backtrace();
    exit;
}
// Use only during development, never in production
```

### Fix 4: Log Backtrace for Debugging

```php
function logBacktrace($message = '', $level = 3) {
    $trace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS, $level);
    $formatted = [];

    foreach ($trace as $frame) {
        $formatted[] = sprintf(
            "%s.%s():%d",
            $frame['file'] ?? '[internal]',
            $frame['function'] ?? '[main]',
            $frame['line'] ?? 0
        );
    }

    error_log("$message\n" . implode("\n", $formatted) . "\n");
}
```

## Examples

```php
// Example: Trace a specific function call
function processOrder($orderId) {
    $trace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS, 5);
    $caller = $trace[1] ?? null;
    error_log("processOrder called from: " . ($caller['function'] ?? 'unknown'));
}

// Example: Format backtrace as readable string
function formatBacktrace() {
    $trace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS);
    $output = "Backtrace:\n";

    foreach ($trace as $i => $frame) {
        $output .= sprintf(
            "  #%d %s:%d %s()\n",
            $i,
            $frame['file'] ?? '[internal]',
            $frame['line'] ?? 0,
            $frame['function']
        );
    }

    return $output;
}

echo formatBacktrace();

// Example: Find the caller of a function
function getCallerInfo($skipFrames = 1) {
    $trace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS, $skipFrames + 2);
    return $trace[$skipFrames] ?? null;
}

$caller = getCallerInfo();
if ($caller) {
    error_log("Called from " . $caller['file'] . ":" . $caller['line']);
}
```

## Related Errors

- [error_log()](/languages/php/error-log-function)
- [set_error_handler()](/languages/php/set-error-handler)
