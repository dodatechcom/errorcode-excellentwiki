---
title: "Padding Modifier Error"
description: "Fix Compose padding modifier for adding space around composable content"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Padding not applying correctly or causing unexpected layout behavior

## Common Causes

- Padding not appearing around content
- Padding overlapping with background
- Padding size not matching expected value
- Padding causing content to overflow parent

## Fixes

- Use padding modifier with dp values
- Use padding for directional padding
- Test padding with different content sizes
- Ensure padding does not cause overflow

## Code Example

```kotlin
Modifier.padding(16.dp)  // All sides
Modifier.padding(horizontal = 16.dp, vertical = 8.dp)
Modifier.padding(start = 16.dp, top = 8.dp, end = 16.dp, bottom = 8.dp)

// With padding values:
Modifier.padding(PaddingValues(16.dp))
Modifier.padding(PaddingValues(horizontal = 16.dp, vertical = 8.dp))
```

# padding(): all sides# padding(horizontal, vertical): directional# padding(start, top, end, bottom): individual# PaddingValues: reusable padding
