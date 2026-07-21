---
title: "[Solution] Spring @Value Not Resolved"
description: "Placeholder not resolving."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Placeholder not resolving.

## Common Causes

Property missing.

## How to Fix

Add to properties.

## Example

```java
@Value("${my.prop}")
private String prop;
```
