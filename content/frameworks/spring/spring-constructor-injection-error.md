---
title: "[Solution] Spring Constructor Injection Error"
description: "Injection not working via constructor."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Injection not working via constructor.

## Common Causes

Missing @Autowired.

## How to Fix

Use constructor injection.

## Example

```java
@Service
public class UserService {
    private final UserRepository repo;
    public UserService(UserRepository repo) { this.repo = repo; }
}
```
