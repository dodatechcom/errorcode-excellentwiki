---
title: "Activity Lifecycle Crash"
description: "Fix Android activity lifecycle crash errors from configuration changes"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Activity crashes during configuration change because state is not preserved

## Common Causes

- Activity recreated without saving instance state
- onSaveInstanceState not called before destruction
- Fragment not properly retained across configuration changes
- ViewModel lost because activity recreated

## Fixes

- Override onSaveInstanceState to save critical state
- Use ViewModel to survive configuration changes
- Use FragmentManager to retain fragments
- Use android:configChanges only as last resort

## Code Example

```kotlin
class MyActivity : AppCompatActivity() {
    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putString("search_query", searchEditText.text.toString())
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val savedQuery = savedInstanceState?.getString("search_query") ?: ""
        searchEditText.setText(savedQuery)
    }
}
```

# ViewModel survives configuration changes
# onSaveInstanceState for small UI state
# Use rememberSaveable in Compose
