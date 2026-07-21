---
title: "[Solution] Spring Spring Cloud Config Error"
description: "Config server not connecting."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Config server not connecting.

## Common Causes

Wrong config.

## How to Fix

Configure client.

## Example

```properties
spring.config.import=optional:configserver:http://localhost:8888
spring.application.name=myapp
```
