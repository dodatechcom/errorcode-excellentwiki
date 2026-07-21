---
title: "Loading State Error"
description: "Fix Compose loading indicator and skeleton screen errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Loading indicator not showing or skeleton screen not matching content layout

## Common Causes

- Loading indicator not centered or visible
- Skeleton placeholder not matching content shape
- Loading state not transitioning smoothly
- Multiple loading states conflicting

## Fixes

- Center loading indicator with proper alignment
- Match skeleton to actual content dimensions
- Use AnimatedVisibility for smooth transitions
- Manage single loading state in ViewModel

## Code Example

```kotlin
@Composable
fun ContentScreen(uiState: UiState) {
    when (uiState) {
        is UiState.Loading -> {
            Box(
                modifier = Modifier.fillMaxSize(),
                contentAlignment = Alignment.Center
            ) {
                CircularProgressIndicator(modifier = Modifier.size(48.dp))
            }
        }
        is UiState.Success -> {
            LazyColumn {
                items(uiState.items) { item ->
                    ItemRow(item)
                }
            }
        }
        is UiState.Error -> {
            ErrorScreen(
                message = uiState.message,
                onRetry = { viewModel.retry() }
            )
        }
    }
}
```

# CircularProgressIndicator: determinate progress
# LinearProgressIndicator: horizontal bar
# Match skeleton to actual content layout
# Center loading indicators
