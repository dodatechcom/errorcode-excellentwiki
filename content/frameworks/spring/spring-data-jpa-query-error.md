---
title: "[Solution] Spring Data JPA Query Error"
description: "JPA query method not found."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

JPA query method not found.

## Common Causes

Wrong method name.

## How to Fix

Follow naming conventions.

## Example

```java
public interface UR extends JpaRepository<User, Long> {
    List<User> findByAgeBetween(int min, int max);
}
```
