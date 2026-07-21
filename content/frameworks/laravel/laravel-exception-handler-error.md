---
title: "[Solution] Laravel Exception Handler Error"
description: "Custom exception not caught."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom exception not caught.

## Common Causes

Not registered.

## How to Fix

Register in handler.

## Example

```php
public function register() {
    $this->renderable(function (NotFoundHttpException $e) { ... });
}
```
