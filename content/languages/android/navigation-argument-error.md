---
title: "Navigation Argument Error"
description: "Fix Android Navigation component argument passing and type safety errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Navigation fails because arguments are not properly defined or received

## Common Causes

- Argument type mismatch between screens
- Missing required argument in navigation action
- NavArgs class not generated for destination
- Argument not declared in nav graph XML

## Fixes

- Define arguments in navigation XML with proper type
- Use NavArgs delegates in Fragment/Activity
- Use safe args Gradle plugin for type safety
- Declare all required arguments in action

## Code Example

```kotlin
<!-- nav_graph.xml -->
<fragment
    android:id="@+id/detailFragment"
    android:name="com.example.DetailFragment"
    android:label="Detail">
    <argument
        android:name="itemId"
        app:argType="long" />
    <argument
        android:name="title"
        app:argType="string"
        android:defaultValue="Default" />
</fragment>
```

// Kotlin with Safe Args:
val args = DetailFragmentArgs.fromBundle(requireArguments())
val itemId = args.itemId
val title = args.title

// Or navigate with args:
val action = HomeFragmentDirections.actionHomeToDetail(itemId, title)
findNavController().navigate(action)
