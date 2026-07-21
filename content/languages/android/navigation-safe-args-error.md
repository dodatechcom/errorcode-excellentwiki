---
title: "Safe Args Error"
description: "Fix Navigation Safe Args Gradle plugin errors and generated code issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Navigation Safe Args does not generate correct argument classes or directions

## Common Causes

- Safe Args plugin not applied in module build.gradle
- Argument type not supported by Safe Args
- Directions class not generated for action
- Args class not found for destination

## Fixes

- Apply Safe Args plugin in module build.gradle
- Use supported types: String, Int, Long, Boolean, etc.
- Define actions in navigation XML
- Ensure nav graph has proper IDs

## Code Example

```kotlin
// build.gradle
plugins {
    id 'androidx.navigation.safeargs.kotlin'
}

// Usage:
val action = HomeFragmentDirections.actionHomeToDetail(itemId)
findNavController().navigate(action)

// Receive args:
val args = DetailFragmentArgs.fromBundle(requireArguments())
val itemId = args.itemId
```

# Safe Args generates:
# - XyzDirections for each fragment with actions
# - XyzArgs for each fragment with arguments
# - Type-safe navigation
