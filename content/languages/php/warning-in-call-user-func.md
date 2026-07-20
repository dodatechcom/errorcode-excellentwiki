---
title: "PHP Warning: call_user_func() expects callable"
description: "Fix PHP Warning: call_user_func() expects callable. Learn to verify functions exist, check method names, and use proper callable syntax."
languages: ["php"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# PHP Warning: call_user_func() expects callable

This warning occurs when `call_user_func()`, `call_user_func_array()`, or similar function-calling utilities receive a value that is not a valid callable.

## Common Causes

- Function name does not exist
- Method name string to a non-existent or private method
- Variable is not a valid callable syntax

## How to Fix

### Verify Function Exists

```php
<?php
// Wrong — function may not exist
$result = call_user_func($callback, $arg);

// Correct — check existence
if (is_callable($callback)) {
    $result = call_user_func($callback, $arg);
}
?>
```

### Check Method Name

```php
<?php
// Wrong — method may not exist
call_user_func([$obj, $method], $arg);

// Correct — check method exists
if (method_exists($obj, $method)) {
    call_user_func([$obj, $method], $arg);
}
?>
```

### Use Proper Callable Syntax

```php
<?php
// Wrong — invalid callable
call_user_func('Namespace\\Class::method', $arg);

// Correct — use array syntax
call_user_func(['Namespace\\Class', 'method'], $arg);
?>
```

## Examples

```php
<?php
// This triggers the warning
call_user_func('nonexistent_function');
// Warning: call_user_func(): Function 'nonexistent_function' is not callable

// Correct
call_user_func('strtoupper', 'hello'); // 'HELLO'
?>
```

## Related Errors

- [PHP Warning: str_replace()]({{< relref "/languages/php/warning-in-str-replace" >}})
- [PHP Fatal Error: Call to undefined function]({{< relref "/languages/php/call-to-undefined" >}})
- [PHP TypeError: call_user_func()]({{< relref "/languages/php/typeerror" >}})
