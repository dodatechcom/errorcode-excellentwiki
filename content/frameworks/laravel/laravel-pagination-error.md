---
title: "[Solution] Laravel Pagination Error"
description: "Pagination not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Pagination not working.

## Common Causes

Wrong call.

## How to Fix

Use paginate.

## Example

```php
$users = User::paginate(15);
// view: $users->links()
```
