---
title: "[Solution] Spring Context Initialization Failed"
description: "App context fails to start."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

App context fails to start.

## Common Causes

Bean creation error.

## How to Fix

Check beans.

## Example

```java
@SpringBootApplication
public class App {
    public static void main(String[] a) { SpringApplication.run(App.class, a); }
}
```
