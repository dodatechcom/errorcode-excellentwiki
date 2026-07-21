---
title: "[Solution] spring Profile Config Error"
description: "Profile-specific config not loading."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Profile-specific config not loading.

## Common Causes

Wrong file naming.

## How to Fix

Use application-{profile}.properties.

## Example

```properties
# application-dev.properties
server.port=8081
```
