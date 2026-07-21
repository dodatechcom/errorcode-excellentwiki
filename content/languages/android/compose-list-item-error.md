---
title: "ListItem Configuration Error"
description: "Fix Material 3 ListItem configuration and content slot errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ListItem does not display headline, supporting text, or trailing content correctly

## Common Causes

- ListItem content slots not properly configured
- Text overflowing in ListItem
- Leading or trailing content not showing
- ListItem not clickable when wrapped

## Fixes

- Use headlineContent, supportingContent, leadingContent
- Set singleLine or maxLines on text
- Use leadingContent and trailingContent slots
- Use Modifier.clickable on ListItem

## Code Example

```kotlin
ListItem(
    headlineContent = { Text("Title") },
    supportingContent = { Text("Description text goes here") },
    leadingContent = {
        Icon(Icons.Default.Person, null)
    },
    trailingContent = {
        Icon(Icons.Default.ChevronRight, null)
    },
    modifier = Modifier.clickable { onClick() }
)
```

# headlineContent: primary text
# supportingContent: secondary text
# leadingContent: icon or image before text
# trailingContent: icon or action after text
