---
title: "[Solution] Spring Password Encoder Error"
description: "Encoding failing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Encoding failing.

## Common Causes

Wrong encoder.

## How to Fix

Use BCrypt.

## Example

```java
@Bean
public PasswordEncoder pe() { return new BCryptPasswordEncoder(); }
```
