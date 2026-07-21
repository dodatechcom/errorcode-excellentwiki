---
title: "[Solution] Deprecated Function Migration: ViewModelProviders to viewModels()"
description: "Migrate from deprecated ViewModelProviders to viewModels()."
deprecated_function: "ViewModelProviders.of(this).get(MyViewModel::class.java)"
replacement_function: "by viewModels<MyViewModel>()"
languages: ["android"]
deprecated_since: "AndroidX Lifecycle 2.2+"
---

# [Solution] Deprecated Function Migration: ViewModelProviders to viewModels()

The `ViewModelProviders.of(this).get(MyViewModel::class.java)` has been deprecated in favor of `by viewModels<MyViewModel>()`.

## Migration Guide

viewModels() is simpler.

## Before (Deprecated)

```android
val viewModel = ViewModelProviders.of(this).get(MyViewModel::class.java)
```

## After (Modern)

```android
val viewModel by viewModels<MyViewModel>()
```

## Key Differences

- viewModels() is simpler
