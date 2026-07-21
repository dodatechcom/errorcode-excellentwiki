---
title: "Compose Desktop Error"
description: "Fix Compose Multiplatform Desktop application errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Compose Desktop application does not build or render correctly

## Common Causes

- Desktop Compose dependencies not configured
- Window not showing or rendering blank
- Desktop-specific modifiers not working
- Kotlin Multiplatform plugin not applied

## Fixes

- Add Compose Desktop dependencies
- Configure desktop application entry point
- Use desktop-specific Window and JFrame
- Apply Kotlin Multiplatform plugin

## Code Example

```kotlin
// build.gradle.kts
kotlin {
    jvm("desktop") {
        compilations.all {
            kotlinOptions.jvmTarget = "17"
        }
    }
}

dependencies {
    implementation(compose.desktop.currentOs)
    implementation(compose.material3)
}

// Desktop main:
fun main() = application {
    Window(
        onCloseRequest = ::exitApplication,
        title = "My App"
    ) {
        App()
    }
}
```

# Compose Desktop for JVM/桌面 apps
# Use Window composable for application window
# Desktop-specific modifiers for mouse input
# Package with jpackage or proguard
