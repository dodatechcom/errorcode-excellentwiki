---
title: "[Solution] laravel API Resource Error"
description: "API resource not transforming."
frameworks: ["laravel"]
error-types: ["framework-error"]
severities: ["error"]
---

API resource not transforming.

## Common Causes

Wrong resource.

## How to Fix

Define resource class.

## Example

```php
class UserResource extends JsonResource {
    public function toArray($request) {
        return ['id' => $this->id, 'name' => $this->name];
    }
}
```
