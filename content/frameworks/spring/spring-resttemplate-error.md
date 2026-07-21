---
title: "[Solution] Spring RestTemplate Error"
description: "RestTemplate call failing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

RestTemplate call failing.

## Common Causes

Wrong URL.

## How to Fix

Configure correctly.

## Example

```java
RestTemplate rt = new RestTemplate();
ResponseEntity<String> r = rt.getForEntity("https://api.example.com/d", String.class);
```
