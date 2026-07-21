---
title: "LiveData Sticky Event Error"
description: "Fix LiveData sticky event errors causing duplicate event processing in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LiveData re-delivers old events when new observer attaches causing duplicate processing

## Common Causes

- SingleLiveEvent does not properly clear events
- Event consumed multiple times by observers
- Fragment re-observes same event on configuration change
- Sticky broadcast re-emitted on re-attach

## Fixes

- Use SingleLiveEvent wrapper for one-time events
- Use Event wrapper class that marks consumed events
- Use Channel for events instead of LiveData
- Check event.consumed flag before processing

## Code Example

```kotlin
// Event wrapper for one-time events
open class Event<out T>(private val content: T) {
    var hasBeenHandled = false
        private set

    fun getContentIfNotHandled(): T? {
        return if (hasBeenHandled) {
            null
        } else {
            hasBeenHandled = true
            content
        }
    }
}

// In ViewModel:
private val _events = MutableLiveData<Event<String>>()
val events: LiveData<Event<String>> = _events

// In observer:
viewModel.events.observe(viewLifecycleOwner) { event ->
    event.getContentIfNotHandled()?.let { showToast(it)
    }
}
```

# Use Event wrapper for navigation, toasts, snackbar
# Use StateFlow for persistent UI state
# Channel is better for one-shot events
