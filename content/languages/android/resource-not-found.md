---
title: "Resource Not Found"
description: "Fix resource not found errors in Android projects when referencing R class"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build fails because a referenced resource ID does not exist in R.java

## Common Causes

- Resource name misspelled in layout or code
- Resource file missing from correct res directory
- Resource in library module not imported
- Clean build needed after resource changes

## Fixes

- Check resource name spelling against actual file names
- Verify resource is in correct res/ subdirectory
- Use library package R import for library resources
- Perform clean build to regenerate R class

## Code Example

```kotlin
// Wrong:
setContentView(R.layout.main_activty)  // typo
// Correct:
setContentView(R.layout.activity_main)

// In Kotlin with View Binding:
binding = ActivityMainBinding.inflate(layoutInflater)
```

# List all resources
find app/src/main/res -type f | sort
# Verify resource name matches file name exactly
