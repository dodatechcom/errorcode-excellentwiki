---
title: "[Solution] Spring CORS Config Error"
description: "CORS not allowing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

CORS not allowing.

## Common Causes

Not configured.

## How to Fix

Add config.

## Example

```java
@Bean
public CorsConfigurationSource ccs() {
    CorsConfiguration c = new CorsConfiguration();
    c.addAllowedOrigin("http://localhost:3000");
    UrlBasedCorsConfigurationSource s = new UrlBasedCorsConfigurationSource();
    s.registerCorsConfiguration("/**", c);
    return s;
}
```
