---
title: "[Solution] Spring Bean Scope Error"
description: "Bean scope not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Bean scope not working.

## Common Causes

Wrong scope.

## How to Fix

Set scope.

## Example

```java
@Component @Scope("prototype")
public class PrototypeBean {}
```
