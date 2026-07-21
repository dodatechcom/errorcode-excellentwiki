---
title: "[Solution] Spring Conditional Bean Error"
description: "Bean not created conditionally."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Bean not created conditionally.

## Common Causes

Wrong condition.

## How to Fix

Use @ConditionalOnProperty.

## Example

```java
@Bean
@ConditionalOnProperty(name = "feature.enabled", havingValue = "true")
public FeatureService fs() { return new FeatureService(); }
```
