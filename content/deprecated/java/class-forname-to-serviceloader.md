---
title: "[Solution] Deprecated Function Migration: Class.forName to ServiceLoader"
description: "Migrate from deprecated Class.forName dynamic loading to ServiceLoader for service discovery."
deprecated_function: "Class.forName()"
replacement_function: "ServiceLoader"
languages: ["java"]
deprecated_since: "Java 6+"
---

# [Solution] Deprecated Function Migration: Class.forName to ServiceLoader

The `Class.forName()` has been deprecated in favor of `ServiceLoader`.

## Migration Guide

ServiceLoader provides standardized service discovery via META-INF/services.

## Before (Deprecated)

```java
try {
    Class<?> clazz = Class.forName("com.example.MyService");
    MyService service = (MyService) clazz.getDeclaredConstructor().newInstance();
    service.doWork();
} catch (Exception e) {
    e.printStackTrace();
}
```

## After (Modern)

```java
import java.util.ServiceLoader;

ServiceLoader<MyService> loader = ServiceLoader.load(MyService.class);
for (MyService service : loader) {
    service.doWork();
}

MyService service = loader.findFirst().orElseThrow();
```

## Key Differences

- ServiceLoader discovers via META-INF/services
- Type-safe without reflection casting
- Works with module system (JPMS)
