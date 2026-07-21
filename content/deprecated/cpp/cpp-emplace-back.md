---
title: "[Solution] Deprecated Function Migration: push_back to emplace_back"
description: "Migrate from deprecated push_back to emplace_back."
deprecated_function: "vec.push_back(T(args))"
replacement_function: "vec.emplace_back(args)"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: push_back to emplace_back

The `vec.push_back(T(args))` has been deprecated in favor of `vec.emplace_back(args)`.

## Migration Guide

emplace_back constructs in place.

## Before (Deprecated)

```cpp
vec.push_back(MyClass(arg1, arg2));
```

## After (Modern)

```cpp
vec.emplace_back(arg1, arg2);
```

## Key Differences

- emplace_back constructs in place
