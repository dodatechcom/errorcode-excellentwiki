---
title: "[Solution] Laravel File Storage Error"
description: "File not storing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

File not storing.

## Common Causes

Disk not configured.

## How to Fix

Configure disk.

## Example

```php
Storage::disk('s3')->put('file.pdf', $contents);
```
