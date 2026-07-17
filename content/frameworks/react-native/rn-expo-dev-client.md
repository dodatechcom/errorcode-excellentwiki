---
title: "Expo dev client - update error"
description: "Expo development client fails to load updates or connect to the development server"
frameworks: ["react-native"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The Expo dev client update error occurs when the development build cannot fetch or apply JavaScript updates from the Metro bundler. This typically happens when the dev client URL is incorrect, the bundler is not running, or there is a version mismatch.

## Common Causes

- Metro bundler not running or not accessible from the device
- Dev client URL configuration is stale after network change
- Expo SDK version mismatch between dev client and project
- Deep link URL format is incorrect
- Firewall blocking connection between device and dev machine

## How to Fix

1. Start the dev server and scan the QR code:

```bash
npx expo start --dev-client
```

2. Clear the dev client cache:

```bash
npx expo start --dev-client --clear
```

3. Manually set the dev server URL:

```bash
# Find your local IP
ipconfig getifaddr en0  # macOS
hostname -I             # Linux

# Use explicit URL
npx expo start --host lan --port 8081
```

4. Update the dev client build:

```bash
eas build --profile development --platform ios
```

5. Check for SDK version mismatch:

```bash
npx expo install --check
```

6. Reinstall the dev client on the device:

```bash
eas build --profile development --platform ios --clean
```

## Examples

```bash
$ npx expo start --dev-client
Starting Metro Bundler
warn Your app is running on an outdated expo-dev-client.
Update to the latest version for best compatibility.
```

```bash
# Device shows "Unable to load script"
# Fix: ensure Metro is running and device can reach dev machine
npx expo start --host lan
```

## Related Errors

- [Expo error]({{< relref "/frameworks/react-native/rn-expo-error" >}})
- [Expo build error]({{< relref "/frameworks/react-native/rn-expo-build-error" >}})
