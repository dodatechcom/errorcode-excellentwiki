---
title: "LazyColumn Accessibility Actions Error"
description: "Fix LazyColumn accessibility actions for scrolling, selection, and navigation"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
LazyColumn accessibility actions not working for scroll and navigation

## Common Causes

- Scroll actions not triggering with accessibility
- Select action not working on items
- Custom actions not accessible
- Navigation between items not working

## Fixes

- Define custom actions with Modifier.semantics
- Use Role and stateDescription for items
- Test with TalkBack enabled
- Provide semantic properties for list interaction

## Code Example

```kotlin
LazyColumn {
    items(items, key = { it.id }) { item ->
        ListItem(
            modifier = Modifier.semantics {
                role = Role.Button
                onClick(label = "Open", action = { openItem(item); true })
                stateDescription = "Position ${item.position}"
            }
        )
    }
}
```

# semantics: define custom actions# role: item type for navigation# stateDescription: current state# Test with TalkBack
