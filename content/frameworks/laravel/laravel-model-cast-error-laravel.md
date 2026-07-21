---
title: "[Solution] Laravel Model Cast Error Laravel"
description: "Model casts not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Model casts not working.

## Common Causes

Wrong cast type.

## How to Fix

Define cast.

## Example

```php
protected $casts = ['price' => 'decimal:2', 'options' => 'array'];
```
