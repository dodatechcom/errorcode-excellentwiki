---
title: "[Solution] laravel Eager Loading Error"
description: "N+1 query problem."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

N+1 query problem.

## Common Causes

Missing with().

## How to Fix

Add with().

## Example

```php
$posts = Post::with('author', 'comments')->get();
```
