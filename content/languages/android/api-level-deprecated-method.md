---
title: "Deprecated Method Usage"
description: "Fix deprecated API method errors and migration warnings in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Lint warns about using deprecated Android APIs that may be removed

## Common Causes

- Using deprecated startActivity result API
- Legacy AsyncTask instead of coroutines
- Deprecated Fragment constructor
- Using ConnectivityManager.getActiveNetworkInfo()

## Fixes

- Migrate to ActivityResultLauncher for activity results
- Replace AsyncTask with Kotlin coroutines or RxJava
- Use FragmentContainerView with Navigation
- Use ConnectivityManager.getNetworkCapabilities() instead

## Code Example

```kotlin
// Deprecated:
startActivityForResult(intent, REQUEST_CODE)

// Modern replacement:
val launcher = registerForActivityResult(
    ActivityResultContracts.StartActivityForResult()
) { result ->
    if (result.resultCode == RESULT_OK) {
        val data = result.data
    }
}
```

# Common deprecated APIs and replacements:
# AsyncTask -> Coroutines
# Fragment.newInstance() -> NavArgs
# Loader -> Room + LiveData
# AlarmManager.set() -> setExactAndAllowWhileIdle()
