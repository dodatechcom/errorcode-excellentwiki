---
title: "Modifier Order Error"
description: "Fix Compose modifier ordering errors that break layout and click handling"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose layout looks wrong or click handling fails due to incorrect modifier order

## Common Causes

- padding before background renders incorrectly
- clickable after size prevents tap detection
- clip before padding does not show border
- fillMaxWidth before padding causes sizing issues

## Fixes

- Apply modifiers in logical order: size, padding, background, clickable
- Use Modifier.padding().background() not reversed
- Put clickable before or after size based on desired behavior
- Test modifier order visually

## Code Example

```kotlin
// WRONG order:
Modifier
    .background(RoundedCornerShape(8.dp))
    .padding(16.dp)  // Padding is OUTSIDE background

// CORRECT order:
Modifier
    .padding(16.dp)
    .background(RoundedCornerShape(8.dp))  // Background INSIDE padding
    .clickable { /* works */ }
```

# Common modifier order:
# 1. padding()
# 2. background() / clip()
# 3. size() / fillMaxWidth()
# 4. clickable()
# 5. alpha() / offset()
