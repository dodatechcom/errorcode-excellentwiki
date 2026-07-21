---
title: "Modifier Node Error"
description: "Fix Compose Modifier.Node for custom modifier creation and composition"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Custom Modifier.Node not correctly composed or causing performance issues

## Common Causes

- Modifier.Node not registering in composition
- Custom modifier causing recomposition on every frame
- Node lifecycle not managed correctly
- Modifier.Node not accessible from composables

## Fixes

- Extend Modifier.Node for custom modifiers
- Use Modifier.Node factory for composition
- Manage node lifecycle with compositionLocalOf
- Test node registration and unregistration

## Code Example

```kotlin
class CustomNode : Modifier.Node() {
    override fun onAttach() { /* Attached */ }
    override fun onDetach() { /* Detached */ }
}

fun Modifier.customModifier(): Modifier = this.then(CustomModifier())

@Composable
fun MyComposable() {
    Box(modifier = Modifier.customModifier()) {
        // Content
    }
}
```

# Modifier.Node: custom modifier base class# onAttach/onDetach: lifecycle# Factory function for composition# Test registration and lifecycle
