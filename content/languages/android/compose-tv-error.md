---
title: "Android TV Compose Error"
description: "Fix Android TV Compose and Leanback integration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Android TV Compose app does not handle focus or D-pad navigation correctly

## Common Causes

- Focus not moving between TV elements
- D-pad navigation not working in LazyColumn
- Card focus state not visible
- TV-specific dependencies not added

## Fixes

- Use Modifier.focusable() for TV elements
- Configure LazyColumn for D-pad navigation
- Show focus state with border or elevation
- Add tv-compose dependencies

## Code Example

```kotlin
dependencies {
    implementation "androidx.tv:tv-foundation:1.0.0-alpha10"
    implementation "androidx.tv:tv-material:1.0.0-alpha10"
}

// TV card with focus:
Card(
    onClick = { onClick() },
    modifier = Modifier
        .fillMaxWidth()
        .focusable()
) {
    Column {
        Image(painter, null)
        Text("Title")
    }
}
```

# tv-foundation: TV-specific Compose components
# tv-material: TV Material Design
# focusable: make element focusable
# onDpadEvent: handle D-pad input
