---
title: "[Solution] laravel Model Not Found Error"
description: "Model not found in database."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Model not found in database.

## Common Causes

Wrong ID.

## How to Fix

Use find or findOrFail.

## Example

```php
$user = User::findOrFail($id);
```
