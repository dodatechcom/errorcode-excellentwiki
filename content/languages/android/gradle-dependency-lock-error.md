---
title: "Dependency Lock Error"
description: "Fix Gradle dependency lock and verification metadata errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Gradle build fails because dependency versions are locked or verified incorrectly

## Common Causes

- Dependency lock file not generated
- Verification metadata rejecting valid dependencies
- Version conflict between locked versions
- Lock file not committed to version control

## Fixes

- Generate lock file with ./gradlew dependencies --write-locks
- Update verification metadata after adding dependencies
- Resolve version conflicts in build.gradle
- Commit lock files to version control

## Code Example

```kotlin
# Generate dependency locks:
./gradlew dependencies --write-locks

# Lock file: gradle/dependency-locks/*

# Or use verification metadata:
./gradlew gradle-dependency-verification-metadata --write-verification-metadata sha256

# gradle/verification-metadata.xml tracks all dependency checksums
```

# Dependency locks ensure reproducible builds
# Verification metadata prevents supply-chain attacks
# Always commit lock files to version control
