---
title: "[Solution] Deprecated Function Migration: observe(this, Observer) to viewLifecycleOwner"
description: "Migrate from deprecated observe(this, Observer) to viewLifecycleOwner."
deprecated_function: "viewModel.data.observe(this, Observer { })"
replacement_function: "viewModel.data.observe(viewLifecycleOwner) { }"
languages: ["android"]
deprecated_since: "AndroidX Fragment 1.2+"
---

# [Solution] Deprecated Function Migration: observe(this, Observer) to viewLifecycleOwner

The `viewModel.data.observe(this, Observer { })` has been deprecated in favor of `viewModel.data.observe(viewLifecycleOwner) { }`.

## Migration Guide

viewLifecycleOwner prevents memory leaks.

## Before (Deprecated)

```android
viewModel.data.observe(this, Observer { data ->
    updateUI(data)
})
```

## After (Modern)

```android
viewModel.data.observe(viewLifecycleOwner) { data ->
    updateUI(data)
}
```

## Key Differences

- viewLifecycleOwner prevents leaks
