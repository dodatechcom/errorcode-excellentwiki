---
title: "[Solution] laravel Polymorphic Error Laravel"
description: "Polymorphic relation not working."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

Polymorphic relation not working.

## Common Causes

Wrong morph type.

## How to Fix

Define morphTo.

## Example

```php
class Comment extends Model {
    public function commentable() { return $this->morphTo(); }
}
```
