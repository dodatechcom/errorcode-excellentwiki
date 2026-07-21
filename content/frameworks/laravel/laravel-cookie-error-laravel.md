---
title: "[Solution] laravel Cookie Error Laravel"
description: "Cookie not setting."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Cookie not setting.

## Common Causes

Wrong usage.

## How to Fix

Use cookie() helper.

## Example

```php
cookie('name', 'value', 3600);
return response()->withCookie(cookie('name', 'value', 3600));
```
