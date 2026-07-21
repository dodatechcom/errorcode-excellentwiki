---
title: "[Solution] Deprecated Function Migration: AsyncTask to Kotlin coroutines"
description: "Migrate from deprecated AsyncTask to Kotlin coroutines for background work."
deprecated_function: "AsyncTask"
replacement_function: "Kotlin coroutines / WorkManager"
languages: ["kotlin"]
deprecated_since: "Android 11 (API 30)"
---

# [Solution] Deprecated Function Migration: AsyncTask to Kotlin coroutines

The `AsyncTask` has been deprecated in favor of `Kotlin coroutines / WorkManager`.

## Migration Guide

AsyncTask is deprecated due to memory leaks and lifecycle issues.

## Before (Deprecated)

```kotlin
class FetchTask extends AsyncTask<String, Void, String> {
    @Override
    protected String doInBackground(String... urls) {
        return fetchData(urls[0]);
    }
    @Override
    protected void onPostExecute(String result) {
        textView.setText(result);
    }
}
new FetchTask().execute("https://api.example.com");
```

## After (Modern)

```kotlin
lifecycleScope.launch {
    val result = withContext(Dispatchers.IO) {
        fetchData("https://api.example.com")
    }
    textView.text = result
}

// With ViewModel
class MyViewModel : ViewModel() {
    fun fetchData() {
        viewModelScope.launch {
            val result = repository.getData()
            _data.value = result
        }
    }
}
```

## Key Differences

- lifecycleScope auto-cancels on destroy
- viewModelScope cancels when ViewModel cleared
- withContext switches coroutine context
- WorkManager for guaranteed execution
