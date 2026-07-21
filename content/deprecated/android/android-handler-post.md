---
title: "[Solution] Deprecated Function Migration: Handler().post to coroutine dispatchers"
description: "Migrate from deprecated Handler().post() to coroutine dispatchers in Android."
deprecated_function: "Handler().post { }"
replacement_function: "withContext(Dispatchers.Main)"
languages: ["kotlin"]
deprecated_since: "Kotlin coroutines"
---

# [Solution] Deprecated Function Migration: Handler().post to coroutine dispatchers

The `Handler().post { }` has been deprecated in favor of `withContext(Dispatchers.Main)`.

## Migration Guide

Handler-based threading is verbose. Coroutines provide structured concurrency.

## Before (Deprecated)

```kotlin
Handler(Looper.getMainLooper()).post {
    textView.text = "Updated"
}

Handler(Looper.getMainLooper()).postDelayed({
    doSomething()
}, 1000)
```

## After (Modern)

```kotlin
lifecycleScope.launch {
    withContext(Dispatchers.Main) {
        textView.text = "Updated"
    }
}

lifecycleScope.launch {
    delay(1000)
    doSomething()
}
```

## Key Differences

- withContext(Dispatchers.Main) for UI thread
- delay() replaces postDelayed
- Structured concurrency prevents leaks
- No need for Handler objects
