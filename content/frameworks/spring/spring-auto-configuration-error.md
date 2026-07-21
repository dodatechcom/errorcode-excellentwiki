---
title: "[Solution] spring Auto Configuration Error"
description: "Auto-config not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Auto-config not working.

## Common Causes

Wrong exclude.

## How to Fix

Exclude correctly.

## Example

```java
@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
public class App {}
```
