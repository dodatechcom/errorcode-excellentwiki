---
title: "[Solution] laravel View Not Found Error"
description: "View file not found."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

View file not found.

## Common Causes

Wrong view name.

## How to Fix

Check view path.

## Example

```php
return view('users.index', ['users' => $users]);
```
