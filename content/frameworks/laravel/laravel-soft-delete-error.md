---
title: "[Solution] Laravel Soft Delete Error"
description: "Soft deletes not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Soft deletes not working.

## Common Causes

Missing trait.

## How to Fix

Add trait.

## Example

```php
class Post extends Model { use SoftDeletes; }
```
