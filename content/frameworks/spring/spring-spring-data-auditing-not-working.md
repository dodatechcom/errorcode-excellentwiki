---
title: "[Solution] spring Spring Data Auditing Not Working"
description: "Auditing fields not auto-populated."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Auditing fields not auto-populated.

## Common Causes

@EnableJpaAuditing missing.

## How to Fix

Add @EnableJpaAuditing to config.

## Example

```java
@Configuration
@EnableJpaAuditing
public class JpaConfig {}
```
