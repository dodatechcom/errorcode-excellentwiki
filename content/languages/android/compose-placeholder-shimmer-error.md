---
title: "Placeholder Shimmer Error"
description: "Fix Compose placeholder and shimmer loading state errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Placeholder content does not show correctly or shimmer animation not working

## Common Causes

- Placeholder not displayed during image load
- Shimmer effect not animating
- Placeholder size not matching content
- Shimmer causing performance issues on scroll

## Fixes

- Use placeholder parameter in AsyncImage
- Use custom shimmer modifier during loading
- Match placeholder size to content dimensions
- Disable shimmer on fast scroll

## Code Example

```kotlin
@Composable
fun ImageWithPlaceholder(imageUrl: String) {
    var isLoading by remember { mutableStateOf(true) }

    AsyncImage(
        model = ImageRequest.Builder(LocalContext.current)
            .data(imageUrl)
            .listener(
                onStart = { isLoading = true },
                onSuccess = { _, _ -> isLoading = false },
                onError = { _, _ -> isLoading = false }
            )
            .build(),
        contentDescription = null,
        placeholder = if (isLoading) {
            painterResource(R.drawable.placeholder)
        } else null,
        modifier = Modifier.fillMaxWidth().height(200.dp)
    )
}
```

# placeholder: shown during image loading
# error: shown on load failure
# crossfade: smooth transition from placeholder
# Listener for loading state tracking
