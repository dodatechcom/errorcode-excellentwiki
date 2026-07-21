---
title: "Gradle Lint Error"
description: "Fix Android Lint errors and warnings in Gradle build output"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Android Lint reports errors or warnings that fail the build

## Common Causes

- Lint configured to fail build on errors
- MissingRequiredPermission lint error
- UnusedResources lint warning
- HardcodedText warning in layouts

## Fixes

- Fix lint errors or configure lint options
- Add @SuppressLint for false positives
- Use tools:ignore for XML lint warnings
- Configure lint baseline for existing warnings

## Code Example

```kotlin
android {
    lint {
        abortOnError false  // Don't fail build
        baseline = file("lint-baseline.xml")  // Ignore existing warnings
        disable "MissingTranslation"  // Disable specific checks
    }
}

// In code:
@SuppressLint("HardcodedText")
fun setText() { ... }

// In XML:
<TextView tools:ignore="HardcodedText" ... />
```

# Run lint:
./gradlew lintDebug
# Report in app/build/reports/lint-results-debug.html
