---
title: "[Solution] Spring Health Indicator Error"
description: "Custom health indicator not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom health indicator not working.

## Common Causes

Not implementing interface.

## How to Fix

Implement HealthIndicator.

## Example

```java
@Component
public class DBHealth implements HealthIndicator {
    public Health health() { return Health.up().build(); }
}
```
