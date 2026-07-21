---
title: "Intrinsic Measurement Error"
description: "Fix Compose intrinsic measurement for composables with dynamic content sizes"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Composable using intrinsic dimensions not sizing correctly based on content

## Common Causes

- maxIntrinsicWidth returning incorrect value
- minIntrinsicHeight not matching expected size
- Content overflowing intrinsic bounds
- Nested intrinsics causing measurement conflict

## Fixes

- Use minIntrinsicWidth/Height for minimum bounds
- Use maxIntrinsicWidth/Height for maximum bounds
- Test intrinsics with varying content sizes
- Avoid circular intrinsic dependencies

## Code Example

```kotlin
Box(
    modifier = Modifier
        .widthIn(min = 100.dp, max = 300.dp)
        .wrapContentWidth()
) {
    Text("Long text that determines intrinsic width")
}

// Custom intrinsic measurement:
Box(modifier = Modifier.width(IntrinsicSize.Max)) {
    Text("Content", modifier = Modifier.fillMaxWidth())
}
```

# minIntrinsic: minimum size content needs# maxIntrinsic: maximum size content needs# wrapContentWidth: size based on content# width(IntrinsicSize.Max): fill available
