---
title: "[Solution] Spring Transaction Manager Error"
description: "Transaction manager not found."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Transaction manager not found.

## Common Causes

Wrong config.

## How to Fix

Define manager.

## Example

```java
@Bean
public PlatformTransactionManager tm(EntityManagerFactory e) { return new JpaTransactionManager(e); }
```
