---
title: "PlatformException - method not found"
description: "Flutter throws PlatformException when calling a native platform method that does not exist on the current platform"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["flutter", "platform", "method-channel", "android", "ios", "native"]
weight: 5
---

A PlatformException "method not found" error occurs when Flutter tries to invoke a platform channel method that is not implemented on the Android or iOS side. This is common when a method is implemented for one platform but not the other.

## Common Causes

- Method channel handler not registered on the target platform
- Method name typo between Dart and platform code
- Platform-specific code only implemented for one platform
- Native method signature changed without updating Dart side
- Missing `else` branch for unsupported platforms

## How to Fix

1. Ensure both platforms implement the method:

```kotlin
// Android: MainActivity.kt
class MainActivity: FlutterActivity() {
  override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
    super.configureFlutterEngine(flutterEngine)
    MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "com.example/app")
      .setMethodCallHandler { call, result ->
        if (call.method == "getBatteryLevel") {
          val level = getBatteryLevel()
          result.success(level)
        } else {
          result.notImplemented()
        }
      }
  }
}
```

```swift
// iOS: AppDelegate.swift
let controller: FlutterViewController = window?.rootViewController as! FlutterViewController
let channel = FlutterMethodChannel(name: "com.example/app", binaryMessenger: controller.binaryMessenger)
channel.setMethodCallHandler { (call, result) in
  if call.method == "getBatteryLevel" {
    result(UIDevice.current.batteryLevel)
  } else {
    result(FlutterMethodNotImplemented)
  }
}
```

2. Handle missing methods gracefully in Dart:

```dart
class PlatformService {
  static const _channel = MethodChannel('com.example/app');

  static Future<int?> getBatteryLevel() async {
    try {
      return await _channel.invokeMethod<int>('getBatteryLevel');
    } on MissingPluginException {
      return null; // platform not supported
    } on PlatformException catch (e) {
      print('Platform error: ${e.message}');
      return null;
    }
  }
}
```

3. Check platform before invoking:

```dart
if (Platform.isAndroid) {
  return await _channel.invokeMethod('androidSpecific');
} else if (Platform.isIOS) {
  return await _channel.invokeMethod('iosSpecific');
} else {
  throw UnsupportedError('Platform not supported');
}
```

## Examples

```dart
// Error: MissingPluginException (No implementation found for method getBattery on channel com.example/app)
final level = await MethodChannel('com.example/app').invokeMethod('getBattery');

// Fix: implement on both platforms or catch the exception
```

## Related Errors

- [Bridge error]({{< relref "/frameworks/react-native/rn-bridge-error" >}})
- [Network error]({{< relref "/frameworks/flutter/flutter-network-error-v2" >}})
