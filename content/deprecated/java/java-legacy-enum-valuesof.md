---
title: "[Solution] Deprecated Function Migration: Enum.valueOf to valueOf with class literal"
description: "Migrate from deprecated Enum.valueOf to valueOf with class literal."
deprecated_function: "Enum.valueOf(MyEnum.class, name)"
replacement_function: "MyEnum.valueOf(name)"
languages: ["java"]
deprecated_since: "Java 5+"
---

# [Solution] Deprecated Function Migration: Enum.valueOf to valueOf with class literal

The `Enum.valueOf(MyEnum.class, name)` has been deprecated in favor of `MyEnum.valueOf(name)`.

## Migration Guide

valueOf is simpler.

## Before (Deprecated)

```java
MyEnum e = Enum.valueOf(MyEnum.class, "VALUE");
```

## After (Modern)

```java
MyEnum e = MyEnum.valueOf("VALUE");
```

## Key Differences

- valueOf is simpler
