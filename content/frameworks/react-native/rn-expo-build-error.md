---
title: "Expo - EAS build error"
description: "Expo Application Services build fails due to configuration errors, dependency issues, or platform-specific problems"
frameworks: ["react-native"]
error-types: ["build-error"]
severities: ["error"]
tags: ["expo", "eas", "build", "cloud", "android", "ios", "eas-build"]
weight: 5
---

An EAS build error occurs when Expo Application Services fails to build your app in the cloud. This can happen during the Android or iOS build phase due to configuration issues, dependency problems, or platform-specific errors.

## Common Causes

- Missing or invalid `eas.json` configuration
- Build profile does not match project requirements
- Native dependencies incompatible with EAS build environment
- Missing environment variables or secrets
- App version/build number conflicts on iOS

## How to Fix

1. Verify `eas.json` configuration:

```json
{
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal"
    },
    "production": {}
  }
}
```

2. Check build logs for specific errors:

```bash
eas build:list
eas build:view <build-id>
```

3. Ensure all dependencies are EAS-compatible:

```bash
npx expo install --check
```

4. Set up environment variables if needed:

```json
{
  "build": {
    "production": {
      "env": {
        "API_URL": "https://api.production.com"
      }
    }
  }
}
```

5. For iOS, ensure proper credentials:

```bash
eas credentials
```

6. Run a local build to debug:

```bash
eas build --platform android --profile development --local
```

## Examples

```bash
$ eas build --platform ios
Build error: EAS Build encountered an error.
Error: xcodebuild: error: 'YourApp.xcodeproj' does not exist.
Run 'expo prebuild' to generate native projects.
```

```bash
# Fix: prebuild first
npx expo prebuild --platform ios
eas build --platform ios
```

## Related Errors

- [Expo error]({{< relref "/frameworks/react-native/rn-expo-error" >}})
- [Expo dev client error]({{< relref "/frameworks/react-native/rn-expo-dev-client" >}})
