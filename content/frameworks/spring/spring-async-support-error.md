---
title: "[Solution] Spring Async Support Error"
description: "@Async not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

@Async not working.

## Common Causes

@EnableAsync missing.

## How to Fix

Add annotation.

## Example

```java
@SpringBootApplication @EnableAsync
public class App {}
```
