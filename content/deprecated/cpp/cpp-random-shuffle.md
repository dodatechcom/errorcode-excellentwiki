---
title: "[Solution] Deprecated Function Migration: random_shuffle to shuffle"
description: "Migrate from deprecated random_shuffle to shuffle."
deprecated_function: "random_shuffle(begin, end)"
replacement_function: "shuffle(begin, end, rng)"
languages: ["cpp"]
deprecated_since: "C++14"
---

# [Solution] Deprecated Function Migration: random_shuffle to shuffle

The `random_shuffle(begin, end)` has been deprecated in favor of `shuffle(begin, end, rng)`.

## Migration Guide

shuffle uses explicit engine.

## Before (Deprecated)

```cpp
random_shuffle(v.begin(), v.end());
```

## After (Modern)

```cpp
mt19937 g(random_device{}());
shuffle(v.begin(), v.end(), g);
```

## Key Differences

- shuffle uses explicit engine
