---
title: "[Solution] MyBatis-Plus DataIntegrityViolationException Fix"
description: "Fix MyBatis-Plus DataIntegrityViolationException when base methods violate database constraints."
languages: ["java"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["mybatis-plus", "data-integrity", "base-mapper", "insert", "constraint"]
weight: 5
---

# MyBatis-Plus DataIntegrityViolationException Fix

A `DataIntegrityViolationException` in MyBatis-Plus occurs when a BaseMapper method (insert, update) violates database constraints. This wraps the underlying SQL exception.

## What This Error Means

Common message:

- `DataIntegrityViolationException: Duplicate entry for key`
- `DataIntegrityViolationException: Column cannot be null`

## Common Causes

```java
// Cause 1: Duplicate key on insert
UserMapper userMapper = ...;
User user = new User();
user.setEmail("existing@email.com");  // Unique constraint
userMapper.insert(user);  // DataIntegrityViolationException

// Cause 2: Null value on NOT NULL column
User user = new User();
user.setName(null);  // Column has NOT NULL constraint
userMapper.insert(user);
```

## How to Fix

### Fix 1: Check before insert

```java
@Service
public class UserService {

    @Autowired
    private UserMapper userMapper;

    public void createUser(User user) {
        LambdaQueryWrapper<User> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(User::getEmail, user.getEmail());
        if (userMapper.selectCount(wrapper) > 0) {
            throw new DuplicateEmailException("Email already exists");
        }
        userMapper.insert(user);
    }
}
```

### Fix 2: Handle exception

```java
try {
    userMapper.insert(user);
} catch (DataIntegrityViolationException ex) {
    if (ex.getMessage().contains("Duplicate entry")) {
        throw new BusinessException("Duplicate entry");
    }
    throw ex;
}
```

### Fix 3: Use saveOrUpdate

```java
IService<User> userService = ...;
userService.saveOrUpdate(user);  // Insert or update based on ID
```

## Related Errors

- {{< relref "mybatis" >}} — BindingException: Invalid bound statement
- {{< relref "mybatis-dynamic" >}} — Dynamic SQL binding errors
- {{< relref "jpa-constraint" >}} — ConstraintViolationException
