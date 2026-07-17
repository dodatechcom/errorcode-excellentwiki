---
title: "Native module - linking failed"
description: "React Native fails to link a native module during build, causing module not found errors at runtime"
frameworks: ["react-native"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

The native module linking error occurs when React Native cannot properly connect JavaScript modules to their native implementations. Since React Native 0.60+, autolinking handles most cases, but manual linking or misconfiguration can still cause failures.

## Common Causes

- Native module requires manual linking but autolink was not configured
- `react-native link` was not run after adding a module
- Pod install not run after adding iOS native module
- Android `settings.gradle` missing module reference
- Module not listed in `react-native.config.js`

## How to Fix

1. Run autolink manually:

```bash
npx react-native autolink
```

2. For iOS, reinstall pods after adding native modules:

```bash
cd ios && pod install && cd ..
```

3. Check autolink status:

```bash
npx react-native config
```

4. Manually link in `android/settings.gradle`:

```gradle
include ':react-native-module-name'
project(':react-native-module-name').projectDir = new File(rootProject.projectDir, '../node_modules/react-native-module-name/android')
```

5. Add to `android/app/build.gradle` dependencies:

```gradle
dependencies {
  implementation project(':react-native-module-name')
}
```

6. Register the module in your `MainApplication.java`:

```java
@Override
protected List<ReactPackage> getPackages() {
  List<ReactPackage> packages = new PackageList(this).getPackages();
  packages.add(new MyNativeModulePackage());
  return packages;
}
```

## Examples

```bash
$ npx react-native run-android
error: NativeModule'ModuleName' not found.
Make sure you have rebuilt the native code.
```

## Related Errors

- [iOS CocoaPods error]({{< relref "/frameworks/react-native/rn-ios-cocoapods-error" >}})
- [Bridge error]({{< relref "/frameworks/react-native/rn-bridge-error" >}})
