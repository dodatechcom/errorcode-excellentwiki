---
title: "Compose Compiler Metrics Error"
description: "Fix Compose Compiler metrics and stability report generation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose Compiler does not generate stability reports or reports show unexpected instability

## Common Causes

- Stability configuration file not properly set
- Data class not marked as stable in report
- Enum or sealed class showing as unstable
- Compiler metrics not being generated

## Fixes

- Add @Stable or @Immutable annotations
- Configure stability config file in build.gradle
- Check which types are unstable in compiler report
- Fix unstable types or suppress warnings

## Code Example

```kotlin
// build.gradle
android {
    kotlinOptions {
        freeCompilerArgs += listOf(
            "-P",
            "plugin:androidx.compose.compiler.plugins.kotlin:stabilityConfigurationFile=" +
            project.rootDir.path + "/compose-stability-config.conf"
        )
    }
}

// compose-stability-config.conf
// Mark types as stable:
kotlin.collections.List
kotlin.collections.Map
com.example.model.User
```

# @Stable: type will not change unpredictably
# @Immutable: type never changes after creation
# Compiler metrics show stability status
# Fix unstable types for better performance
