---
title: "[Solution] Spring Native Query Error"
description: "SQL query failing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

SQL query failing.

## Common Causes

Wrong SQL.

## How to Fix

Fix query.

## Example

```java
@Query(value = "SELECT * FROM users WHERE email = ?1", nativeQuery = true)
User findByEmail(String e);
```
