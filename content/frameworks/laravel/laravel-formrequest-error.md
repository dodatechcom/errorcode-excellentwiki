---
title: "[Solution] Laravel FormRequest Error"
description: "FormRequest not validating."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

FormRequest not validating.

## Common Causes

Rules not defined.

## How to Fix

Define rules.

## Example

```php
public function rules() { return ['name' => 'required|string']; }
```
