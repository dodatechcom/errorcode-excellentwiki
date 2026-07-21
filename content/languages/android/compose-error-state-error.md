---
title: "Error State Display Error"
description: "Fix Compose error state display and retry mechanism implementation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Error state not showing or retry mechanism not working correctly

## Common Causes

- Error state not visible or not descriptive
- Retry button not triggering reload
- Error state not dismissable after successful retry
- Error message not matching actual error type

## Fixes

- Show clear error message with retry action
- Connect retry button to ViewModel refresh method
- Dismiss error state on successful data load
- Show different messages for different error types

## Code Example

```kotlin
@Composable
fun ErrorScreen(message: String, onRetry: () -> Unit) {
    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Icon(
            Icons.Default.ErrorOutline,
            contentDescription = null,
            modifier = Modifier.size(64.dp),
            tint = MaterialTheme.colorScheme.error
        )
        Spacer(modifier = Modifier.height(16.dp))
        Text(
            text = "Something went wrong",
            style = MaterialTheme.typography.titleMedium
        )
        Spacer(modifier = Modifier.height(8.dp))
        Text(
            text = message,
            style = MaterialTheme.typography.bodyMedium,
            textAlign = TextAlign.Center
        )
        Spacer(modifier = Modifier.height(16.dp))
        Button(onClick = onRetry) {
            Text("Retry")
        }
    }
}
```

# Clear error message
# Retry action button
# Match error type to appropriate message
# Show after data load fails
