---
title: "[Solution] Deprecated Function Migration: ViewModelProviders to viewModels() delegate"
description: "Migrate from deprecated ViewModelProviders.of() to viewModels() delegate."
deprecated_function: "ViewModelProviders.of(activity)"
replacement_function: "by viewModels()"
languages: ["kotlin"]
deprecated_since: "AndroidX 2.2+"
---

# [Solution] Deprecated Function Migration: ViewModelProviders to viewModels() delegate

The `ViewModelProviders.of(activity)` has been deprecated in favor of `by viewModels()`.

## Migration Guide

The viewModels() delegate is the modern way to obtain ViewModels.

## Before (Deprecated)

```kotlin
val viewModel = ViewModelProviders.of(this).get(MyViewModel::class.java)
val viewModel = ViewModelProviders.of(this, factory).get(MyViewModel::class.java)
```

## After (Modern)

```kotlin
val viewModel by viewModels<MyViewModel>()
val viewModel by viewModels { MyViewModelFactory(repository) }
```

## Key Differences

- viewModels() is a Kotlin delegate
- Factory can be passed as lambda
- Much less boilerplate
- Same lifecycle behavior
