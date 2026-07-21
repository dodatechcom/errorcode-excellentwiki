---
title: "LazyColumn Empty State Error"
description: "Fix LazyColumn empty state and placeholder content display"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn does not show empty state when list is empty

## Common Causes

- Empty state not visible when items list is empty
- Placeholder not matching expected content layout
- Empty state not centered or styled
- Retry action not working from empty state

## Fixes

- Check for empty state before rendering LazyColumn
- Show centered empty state with action
- Match placeholder to expected content size
- Connect retry action to refresh method

## Code Example

```kotlin
@Composable
fun ItemList(items: List<Item>, onRetry: () -> Unit) {
    if (items.isEmpty()) {
        Column(
            modifier = Modifier.fillMaxSize(),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            Icon(Icons.Default.Inbox, null, modifier = Modifier.size(64.dp))
            Spacer(modifier = Modifier.height(16.dp))
            Text("No items found", style = MaterialTheme.typography.bodyLarge)
            Spacer(modifier = Modifier.height(8.dp))
            Button(onClick = onRetry) { Text("Retry") }
        }
    } else {
        LazyColumn {
            items(items, key = { it.id }) { item ->
                ItemRow(item)
            }
        }
    }
}
```

# Always handle empty state
# Center empty state with action
# Match placeholder to expected content
