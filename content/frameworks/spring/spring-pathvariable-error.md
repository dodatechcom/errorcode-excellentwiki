---
title: "[Solution] Spring PathVariable Error"
description: "Path variable not binding."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Path variable not binding.

## Common Causes

Wrong name.

## How to Fix

Match name.

## Example

```java
@GetMapping("/u/{id}")
public User get(@PathVariable Long id) {}
```
