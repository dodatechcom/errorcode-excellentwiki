---
title: "[Solution] Spring Validation Error Spring"
description: "Validation not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Validation not working.

## Common Causes

@Valid missing.

## How to Fix

Add @Valid.

## Example

```java
@PostMapping("/u")
public User create(@Valid @RequestBody User u) {}
```
