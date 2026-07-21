---
title: "[Solution] Spring Cache Abstraction Error"
description: "Cache not storing."
frameworks: ["spring"]
error-types: ["framework-error"]
severities: ["error"]
---

Cache not storing.

## Common Causes

Manager not configured.

## How to Fix

Configure.

## Example

```java
@Bean
public CacheManager cm() { return new ConcurrentMapCacheManager(); }
```
