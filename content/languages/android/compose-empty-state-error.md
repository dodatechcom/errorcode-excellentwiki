---
title: "Empty State Error"
description: "Fix Compose empty state and placeholder content display errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Empty state not showing correctly or placeholder not matching content size

## Common Causes

- Empty state not visible when list is empty
- Placeholder size not matching expected content
- Empty state message not user-friendly
- Retry action not working from empty state

## Fixes

- Check for empty state before rendering list
- Match placeholder size to content dimensions
- Use friendly message with retry action
- Use AnimatedContent for smooth transitions

## Code Example

```kotlin
@Composable
fun ItemList(items: List<Item>) {
    if (items.isEmpty()) {
        EmptyState(
            message = "No items found",
            actionText = "Refresh",
            onAction = { viewModel.refresh() }
        )
    } else {
        LazyColumn {
            items(items, key = { it.id }) { item ->
                ItemRow(item)
            }
        }
    }
}

@Composable
fun EmptyState(message: String, actionText: String, onAction: () -> Unit) {
    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Icon(Icons.Default.Inbox, null, modifier = Modifier.size(64.dp))
        Spacer(modifier = Modifier.height(16.dp))
        Text(message, style = MaterialTheme.typography.bodyLarge)
        Spacer(modifier = Modifier.height(8.dp))
        Button(onClick = onAction) { Text(actionText) }
    }
}
```

# Always handle empty state
# Show friendly message and retry action
# Match placeholder to expected content size
