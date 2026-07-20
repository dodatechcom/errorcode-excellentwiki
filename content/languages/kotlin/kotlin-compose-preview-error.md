---
title: "[Solution] Kotlin Compose Preview Error — @Preview Parameter and Rendering"
description: "Fix Compose @Preview rendering errors and parameter issues. Learn correct preview configuration and common preview pitfalls."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1021
---

## What This Error Means

Compose preview errors occur when @Preview annotations are misconfigured, the preview composable has unsupported parameters, or the preview rendering environment lacks required dependencies.

## Common Causes

- Preview composable has required parameters without defaults
- @Preview missing `name` or `showBackground` parameters
- Preview references ViewModels or injected dependencies not available in preview
- Using non-Composable functions inside preview that need runtime context

```kotlin
// ERROR: Preview composable has required parameter
@Preview
@Composable
fun UserCard(user: User) {  // User is not provided for preview
    Text(user.name)
}
```

## How to Fix

**1. Provide default parameter values for preview**

```kotlin
@Preview
@Composable
fun UserCardPreview() {
    UserCard(user = User(name = "Alice", age = 30))
}

@Composable
fun UserCard(user: User = User(name = "Preview", age = 25)) {
    Text(user.name)
}
```

**2. Use @PreviewParameter for dynamic preview data**

```kotlin
class UserNameProvider : PreviewParameterProvider<String> {
    override val values = sequenceOf("Alice", "Bob", "Charlie")
}

@Preview
@Composable
fun UserCardPreview(@PreviewParameter(UserNameProvider::class) name: String) {
    UserCard(user = User(name = name, age = 30))
}
```

**3. Use wrapper composable for preview-only context**

```kotlin
@Preview(showBackground = true, backgroundColor = 0xFFFFFFFF)
@Composable
fun ScreenPreview() {
    MaterialTheme {
        MyScreen(
            viewModel = PreviewViewModel()
        )
    }
}
```

**4. Use @Preview annotation parameters**

```kotlin
@Preview(
    name = "User Card",
    showBackground = true,
    backgroundColor = 0xFFFFFFFF,
    device = Devices.PIXEL_4,
    showSystemUi = true
)
@Composable
fun UserCardPreview() {
    UserCard(user = User(name = "Alice", age = 30))
}
```

## Examples

```kotlin
// Example 1: Multi-device preview
@Preview(name = "Phone", device = Devices.PHONE)
@Preview(name = "Tablet", device = Devices.TABLET)
@Composable
fun AdaptiveLayoutPreview() {
    AdaptiveLayout()
}

// Example 2: Dark mode preview
@Preview(name = "Light", uiMode = UI_MODE_NIGHT_NO)
@Preview(name = "Dark", uiMode = UI_MODE_NIGHT_YES)
@Composable
fun ThemedPreview() {
    ThemedComponent()
}

// Example 3: Preview with state
@Preview
@Composable
fun TogglePreview() {
    var enabled by remember { mutableStateOf(true) }
    Switch(checked = enabled, onCheckedChange = { enabled = it })
}
```

## Related Errors

- [Compose recomposition](kotlin-compose-recomposition) — excessive recomposition
- [Compose modifier error](kotlin-compose-modifier-error) — modifier issues
- [Compose navigation](kotlin-compose-navigation) — navigation issues
