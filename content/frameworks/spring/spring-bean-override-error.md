---
title: "[Solution] spring Bean Override Error"
description: "Bean overriding not disabled."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Bean overriding not disabled.

## Common Causes

Duplicate bean.

## How to Fix

Disable override.

## Example

```properties
spring.main.allow-bean-definition-overriding=true
```
