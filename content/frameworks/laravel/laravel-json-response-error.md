---
title: "[Solution] laravel JSON Response Error"
description: "JSON response failing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

JSON response failing.

## Common Causes

Data not serializable.

## How to Fix

Use toJson().

## Example

```php
return response()->json(['data' => $users->toArray()]);
```
