---
title: "Version Catalog Error"
description: "Fix Gradle version catalog dependency declaration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Version catalog TOML configuration causes dependency resolution failure

## Common Causes

- Alias not declared in libs.versions.toml
- Version not defined for dependency
- Group or module name incorrect in catalog
- Catalog not referenced in settings.gradle

## Fixes

- Add library alias in libs.versions.toml
- Define version in [versions] section
- Use correct group:module format
- Verify versionCatalogs block in settings.gradle

## Code Example

```kotlin
# gradle/libs.versions.toml
[versions]
kotlin = "1.9.21"
compose-bom = "2024.01.00"

[libraries]
compose-ui = { group = "androidx.compose.ui", name = "ui", version.ref = "compose-bom" }
compose-material3 = { group = "androidx.compose.material3", name = "material3" }

[plugins]
android-application = { id = "com.android.application", version = "8.2.0" }
```

# In build.gradle:
dependencies {
    implementation(libs.compose.ui)
    implementation(libs.compose.material3)
}
