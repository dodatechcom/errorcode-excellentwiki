---
title: "[Solution] Spring Circular Dependency Error"
description: "Circular dependency."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Circular dependency.

## Common Causes

A depends on B, B on A.

## How to Fix

Use @Lazy.

## Example

```java
@Autowired @Lazy
private CircularDep bean;
```
