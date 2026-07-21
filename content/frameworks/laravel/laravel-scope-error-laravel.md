---
title: "[Solution] laravel Scope Error Laravel"
description: "Query scope not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Query scope not working.

## Common Causes

Wrong definition.

## How to Fix

Define scope.

## Example

```php
class User extends Model {
    public function scopeActive($q) { return $q->where('active', true); }
}
User::active()->get();
```
