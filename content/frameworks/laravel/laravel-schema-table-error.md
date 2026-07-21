---
title: "[Solution] Laravel Schema Table Error"
description: "Schema operation failing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Schema operation failing.

## Common Causes

Wrong table.

## How to Fix

Check name.

## Example

```php
Schema::table('users', function (Blueprint $t) { $t->string('email'); });
```
