---
title: "[Solution] Spring RequestBody Error"
description: "Body not deserializing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Body not deserializing.

## Common Causes

Wrong JSON.

## How to Fix

Match class.

## Example

```java
@PostMapping("/u")
public User create(@RequestBody User u) {}
```
