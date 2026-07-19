---
title: "[Solution] Java NoSuchBeanDefinitionException — bean only available for specific profile injected when inactive"
description: "Fix Java NoSuchBeanDefinitionException when bean only available for specific profile injected when inactive with proven solutions."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# NoSuchBeanDefinitionException — bean only available for specific profile injected when inactive

A `NoSuchBeanDefinitionException` occurs when @Profile("production")
@Service
public class ProductionService {}
// Injected in dev — NoSuchBeanDefinitionException.

## Common Causes

```java
@Profile("production")
@Service
public class ProductionService {}
// Injected in dev — NoSuchBeanDefinitionException
```

## Solutions

```java
// Fix: ConditionalOnMissingBean fallback
@ConditionalOnMissingBean(ProductionService.class)
@Service
public class DevService implements ProductionService {}

// Fix: ObjectProvider
@Autowired private ObjectProvider<ProductionService> ps;
ProductionService svc = ps.getIfAvailable();
```

## Prevention Checklist

- Provide fallback beans for all profiles.
- Use ObjectProvider for optional profile beans.
- Use @ConditionalOnMissingBean for defaults.
- Test all profile configurations.

## Related Errors

NoSuchBeanDefinitionException, BeanCreationException
