---
title: "[Solution] laravel Pagination Error Laravel"
description: "Pagination links not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Pagination links not working.

## Common Causes

Missing links().

## How to Fix

Add links().

## Example

```php
$users = User::paginate(15);
// In blade: $users->links()
```
