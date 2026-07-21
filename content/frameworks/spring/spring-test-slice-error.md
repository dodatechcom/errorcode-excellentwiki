---
title: "[Solution] spring Test Slice Error"
description: "Test slice not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Test slice not working.

## Common Causes

Wrong annotation.

## How to Fix

Use correct slice.

## Example

```java
@DataJpaTest
public class UserRepositoryTest {
    @Autowired private UserRepository repo;
}
```
