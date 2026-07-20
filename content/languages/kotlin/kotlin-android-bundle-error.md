---
title: "[Solution] Kotlin Android Build Variant — Resource Merge and minSdkVersion"
description: "Fix Kotlin Android build variant errors. Learn correct build type, flavor, resource merge, and minSdkVersion configuration."
languages: ["kotlin"]
severities: ["error"]
error-types: ["compile-error"]
weight: 1027
---

## Common Causes

- Resource merge conflicts between modules (duplicate resource names)
- `minSdkVersion` lower than required by dependencies
- Build variant not matching source set directory structure
- ProGuard/R8 stripping needed classes in release builds

```kotlin
// Resource merge conflict
// Module A: res/values/strings.xml <string name="app_name">A</string>
// Module B: res/values/strings.xml <string name="app_name">B</string>
// Duplicate resource error
```

## How to Fix

**1. Resolve resource merge conflicts**

```kotlin
// build.gradle.kts
android {
    defaultConfig {
        resourcePrefix = "moduleA_"  // Unique prefix
    }
}
```

**2. Align minSdkVersion with dependencies**

```kotlin
android {
    defaultConfig {
        minSdk = 24  // Check dependency requirements
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
}
```

**3. Create proper source set directories**

```
src/
  main/          # Default
  debug/         # Debug build type
  release/       # Release build type
  freeFlavor/    # Product flavor
  paidFlavor/    # Product flavor
```

**4. Use build features correctly**

```kotlin
android {
    buildFeatures {
        compose = true
        viewBinding = true
        buildConfig = true
    }
    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.8"
    }
}
```

## Examples

```kotlin
// Example 1: Product flavors
android {
    flavorDimensions += "tier"
    productFlavors {
        create("free") {
            dimension = "tier"
            applicationIdSuffix = ".free"
            buildConfigField("Boolean", "IS_PRO", "false")
        }
        create("pro") {
            dimension = "tier"
            applicationIdSuffix = ".pro"
            buildConfigField("Boolean", "IS_PRO", "true")
        }
    }
}

// Example 2: Build type configuration
android {
    buildTypes {
        release {
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}

// Example 3: Source set dependencies
dependencies {
    "freeImplementation"("com.example:ads:1.0")
    "proImplementation"("com.example:premium:1.0")
}
```

## Related Errors

- [Gradle plugin error](kotlin-gradle-plugin-error) — plugin version
- [Compose compiler error](kotlin-compose-compiler-error) — compiler plugin
- [JVM annotation error](kotlin-jvm-annotation-error) — annotation config
