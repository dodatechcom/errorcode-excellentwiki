---
title: "[Solution] Spring DataSource Not Found Error"
description: "DataSource bean not found."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

DataSource bean not found.

## Common Causes

Config missing.

## How to Fix

Configure datasource.

## Example

```properties
spring.datasource.url=jdbc:postgresql://localhost/mydb
spring.datasource.username=u
spring.datasource.password=p
```
