---
title: "[Solution] laravel Accessors Error Laravel"
description: "Accessor not returning."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Accessor not returning.

## Common Causes

Wrong name.

## How to Fix

Define getAttribute.

## Example

```php
public function getNameAttribute() { return ucfirst($this->attributes['name']); }
```
