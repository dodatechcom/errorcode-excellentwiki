---
title: "Compose Preview Error"
description: "Fix Android Studio Compose preview configuration and rendering errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose preview in Android Studio fails to render or shows wrong content

## Common Causes

- Preview function not properly annotated
- Missing @Preview annotation parameters
- Preview function has parameters it should not
- Theme not applied in preview

## Fixes

- Add @Preview annotation to preview function
- Use showBackground, showSystemUi parameters
- Preview functions must have no parameters
- Wrap content with theme composable in preview

## Code Example

```kotlin
@Preview(showBackground = true, showSystemUi = true)
@Composable
fun PreviewMyScreen() {
    MyTheme {
        MyScreen(
            user = User("Preview User", 25),
            onClick = {}
        )
    }
}

@Preview(name = "Dark Mode", uiMode = UI_MODE_NIGHT_YES)
@Composable
fun PreviewMyScreenDark() {
    MyTheme(darkTheme = true) {
        MyScreen(user = User("Dark User", 30), onClick = {})
    }
}
```

# Preview tips:
# - Build project first if preview not rendering
# - Invalidate caches if preview stuck
# - Add @Preview for different screen sizes
