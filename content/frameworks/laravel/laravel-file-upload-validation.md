---
title: "[Solution] Laravel File Upload Validation"
description: "Upload validation failing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Upload validation failing.

## Common Causes

Wrong rules.

## How to Fix

Use correct rules.

## Example

```php
$validated = $request->validate(['file' => 'required|file|max:2048|mimes:pdf,jpg']);
```
