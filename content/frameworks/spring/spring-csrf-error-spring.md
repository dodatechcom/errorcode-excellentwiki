---
title: "[Solution] Spring CSRF Error Spring"
description: "CSRF token missing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

CSRF token missing.

## Common Causes

Not disabled for API.

## How to Fix

Disable for REST.

## Example

```java
http.csrf(c -> c.disable());
```
