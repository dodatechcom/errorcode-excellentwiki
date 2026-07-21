---
title: "Preview Error"
description: "Fix Compose preview function for Android Studio preview rendering"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose preview not rendering in Android Studio or showing errors

## Common Causes

- @Preview function not showing in design view
- Preview compilation failing
- Preview showing error instead of composable
- Preview not updating after code changes

## Fixes

- Ensure @Preview function is public and has no required parameters
- Check that preview function returns composable
- Verify preview parameters are correct
- Rebuild and invalidate caches

## Code Example

```kotlin
@Preview(showBackground = true)
@Composable
fun PreviewMyScreen() {
    MaterialTheme {
        MyScreen(data = previewData)
    }
}

@Preview(name = "Dark", showBackground = true)
@Preview(name = "Light", uiMode = Configuration.UI_MODE_NIGHT_NO)
@Composable
fun PreviewMyScreenThemes() {
    MaterialTheme {
        MyScreen(data = previewData)
    }
}
```

# @Preview: public function, no params# Preview data: use fake/default data# Multiple previews: stack @Preview annotations# Rebuild if preview not updating
