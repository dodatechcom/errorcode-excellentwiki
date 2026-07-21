---
title: "[Solution] Spring Transactional Error"
description: "@Transactional not committing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

@Transactional not committing.

## Common Causes

Wrong propagation.

## How to Fix

Check settings.

## Example

```java
@Transactional
public void save(User u) { repo.save(u); }
```
