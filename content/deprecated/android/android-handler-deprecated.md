---
title: "[Solution] Deprecated Function Migration: Handler(Looper.getMainLooper()) to CoroutineScope"
description: "Migrate from deprecated Handler to CoroutineScope."
deprecated_function: "Handler(Looper.getMainLooper()).post { }"
replacement_function: "lifecycleScope.launch(Dispatchers.Main) { }"
languages: ["android"]
deprecated_since: "AndroidX"
---

# [Solution] Deprecated Function Migration: Handler(Looper.getMainLooper()) to CoroutineScope

The `Handler(Looper.getMainLooper()).post { }` has been deprecated in favor of `lifecycleScope.launch(Dispatchers.Main) { }`.

## Migration Guide

Coroutines are more structured.

## Before (Deprecated)

```android
Handler(Looper.getMainLooper()).post {
    updateUI()
}
```

## After (Modern)

```android
lifecycleScope.launch(Dispatchers.Main) {
    updateUI()
}
```

## Key Differences

- Coroutines are more structured
