---
title: "[Solution] Spring Access Denied Error"
description: "User lacks role."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

User lacks role.

## Common Causes

Wrong role.

## How to Fix

Assign role.

## Example

```java
http.authorizeHttpRequests(a -> a.requestMatchers("/admin/**").hasRole("ADMIN"));
```
