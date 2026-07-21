---
title: "[Solution] Spring JPARepository Error"
description: "Repository method wrong."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Repository method wrong.

## Common Causes

Wrong method name.

## How to Fix

Use naming convention.

## Example

```java
public interface UR extends JpaRepository<User, Long> {
    List<User> findByName(String n);
}
```
