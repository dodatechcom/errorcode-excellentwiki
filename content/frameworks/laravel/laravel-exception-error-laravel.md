---
title: "[Solution] laravel Exception Error Laravel"
description: "Exception not caught."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Exception not caught.

## Common Causes

Not handled.

## How to Fix

Handle in handler.

## Example

```php
public function register() {
    $this->renderable(function (NotFoundHttpException $e) {
        return response()->json(['error' => 'Not found'], 404);
    });
}
```
