---
title: "[Solution] laravel Mass Assignment Error"
description: "Mass assignment guarded."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Mass assignment guarded.

## Common Causes

Not in fillable.

## How to Fix

Add to fillable.

## Example

```php
protected $fillable = ['name', 'email', 'password'];
```
