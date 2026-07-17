---
title: "Hermes - bytecode compilation error"
description: "React Native Hermes engine fails to compile JavaScript into Hermes bytecode during build"
frameworks: ["react-native"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

The Hermes bytecode compilation error occurs when the Hermes engine cannot compile your JavaScript bundle into its bytecode format. This typically happens during the Android build when Hermes is enabled but encounters unsupported syntax or configuration issues.

## Common Causes

- JavaScript code using syntax not supported by Hermes
- Hermes version mismatch with React Native version
- Corrupted Hermes cache from previous builds
- Memory limitations during bytecode generation
- Incorrect Hermes configuration in `gradle.properties`

## How to Fix

1. Verify Hermes is enabled in `android/gradle.properties`:

```properties
hermesEnabled=true
```

2. Update Hermes with React Native:

```bash
npm install react-native@latest
cd android && ./gradlew clean
```

3. Clear the Hermes cache:

```bash
rm -rf android/app/build/generated/hermes*
rm -rf /tmp/hermes-*
cd android && ./gradlew clean
```

4. Check for unsupported syntax in your bundle:

```bash
npx hermes-engine --version
npx react-native bundle --platform android --dev false --entry-file index.js --bundle-output /tmp/index.android.bundle
```

5. If Hermes compilation fails, temporarily disable to test:

```properties
# android/gradle.properties
hermesEnabled=false
```

## Examples

```bash
# Build output
> Task :app:bundleReleaseJsAndAssets FAILED
FAILURE: Build failed with an exception.
* What went wrong:
Execution failed for task ':app:bundleReleaseJsAndAssets'.
> Process 'command 'node'' finished with non-zero exit value 1
stderr: Error: Hermes bytecode compilation failed
```

## Related Errors

- [Build error]({{< relref "/frameworks/react-native/rn-build-error-v2" >}})
- [New Architecture error]({{< relref "/frameworks/react-native/rn-new-architecture-error" >}})
