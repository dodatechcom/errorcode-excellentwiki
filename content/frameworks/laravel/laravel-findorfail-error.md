---
title: "[Solution] Laravel findOrFail Error"
description: "Model not found exception."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Model not found exception.

## Common Causes

Wrong ID.

## How to Fix

Handle.

## Example

```php
$user = User::find($id);
if (!$user) abort(404);
```
