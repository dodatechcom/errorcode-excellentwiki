---
title: "[Solution] laravel Carbon Error Laravel"
description: "Carbon date not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Carbon date not working.

## Common Causes

Wrong import.

## How to Fix

Import Carbon.

## Example

```php
use Carbon\Carbon;
$now = Carbon::now();
$yesterday = Carbon::yesterday();
```
