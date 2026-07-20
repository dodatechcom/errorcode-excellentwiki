---
title: "[Solution] Kotlin IllegalStateException: Reading a state that was created after a composition"
description: "Fix Jetpack Compose state errors when reading state created after composition. Learn how to properly manage Compose state lifecycle with State, remember, and derivedStateOf."
languages: ["kotlin"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# IllegalStateException: Reading a state that was created after a composition

This error occurs in Jetpack Compose when you read a `State` object that was created during a composition but is accessed outside the composition's lifecycle.

## Error Message

```
java.lang.IllegalStateException: Reading a state that was created after a composition. Use State<T> only in composition scope.
```

## Description

Jetpack Compose tracks reads and writes of `State` objects during the recomposition cycle. When you create a `mutableStateOf()` or `remember {}` value inside a `@Composable` function but then try to read it outside of the composition scope (for example, from a callback that fires after the composable has left the composition), Compose throws this exception.

This is common when using ViewModel state, coroutine callbacks, or shared mutable state objects that outlive the composable's lifecycle.

## Common Causes

- Reading `mutableStateOf` from a coroutine launched inside `LaunchedEffect` after the composable is disposed
- Storing state in a ViewModel and reading it from a disposed composable
- Using `remember` with a state that is accessed in a delayed callback
- Sharing `MutableState` across composables without proper scoping

## Solutions

### Solution 1: Use StateFlow or LiveData in the ViewModel

Expose state from the ViewModel as a `StateFlow` and collect it inside the composable using `collectAsState()`.

```kotlin
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

class MyViewModel : ViewModel() {
    private val _uiState = MutableStateFlow(UiState())
    val uiState: StateFlow<UiState> = _uiState

    fun loadData() {
        viewModelScope.launch {
            _uiState.value = _uiState.value.copy(loading = true)
            delay(2000)
            _uiState.value = _uiState.value.copy(data = "Loaded", loading = false)
        }
    }
}

data class UiState(
    val loading: Boolean = false,
    val data: String = ""
)
```

```kotlin
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue

@Composable
fun MyScreen(viewModel: MyViewModel = viewModel()) {
    val state by viewModel.uiState.collectAsState()

    if (state.loading) {
        CircularProgressIndicator()
    } else {
        Text(text = state.data)
    }
}
```

### Solution 2: Scope state to the composition using remember

Use `remember` with a composable scope so the state is only alive while the composable is in the composition.

```kotlin
import androidx.compose.runtime.*

@Composable
fun CounterScreen() {
    var count by remember { mutableIntStateOf(0) }

    Column {
        Text("Count: $count")
        Button(onClick = { count++ }) {
            Text("Increment")
        }
    }
}
```

### Solution 3: Use derivedStateOf for computed values

When you need a computed state that depends on other states, use `derivedStateOf` to avoid stale reads.

```kotlin
import androidx.compose.runtime.*

@Composable
fun FilteredList(items: List<String>, query: String) {
    val filteredItems by remember(query) {
        derivedStateOf {
            items.filter { it.contains(query, ignoreCase = true) }
        }
    }

    LazyColumn {
        items(filteredItems) { item ->
            Text(text = item)
        }
    }
}
```

## Prevention Tips

- Never read `mutableStateOf` from callbacks that outlive the composable
- Always collect `StateFlow` inside composables using `collectAsState()`
- Use `remember` to scope state to the composable lifecycle
- Avoid storing Compose `State` objects in singletons or application-scoped objects

## Related Errors

- [IllegalStateException]({{< relref "/languages/kotlin/illegal-state" >}}) — general state errors in Kotlin.
- [ConcurrentModificationException]({{< relref "/languages/kotlin/concurrentmodificationexception" >}}) — concurrent access to state.
- [NullPointerException]({{< relref "/languages/kotlin/null-pointer" >}}) — null state references.
