---
title: "[Solution] Java NoSuchBeanDefinitionException — Spring cannot find a bean of requested type or name"
description: "Fix Java NoSuchBeanDefinitionException when spring cannot find a bean of requested type or name with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoSuchBeanDefinitionException — Spring cannot find a bean of requested type or name

A `NoSuchBeanDefinitionException` occurs when @Autowired private UserService userService;  // NoSuchBeanDefinitionException.

## Common Causes

```java
@Autowired private UserService userService;  // NoSuchBeanDefinitionException
```

## Solutions

```java
// Fix: ensure bean registered
@Service public class UserServiceImpl implements UserService {}

// Fix: @Primary for multiple
@Service @Primary public class UserServiceImpl implements UserService {}

// Fix: ObjectProvider
@Autowired private ObjectProvider<UserService> sp;
UserService svc = sp.getIfAvailable();

// Fix: @ConditionalOnMissingBean
@ConditionalOnMissingBean(UserService.class)
@Service
public class DefaultUserService implements UserService {}
```

## Prevention Checklist

- Ensure classes have @Service/@Component/@Bean.
- Use @Primary for default implementation.
- Use @ConditionalOnMissingBean for defaults.
- Check component scan paths.

## Related Errors

BeanCreationException, IllegalArgumentException
