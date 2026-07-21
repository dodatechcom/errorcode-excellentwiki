---
title: "[Solution] Deprecated Function Migration: getResources() to requireContext().getResources()"
description: "Migrate from deprecated getResources() to requireContext().getResources()."
deprecated_function: "getResources()"
replacement_function: "requireContext().getResources()"
languages: ["android"]
deprecated_since: "AndroidX Fragment 1.3+"
---

# [Solution] Deprecated Function Migration: getResources() to requireContext().getResources()

The `getResources()` has been deprecated in favor of `requireContext().getResources()`.

## Migration Guide

requireContext() is safer.

## Before (Deprecated)

```android
val res = getResources()
```

## After (Modern)

```android
val res = requireContext().getResources()
```

## Key Differences

- requireContext() is safer
