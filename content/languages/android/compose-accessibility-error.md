---
title: "Compose Accessibility Error"
description: "Fix Jetpack Compose accessibility and screen reader compatibility errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose components not accessible to screen readers or accessibility services

## Common Causes

- Content description missing on clickable elements
- Semantics not properly defined for custom components
- Touch target too small for accessibility
- Color contrast not meeting WCAG requirements

## Fixes

- Add contentDescription to all interactive elements
- Use Modifier.semantics {} for custom components
- Ensure minimum 48dp touch target
- Use MaterialTheme colors for proper contrast

## Code Example

```kotlin
// Add content description
Image(
    painter = painterResource(R.drawable.icon),
    contentDescription = "Settings icon",
    modifier = Modifier.clickable { openSettings() }
)

// Custom semantics:
Box(
    modifier = Modifier
        .semantics {
            contentDescription = "Progress: 75%"
            stateDescription = "Loading"
        }
) {
    CircularProgressIndicator(progress = 0.75f)
}

// Minimum touch target:
Button(
    onClick = { /* click */ },
    modifier = Modifier.minimumInteractiveComponentSize()
) {
    Text("Small Button")
}
```

# contentDescription for images and icons
# Modifier.semantics {} for custom components
# minimumInteractiveComponentSize() for touch targets
# Test with TalkBack
