---
title: "[Solution] laravel Validation Error Laravel"
description: "Validation failing silently."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Validation failing silently.

## Common Causes

Not checking fails().

## How to Fix

Check $request->validate().

## Example

```php
$validated = $request->validate(['email' => 'required|email']);
```
