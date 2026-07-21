---
title: "State Hosting Pattern Error"
description: "Fix Compose state hosting pattern for reusable form components"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Reusable form components do not properly host and manage their state

## Common Causes

- Component not receiving value and onValueChange
- State mutation happening inside component
- Parent not receiving state changes from child
- Component not reusable because of internal state

## Fixes

- Use value and onValueChange parameters for state
- Never mutate state inside child component
- Pass state changes to parent through callbacks
- Make components stateless for reusability

## Code Example

```kotlin
// Stateless reusable component
@Composable
fun SearchBar(
    query: String,
    onQueryChange: (String) -> Unit,
    onSearch: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    OutlinedTextField(
        value = query,
        onValueChange = onQueryChange,
        modifier = modifier.fillMaxWidth(),
        placeholder = { Text("Search...") },
        keyboardActions = KeyboardActions(
            onSearch = { onSearch(query) }
        )
    )
}

// Parent manages state:
@Composable
fun ParentScreen() {
    var query by remember { mutableStateOf("") }
    SearchBar(
        query = query,
        onQueryChange = { query = it },
        onSearch = { viewModel.search(it) }
    )
}
```

# value: current state (down)
# onValueChange: state change callback (up)
# Component is stateless and reusable
# Parent owns and manages state
