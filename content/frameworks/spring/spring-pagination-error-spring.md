---
title: "[Solution] Spring Pagination Error Spring"
description: "Pagination not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Pagination not working.

## Common Causes

Wrong parameter.

## How to Fix

Use Pageable.

## Example

```java
@GetMapping
public Page<User> getUsers(Pageable p) { return repo.findAll(p); }
```
