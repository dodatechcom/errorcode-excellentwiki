---
title: "[Solution] Spring HikariCP Pool Error"
description: "Pool exhausted."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Pool exhausted.

## Common Causes

Pool too small.

## How to Fix

Increase size.

## Example

```properties
spring.datasource.hikari.maximum-pool-size=20
```
