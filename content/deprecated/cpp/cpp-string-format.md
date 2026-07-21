---
title: "[Solution] Deprecated Function Migration: sprintf to fmt::format or std::format"
description: "Migrate from deprecated sprintf to fmt::format."
deprecated_function: "sprintf with format string"
replacement_function: "fmt::format or std::format"
languages: ["cpp"]
deprecated_since: "C++20/fmt"
---

# [Solution] Deprecated Function Migration: sprintf to fmt::format or std::format

The `sprintf(buf, "%s: %d", name, value)` has been deprecated in favor of `fmt::format("{}: {}", name, value)`.

## Migration Guide

format is type-safe.

## Before (Deprecated)

```cpp
char buf[100];
sprintf(buf, "%s: %d", name, value);
```

## After (Modern)

```cpp
std::string result = std::format("{}: {}", name, value);
```

## Key Differences

- format is type-safe
