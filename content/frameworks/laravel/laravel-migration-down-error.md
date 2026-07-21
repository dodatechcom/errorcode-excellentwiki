---
title: "[Solution] laravel Migration Down Error"
description: "Migration rollback failing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Migration rollback failing.

## Common Causes

Wrong down method.

## How to Fix

Define reversible.

## Example

```php
Schema::table('users', function (Blueprint $t) {
    $t->string('phone')->nullable();
});
```
