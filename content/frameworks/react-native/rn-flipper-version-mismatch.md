---
title: "[Solution] React Native Flipper SDK Version Mismatch"
description: "react-native Flipper SDK embedded in app does not match the Flipper desktop client version causing connection drops or plugin load failures"
frameworks: ["react-native"]
error-types: ["framework-error"]
severities: ["error"]
---

The Flipper version mismatch error appears when the native Flipper SDK inside your app reports a different major or minor version than the Flipper desktop application. The Flipper protocol uses versioned serialization, so mismatched SDKs fail to negotiate the connection.

## Common Causes

- Different Flipper version in Podfile vs the React Native Flipper package
- Android SoLoader Flipper version overridden by a transitive dependency
- Flipper desktop client auto-update changed its version independently
- Using Expo managed workflow with custom dev client Flipper version
- Multiple React Native modules pulling conflicting Flipper transitive versions

## How to Fix

1. Pin the exact Flipper version in ios/Podfile:

```ruby
use_flipper!({ 'Flipper' => '0.201.0', 'Flipper-DoubleConversion' => '3.2.0' })
```

2. For Android, check root build.gradle:

```gradle
ext {
  flipperVersion = '0.201.0'
}
```

3. Remove the conflict by cleaning:

```bash
rm -rf node_modules ios/Pods
rm -rf ~/.gradle/caches/
npm install
cd ios && pod install && cd ..
```

## Examples

```bash
# Flipper desktop log:
# Connection to app lost: protocol version mismatch (app: 15, client: 14)

# Fix: upgrade both to the same version
npx react-native-flipper-upgrade
```

## Related Errors

- [Flipper Error]({{< relref "/frameworks/react-native/rn-flipper-error" >}})
