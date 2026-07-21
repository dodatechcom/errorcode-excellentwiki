---
title: "[Solution] Deprecated Function Migration: Job to SupervisorJob for child failure isolation"
description: "Migrate from deprecated Job to SupervisorJob for child failure isolation."
deprecated_function: "Job()"
replacement_function: "SupervisorJob()"
languages: ["kotlin"]
deprecated_since: "Kotlin Coroutines"
---

# [Solution] Deprecated Function Migration: Job to SupervisorJob for child failure isolation

The `Job()` has been deprecated in favor of `SupervisorJob()`.

## Migration Guide

SupervisorJob isolates child failures.

## Before (Deprecated)

```kotlin
val job = Job()
```

## After (Modern)

```kotlin
val job = SupervisorJob()
```

## Key Differences

- SupervisorJob isolates child failures
