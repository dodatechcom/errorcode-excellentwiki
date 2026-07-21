---
title: "[Solution] Laravel Authorization Error"
description: "Policy not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Policy not working.

## Common Causes

Not registered.

## How to Fix

Register policy.

## Example

```php
protected $policies = [\n    Post::class => PostPolicy::class,\n];
```
