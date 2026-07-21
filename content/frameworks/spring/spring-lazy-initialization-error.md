---
title: "[Solution] Spring Lazy Initialization Error"
description: "Bean initialized too early."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Bean initialized too early.

## Common Causes

Not using @Lazy.

## How to Fix

Add @Lazy.

## Example

```java
@Autowired @Lazy private HeavyBean heavy;
```
