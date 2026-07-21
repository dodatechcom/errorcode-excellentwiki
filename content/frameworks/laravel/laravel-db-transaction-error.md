---
title: "[Solution] Laravel DB Transaction Error"
description: "Transaction not rolling back."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Transaction not rolling back.

## Common Causes

Wrong usage.

## How to Fix

Use DB::transaction.

## Example

```php
DB::transaction(function () { User::create($d); Order::create($o); });
```
