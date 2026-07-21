---
title: "[Solution] Spring Configuration Properties Error"
description: "Config properties not binding."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Config properties not binding.

## Common Causes

Wrong prefix.

## How to Fix

Use @ConfigurationProperties.

## Example

```java
@ConfigurationProperties(prefix = "app")
public class AppProps {
    private String name;
}
```
