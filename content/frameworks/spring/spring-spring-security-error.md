---
title: "[Solution] Spring Spring Security Error"
description: "Security blocking request."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Security blocking request.

## Common Causes

Wrong config.

## How to Fix

Configure rules.

## Example

```java
@Configuration
public class Sec {
    @Bean
    public SecurityFilterChain fc(HttpSecurity h) throws Exception {
        h.authorizeHttpRequests(a -> a.anyRequest().permitAll());
        return h.build();
    }
}
```
