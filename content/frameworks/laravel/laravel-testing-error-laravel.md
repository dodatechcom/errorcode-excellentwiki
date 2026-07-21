---
title: "[Solution] laravel Testing Error Laravel"
description: "Test failing."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Test failing.

## Common Causes

Wrong setup.

## How to Fix

Use RefreshDatabase.

## Example

```php
use Illuminate\Foundation\Testing\RefreshDatabase;
class UserTest extends TestCase {
    use RefreshDatabase;
}
```
