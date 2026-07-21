---
title: "Text Trim Error"
description: "Fix Compose trim modifier for text overflow and ellipsis handling"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Text not trimming correctly or ellipsis not appearing when content overflows

## Common Causes

- Text overflowing container bounds
- Ellipsis not appearing on overflow
- Max lines not being respected
- Text not truncating correctly

## Fixes

- Use maxLines parameter for text
- Use overflow parameter for ellipsis
- Use softWrap for text wrapping
- Test with varying text lengths

## Code Example

```kotlin
Text(
    text = "Long text content",
    maxLines = 1,
    overflow = TextOverflow.Ellipsis
)

// Multiple lines:
Text(
    text = "Long text content",
    maxLines = 3,
    overflow = TextOverflow.Ellipsis,
    softWrap = true
)
```

# maxLines: maximum lines# overflow: ellipsis behavior# softWrap: text wrapping# Test with varying lengths
