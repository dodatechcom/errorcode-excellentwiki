---
title: "[Solution] Spring Bean Not Found Error"
description: "NoSuchBeanDefinitionException."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

NoSuchBeanDefinitionException.

## Common Causes

Bean not defined.

## How to Fix

Add @Component.

## Example

```java
@Component
public class MyService {}
```
