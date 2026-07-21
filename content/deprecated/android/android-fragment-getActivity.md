---
title: "[Solution] Deprecated Function Migration: getActivity() to requireActivity()"
description: "Migrate from deprecated getActivity() to requireActivity()."
deprecated_function: "getActivity()"
replacement_function: "requireActivity()"
languages: ["android"]
deprecated_since: "AndroidX Fragment 1.3+"
---

# [Solution] Deprecated Function Migration: getActivity() to requireActivity()

The `getActivity()` has been deprecated in favor of `requireActivity()`.

## Migration Guide

requireActivity() throws on null.

## Before (Deprecated)

```android
val activity = getActivity()
```

## After (Modern)

```android
val activity = requireActivity()
```

## Key Differences

- requireActivity() is safer
