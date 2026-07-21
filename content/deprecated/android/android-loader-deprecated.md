---
title: "[Solution] Deprecated Function Migration: Loader to ViewModel + LiveData"
description: "Migrate from deprecated Loader to ViewModel + LiveData."
deprecated_function: "CursorLoader / AsyncTaskLoader"
replacement_function: "ViewModel + LiveData / Flow"
languages: ["android"]
deprecated_since: "Android Architecture Components"
---

# [Solution] Deprecated Function Migration: Loader to ViewModel + LiveData

The `CursorLoader / AsyncTaskLoader` has been deprecated in favor of `ViewModel + LiveData / Flow`.

## Migration Guide

Loaders were deprecated.

## Before (Deprecated)

```android
class MyLoader : AsyncTaskLoader<String>(context) {
    override fun loadInBackground() = fetchData()
}
```

## After (Modern)

```android
class MyViewModel : ViewModel() {
    val data: LiveData<Result> = liveData {
        emit(Result.Loading)
        emit(Result.Success(fetchData()))
    }
}
```

## Key Differences

- ViewModel + LiveData is the modern approach
