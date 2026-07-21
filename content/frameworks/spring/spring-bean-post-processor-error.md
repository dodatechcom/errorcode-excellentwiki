---
title: "[Solution] Spring Bean Post Processor Error"
description: "BeanPostProcessor not modifying beans."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

BeanPostProcessor not modifying beans.

## Common Causes

Not implementing interface.

## How to Fix

Implement BeanPostProcessor.

## Example

```java
@Component
public class CustomBPP implements BeanPostProcessor {
    public Object postProcessAfterInitialization(Object bean, String name) { return bean; }
}
```
