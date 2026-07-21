---
title: "Compose Recomposition Error"
description: "Fix Jetpack Compose recomposition performance issues and unnecessary recompositions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose UI recomposes too frequently causing performance problems

## Common Causes

- Unstable parameter types causing recomposition
- Lambda parameters not properly remembered
- Reading mutableStateOf outside Composable
- Using key{} incorrectly or missing keys in LazyColumn

## Fixes

- Use @Immutable or @Stable annotations on data classes
- Remember lambdas with remember{}
- Use derivedStateOf for derived state
- Add keys to LazyColumn items

## Code Example

```kotlin
@Stable
data class User(val name: String, val age: Int)

@Composable
fun UserList(users: List<User>) {
    LazyColumn {
        items(users, key = { it.name }) { user ->
            UserCard(user)  // Won't recompose if user unchanged
        }
    }
}
```

# Use stable types for parameters
# Use remember and derivedStateOf
# Profile with Layout Inspector recompose counter
