---
title: "Semantics Modifier Error"
description: "Fix Compose semantics modifier for accessibility properties and actions"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Accessibility properties not being read by screen readers or semantics not configured correctly

## Common Causes

- Content description not read by TalkBack
- Custom actions not accessible
- Semantics properties conflicting between composables
- Screen reader navigation not working

## Fixes

- Use semantics modifier with contentDescription
- Use role to define element type
- Use onClick for clickable actions
- Test with TalkBack enabled

## Code Example

```kotlin
Modifier.semantics {
    contentDescription = "Close button"
    role = Role.Button
    onClick(label = "Close", action = { closeDialog(); true })
}
```

# semantics: accessibility properties# contentDescription: screen reader text# role: element type# onClick: accessible click action
