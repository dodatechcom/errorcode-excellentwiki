---
title: "[Solution] Kotlin Compose Excessive Recomposition — Skippable/Unstable"
description: "Fix Compose excessive recomposition. Learn how to make composables skippable, avoid unstable parameters, and reduce recompositions."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 1019
---

## What This Error Means

Excessive recomposition occurs when Compose recomposes composables more often than necessary, causing performance degradation. This is triggered by unstable parameter types, lambda recomposition, or state changes in unrelated scopes.

## Common Causes

- Passing non-data-class or non-`@Stable` types as parameters
- Creating lambdas inside composable bodies (new instance each recomposition)
- Using `var` state that triggers unnecessary recomposition
- Collections (`List`, `Map`) are unstable by default in Compose compiler

```kotlin
// Unstable: data class with mutable collection
data class UiState(val items: List<String>)  // List is unstable

@Composable
fun ItemList(state: UiState) { ... }
// Recomposes on every recomposition even if items unchanged
```

## How to Fix

**1. Use @Immutable or @Stable annotations**

```kotlin
@Immutable
data class UiState(val items: List<String>)

// Or use kotlinx.collections.immutable
data class UiState(val items: ImmutableList<String>)
```

**2. Extract lambda parameters to stable types**

```kotlin
// WRONG: Lambda created each recomposition
@Composable
fun Button(onClick: () -> Unit) { ... }

// CORRECT: Use stable reference
@Composable
fun Button(onClick: () -> Unit) { ... }  // Still fine if passed from stable scope
```

**3. Use derivedStateOf to reduce recomposition scope**

```kotlin
val scrollState = rememberLazyListState()
val showButton by remember {
    derivedStateOf { scrollState.firstVisibleItemIndex > 0 }
}
```

**4. Use key() to help Compose identify items**

```kotlin
LazyColumn {
    items(users, key = { it.id }) { user ->
        UserCard(user)  // Only recomposes for changed users
    }
}
```

**5. Profile with Compose compiler metrics**

```kotlin
// build.gradle.kts
android {
    buildFeatures { compose = true }
}
tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {
    compilerOptions {
        freeCompilerArgs.addAll("-P", "plugin:androidx.compose.compiler.plugins.kotlin:metricsDestination=${project.buildDir}/compose-metrics")
    }
}
```

## Examples

```kotlin
// Example 1: Stable vs unstable
@Immutable
data class User(val id: Long, val name: String)  // Stable

@Composable
fun UserCard(user: User) {
    Text(user.name)  // Only recomposes when user changes
}

// Example 2: remember for expensive computations
@Composable
fun FilteredList(query: String, items: List<String>) {
    val filtered = remember(query) {
        items.filter { it.contains(query) }
    }
    LazyColumn {
        items(filtered) { Text(it) }
    }
}

// Example 3: CompositionLocal for deep prop drilling
val LocalUser = compositionLocalOf<User> { error("No user") }
```

## Related Errors

- [Compose side effect error](kotlin-compose-side-effect) — side effect lifecycle
- [Compose preview error](kotlin-compose-preview-error) — preview rendering
- [Compose modifier error](kotlin-compose-modifier-error) — modifier issues
