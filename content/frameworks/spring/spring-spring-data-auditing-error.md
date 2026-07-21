---
title: "[Solution] Spring Spring Data Auditing Error"
description: "Auditing not working."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Auditing not working.

## Common Causes

@EnableJpaAuditing missing.

## How to Fix

Add annotation.

## Example

```java
@Configuration @EnableJpaAuditing
public class JpaConfig {}
```
