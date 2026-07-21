---
title: "[Solution] Spring Actuator Endpoint Error"
description: "Actuator endpoints not accessible."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Actuator endpoints not accessible.

## Common Causes

Not enabled.

## How to Fix

Enable endpoints.

## Example

```properties
management.endpoints.web.exposure.include=health,info
```
