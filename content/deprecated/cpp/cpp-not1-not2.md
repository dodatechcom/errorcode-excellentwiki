---
title: "[Solution] Deprecated Function Migration: not1/not2 to lambdas"
description: "Migrate from deprecated not1/not2 to lambdas."
deprecated_function: "not1(pred)"
replacement_function: "lambda expression"
languages: ["cpp"]
deprecated_since: "C++11"
---

# [Solution] Deprecated Function Migration: not1/not2 to lambdas

The `not1(pred)` has been deprecated in favor of `lambda expression`.

## Migration Guide

not1/not2 were removed in C++17.

## Before (Deprecated)

```cpp
remove_if(v.begin(), v.end(), not1(pred));
```

## After (Modern)

```cpp
remove_if(v.begin(), v.end(), [](int x) { return !pred(x); });
```

## Key Differences

- not1/not2 were removed in C++17
