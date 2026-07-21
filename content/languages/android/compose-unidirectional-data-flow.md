---
title: "Unidirectional Data Flow Error"
description: "Fix unidirectional data flow implementation in Compose architecture"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Data flow is bidirectional causing state inconsistencies in Compose

## Common Causes

- State flowing both up and down
- Callback not properly passing events upward
- State mutation happening in composable
- Multiple sources of truth for same data

## Fixes

- Enforce state down, events up pattern
- Never mutate state directly in composable
- Use single source of truth in ViewModel
- Use callback functions for event passing

## Code Example

```kotlin
// CORRECT: Unidirectional flow
@Composable
fun TodoList(
    todos: List<Todo>,           // State DOWN from ViewModel
    onToggle: (Long) -> Unit,    // Event UP to ViewModel
    onDelete: (Long) -> Unit     // Event UP to ViewModel
) {
    LazyColumn {
        items(todos, key = { it.id }) { todo ->
            TodoItem(
                todo = todo,
                onToggle = { onToggle(todo.id) },
                onDelete = { onDelete(todo.id) }
            )
        }
    }
}

// WRONG: Bidirectional (avoid!)
// var todos by remember { mutableStateOf(listOf()) }  // State mutation in composable!
```

# State: ViewModel -> Composable (down)
# Events: Composable -> ViewModel (up)
# Single source of truth: ViewModel
# Never mutate state in composable
