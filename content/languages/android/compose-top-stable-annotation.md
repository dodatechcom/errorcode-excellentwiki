---
title: "Stable Type Error"
description: "Fix Compose performance by ensuring types are stable for smart recomposition skipping"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable receiving unstable types causing unnecessary recompositions

## Common Causes

- Composable recomposing because parameter type is unstable
- Immutable annotation missing on data class
- List parameter causing recomposition on every parent recompose
- Callback lambda causing recomposition

## Fixes

- Use @Immutable or @Stable annotations
- Use stable collection types
- Remember callback lambdas
- Verify with Compose compiler report

## Code Example

```kotlin
@Immutable
data class User(val name: String, val email: String)

// For collections, use kotlinx.collections.immutable
@Composable
fun UserList(users: ImmutableList<User>) {
    LazyColumn {
        items(users, key = { it.email }) { user ->
            UserRow(user)
        }
    }
}

// Remember callbacks:
val onClick = remember { { user: User -> openUser(user) } }
```

# @Immutable: all properties are stable# @Stable: runtime stable# ImmutableList: stable collection# Remember callbacks to prevent recomposition
