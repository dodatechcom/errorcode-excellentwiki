---
title: "Memory Leak Error"
description: "Fix Android memory leak errors from activity references and static contexts"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
App consumes increasing memory because of unreleased object references

## Common Causes

- Activity reference held by static object
- Inner class holding implicit Activity reference
- Handler holding Activity reference after destroy
- Anonymous callback not properly cleaned up

## Fixes

- Use WeakReference for Activity references in background
- Make inner classes static with WeakReference
- Remove callbacks in onDestroy
- Use lifecycle-aware components

## Code Example

```kotlin
// WRONG: inner class holds Activity reference
class MyTask(activity: Activity) {
    fun run() { activity.showToast("Done") }  // LEAK!
}

// CORRECT: WeakReference
class MyTask(activity: Activity) {
    private val activityRef = WeakReference(activity)
    fun run() {
        activityRef.get()?.showToast("Done")
    }
}

// Use lifecycle-aware scope:
lifecycleScope.launch {
    // Automatically cancelled when lifecycle destroyed
}

// Use ViewBinding lifecycle-aware:
binding.lifecycleOwner = this
```

# Use LeakCanary to detect memory leaks
# Avoid static references to Activities
# Use lifecycleScope instead of GlobalScope
