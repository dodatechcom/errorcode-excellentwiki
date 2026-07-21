---
title: "[Solution] Laravel Foreign Key Error"
description: "FK constraint failing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

FK constraint failing.

## Common Causes

Wrong reference.

## How to Fix

Check definition.

## Example

```php
$table->foreignId('user_id')->constrained()->onDelete('cascade');
```
