---
title: "LiveData Transformation Error"
description: "Fix LiveData transformation errors with map and switchMap"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LiveData transformations produce unexpected results or memory leaks

## Common Causes

- switchMap returning null LiveData
- map transformation not triggering on source change
- Transformation creating circular dependency
- MediatorLiveData not properly configured

## Fixes

- Ensure switchMap function returns non-null LiveData
- Verify source LiveData is being updated
- Avoid circular dependencies between transformations
- Use MediatorLiveData for complex multi-source transformations

## Code Example

```kotlin
// map transformation
val userName: LiveData<String> = userLiveData.map { user ->
    user.name
}

// switchMap transformation
val userPosts: LiveData<List<Post>> = userId.switchMap { id ->
    repository.getPostsForUser(id)
}

// MediatorLiveData for multiple sources
val combined = MediatorLiveData<UiState>()
combined.addSource(userLiveData) { user ->
    combined.value = UiState.UserLoaded(user)
}
combined.addSource(postsLiveData) { posts ->
    combined.value = UiState.PostsLoaded(posts)
}
```

# map: transforms value directly
# switchMap: transforms to new LiveData
# MediatorLiveData: combines multiple sources
