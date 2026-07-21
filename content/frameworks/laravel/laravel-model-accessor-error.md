---
title: "[Solution] Laravel Model Accessor Error"
description: "Accessor not returning."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Accessor not returning.

## Common Causes

Wrong name.

## How to Fix

Define correctly.

## Example

```php
public function getFullNameAttribute() { return $this->first_name.' '.$this->last_name; }
```
