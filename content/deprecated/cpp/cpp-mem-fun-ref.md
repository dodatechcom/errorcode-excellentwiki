---
title: "[Solution] Deprecated Function Migration: mem_fun_ref to member function pointer"
description: "Migrate from deprecated mem_fun_ref to member function pointer."
deprecated_function: "mem_fun_ref(&Class::method)"
replacement_function: "&Class::method"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: mem_fun_ref to member function pointer

The `mem_fun_ref(&Class::method)` has been deprecated in favor of `&Class::method`.

## Migration Guide

mem_fun_ref was removed in C++17.

## Before (Deprecated)

```cpp
for_each(v.begin(), v.end(), mem_fun_ref(&Foo::bar));
```

## After (Modern)

```cpp
for_each(v.begin(), v.end(), &Foo::bar);
```

## Key Differences

- mem_fun_ref was removed in C++17
