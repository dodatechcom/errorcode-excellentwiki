---
title: "[Solution] Deprecated Function Migration: fragment transactions to Navigation Component"
description: "Migrate from deprecated fragment transactions to Navigation Component."
deprecated_function: "fragmentManager.beginTransaction().replace(...)"
replacement_function: "NavHostFragment / NavController"
languages: ["android"]
deprecated_since: "AndroidX Navigation"
---

# [Solution] Deprecated Function Migration: fragment transactions to Navigation Component

The `fragmentManager.beginTransaction().replace(...)` has been deprecated in favor of `NavHostFragment / NavController`.

## Migration Guide

Navigation Component is safer.

## Before (Deprecated)

```android
supportFragmentManager.beginTransaction()
    .replace(R.id.container, MyFragment())
    .commit()
```

## After (Modern)

```android
findNavController().navigate(R.id.action_to_fragment)
```

## Key Differences

- Navigation Component is safer
