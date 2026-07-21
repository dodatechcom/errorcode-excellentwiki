---
title: "[Solution] Spring Factory Bean Error"
description: "Factory bean not creating instances."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Factory bean not creating instances.

## Common Causes

Wrong definition.

## How to Fix

Implement FactoryBean.

## Example

```java
@Component
public class MyFactory implements FactoryBean<MyObj> {
    public MyObj getObject() { return new MyObj(); }
    public Class<?> getObjectType() { return MyObj.class; }
}
```
