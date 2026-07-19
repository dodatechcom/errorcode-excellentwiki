---
title: "[Solution] Java ClassNotFoundException — component scanner cannot find bean class due to package or classpath issues"
description: "Fix Java ClassNotFoundException when component scanner cannot find bean class due to package or classpath issues with code examples."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ClassNotFoundException — component scanner cannot find bean class due to package or classpath issues

A `ClassNotFoundException` occurs when @ComponentScan(basePackages="com.example.api")
// MyService in com.example.service — not scanned.

## Common Causes

```java
@ComponentScan(basePackages="com.example.api")
// MyService in com.example.service — not scanned
```

## Solutions

```java
// Fix: include all packages
@ComponentScan(basePackages={"com.example.api","com.example.service","com.example.config"})

// Fix: ConditionalOnClass for optional
@ConditionalOnClass(name="com.example.OptionalFeature")
@Configuration
public class OptionalFeatureConfig {}
```

## Prevention Checklist

- Ensure all modules are dependencies.
- Use @ComponentScan with correct packages.
- Use @ConditionalOnClass for optional deps.

## Related Errors

ClassNotFoundException, BeanCreationException
