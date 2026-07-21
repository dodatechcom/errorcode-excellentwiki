---
title: "[Solution] Deprecated Function Migration: Log.d in production to Timber"
description: "Migrate from deprecated Log.d in production to Timber."
deprecated_function: "Log.d(TAG, msg)"
replacement_function: "Timber.d(msg)"
languages: ["android"]
deprecated_since: "Timber library"
---

# [Solution] Deprecated Function Migration: Log.d in production to Timber

The `Log.d(TAG, msg)` has been deprecated in favor of `Timber.d(msg)`.

## Migration Guide

Timber is more flexible.

## Before (Deprecated)

```android
Log.d("MyTag", "Debug message")
```

## After (Modern)

```android
Timber.d("Debug message")
```

## Key Differences

- Timber is more flexible
