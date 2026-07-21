---
title: "[Solution] Deprecated Function Migration: getString() to requireContext().getString()"
description: "Migrate from deprecated getString() to requireContext().getString()."
deprecated_function: "getString(R.string.app_name)"
replacement_function: "requireContext().getString(R.string.app_name)"
languages: ["android"]
deprecated_since: "AndroidX Fragment 1.3+"
---

# [Solution] Deprecated Function Migration: getString() to requireContext().getString()

The `getString(R.string.app_name)` has been deprecated in favor of `requireContext().getString(R.string.app_name)`.

## Migration Guide

requireContext() is safer.

## Before (Deprecated)

```android
val name = getString(R.string.app_name)
```

## After (Modern)

```android
val name = requireContext().getString(R.string.app_name)
```

## Key Differences

- requireContext() is safer
