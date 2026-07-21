---
title: "[Solution] Spring WebTestClient Error"
description: "WebTestClient not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

WebTestClient not working.

## Common Causes

Wrong configuration.

## How to Fix

Configure properly.

## Example

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
public class Test {
    @Autowired private WebTestClient client;
}
```
