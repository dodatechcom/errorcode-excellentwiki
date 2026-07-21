---
title: "[Solution] laravel Redirect Error Laravel"
description: "Redirect not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Redirect not working.

## Common Causes

Wrong URL.

## How to Fix

Use redirect().

## Example

```php
return redirect()->route('dashboard');
return redirect('/home');
```
