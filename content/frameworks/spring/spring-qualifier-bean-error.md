---
title: "[Solution] Spring Qualifier Bean Error"
description: "Ambiguous bean."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Ambiguous bean.

## Common Causes

Multiple beans.

## How to Fix

Use @Qualifier.

## Example

```java
@Autowired @Qualifier("specific")
private MyService svc;
```
