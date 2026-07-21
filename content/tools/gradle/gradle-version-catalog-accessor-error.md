---
title: "Version Catalog Accessor Error"
description: "Gradle version catalog type-safe accessors fail to resolve, preventing use of catalog references in build scripts."
tools: ["gradle"]
error-types: ["tool-error"]
severities: ["error"]
---

# Version Catalog Accessor Error

Gradle version catalogs provide type-safe accessors for declaring dependencies. An accessor error occurs when the catalog entry cannot be found or the generated accessor code fails to compile.

## Common Causes

- The version catalog TOML file contains syntax errors
- A dependency alias in `build.gradle.kts` does not match the catalog entry
- The `libs.` accessor references a group or artifact that is not defined
- A version catalog entry is defined in a subproject but not the root project

## How to Fix

1. Verify the version catalog TOML file is valid:

```toml
# gradle/libs.versions.toml
[versions]
kotlin = "1.9.22"
spring-boot = "3.2.2"

[libraries]
kotlin-stdlib = { module = "org.jetbrains.kotlin:kotlin-stdlib", version.ref = "kotlin" }
spring-boot-web = { module = "org.springframework.boot:spring-boot-starter-web", version.ref = "spring-boot" }

[plugins]
kotlin-jvm = { id = "org.jetbrains.kotlin.jvm", version.ref = "kotlin" }
```

2. Ensure the accessor name matches the TOML entry:

```kotlin
// TOML: [libraries] my-lib = { ... }
// Accessor: libs.my.lib (dots become property access)
dependencies {
    implementation(libs.my.lib)
}
```

3. Regenerate the catalog accessors:

```bash
./gradlew --stop
rm -rf .gradle/
./gradlew dependencies --configuration compileClasspath
```

4. Check for typos in the catalog entry names:

```bash
grep -n "my-lib" gradle/libs.versions.toml
```

## Examples

```kotlin
// Error -- unresolved reference
dependencies {
    implementation(libs.my.nonexistent) // does not exist in TOML
}

// Fixed -- matches TOML entry
dependencies {
    implementation(libs.spring.boot.web) // spring-boot-web in TOML
}
```

```toml
# Version catalog with aliases
[versions]
junit = "5.10.1"

[libraries]
junit-jupiter = { group = "org.junit.jupiter", name = "junit-jupiter", version.ref = "junit" }

[bundles]
testing = ["junit-jupiter"]
```

## Related Errors

- [Version Catalog Not Found]({{< relref "/tools/gradle/gradle-version-catalog-not-found" >}}) -- missing catalog file
- [TOML File Syntax]({{< relref "/tools/gradle/gradle-toml-file-syntax" >}}) -- TOML parsing errors
