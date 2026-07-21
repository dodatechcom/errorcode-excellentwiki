---
title: "CI Build Error"
description: "Fix Android CI/CD build configuration errors for GitHub Actions or Jenkins"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Android CI build fails because of missing tools, SDK, or signing configuration

## Common Causes

- Android SDK not properly set up in CI
- Signing keystore not available in CI environment
- Build tools version not installed
- Gradle wrapper not downloaded

## Fixes

- Use Android SDK GitHub Action for setup
- Store keystore as CI secret
- Specify build tools version explicitly
- Commit Gradle wrapper to repository

## Code Example

```kotlin
# GitHub Actions example:
- uses: android-actions/setup-android@v3
- name: Build
  run: ./gradlew assembleRelease

# Store signing config as secrets:
env:
  KEYSTORE_BASE64: ${{ secrets.KEYSTORE_BASE64 }}
  KEYSTORE_PASSWORD: ${{ secrets.KEYSTORE_PASSWORD }}
  KEY_ALIAS: ${{ secrets.KEY_ALIAS }}
  KEY_PASSWORD: ${{ secrets.KEY_PASSWORD }}

# Decode keystore:
- run: echo $KEYSTORE_BASE64 | base64 --decode > app/keystore.jks
```

# Android CI tools:
# android-actions/setup-android
# Store secrets in CI environment
# Use Gradle caching in CI
