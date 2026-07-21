---
title: "[Solution] Deprecated Function Migration: AsyncTask to coroutines"
description: "Migrate from deprecated AsyncTask to coroutines."
deprecated_function: "AsyncTask"
replacement_function: "viewModelScope.launch"
languages: ["android"]
deprecated_since: "Android 11+"
---

# [Solution] Deprecated Function Migration: AsyncTask to coroutines

The `AsyncTask` has been deprecated in favor of `viewModelScope.launch`.

## Migration Guide

AsyncTask was deprecated in API 30.

## Before (Deprecated)

```android
class MyTask : AsyncTask<Void, Void, String>() {
    override fun doInBackground(vararg params: Void?) = fetchData()
    override fun onPostExecute(result: String) { updateUI(result) }
}
```

## After (Modern)

```android
lifecycleScope.launch {
    val result = withContext(Dispatchers.IO) { fetchData() }
    updateUI(result)
}
```

## Key Differences

- Coroutines are the modern approach
