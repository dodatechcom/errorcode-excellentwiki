---
title: "[Solution] spring Swagger Error"
description: "Swagger docs not generating."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Swagger docs not generating.

## Common Causes

Wrong config.

## How to Fix

Configure swagger.

## Example

```java
@Bean
public OpenAPI customOpenAPI() {
    return new OpenAPI().info(new Info().title("My API").version("1.0"));
}
```
