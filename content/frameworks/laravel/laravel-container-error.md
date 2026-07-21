---
title: "[Solution] Laravel Container Error"
description: "Container cannot resolve."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Container cannot resolve.

## Common Causes

Not bound.

## How to Fix

Bind in provider.

## Example

```php
$this->app->bind(I::class, Impl::class);
```
