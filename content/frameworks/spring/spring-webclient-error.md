---
title: "[Solution] Spring WebClient Error"
description: "WebClient not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

WebClient not working.

## Common Causes

Wrong config.

## How to Fix

Configure.

## Example

```java
WebClient c = WebClient.baseUrl("https://api.example.com").build();
Mono<String> r = c.get().uri("/d").retrieve().bodyToMono(String.class);
```
