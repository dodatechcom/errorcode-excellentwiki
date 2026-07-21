---
title: "[Solution] Laravel Localization Error"
description: "Translation not found."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Translation not found.

## Common Causes

Key missing.

## How to Fix

Add translation.

## Example

```php
__('messages.welcome')
// resources/lang/en/messages.php
return ['welcome' => 'Welcome!'];
```
