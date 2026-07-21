---
title: "[Solution] Spring Service Layer Error"
description: "Service not found."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Service not found.

## Common Causes

Not annotated.

## How to Fix

Add @Service.

## Example

```java
@Service
public class UserService {
    @Autowired private UserRepository repo;
}
```
