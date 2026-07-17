---
title: "Platform channel error"
description: "Flutter throws a MissingPluginException when a platform channel method has no registered handler"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Flutter's platform channel cannot find a registered handler for a method call, typically because the native side (Kotlin/Java for Android, Swift/ObjC for iOS) does not implement the channel.

## Common Causes

- Native plugin not properly registered in the platform project
- Running on a real device without rebuilding after adding a plugin
- Method channel name mismatch between Dart and native code
- Native code was not compiled with the latest Dart code

## How to Fix

1. Rebuild the app after installing plugins:

```bash
flutter clean
flutter pub get
flutter run
```

2. Verify the method channel names match between Dart and native:

```dart
// Dart side
const platform = MethodChannel('com.example/myplugin');
final result = await platform.invokeMethod('getData');
```

```kotlin
// Android - MainActivity.kt
class MainActivity : FlutterActivity() {
    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "com.example/myplugin")
            .setMethodCallHandler { call, result ->
                if (call.method == "getData") {
                    result.success("data from native")
                } else {
                    result.notImplemented()
                }
            }
    }
}
```

3. Ensure plugins are registered in the app delegate (iOS):

```swift
// AppDelegate.swift
@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
    override func application(_ application: UIApplication,
        didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        GeneratedPluginRegistrant.register(with: self)
        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }
}
```

## Examples

```dart
const platform = MethodChannel('com.example/battery');
final level = await platform.invokeMethod('getBatteryLevel');
// MissingPluginException: No implementation found for method getBatteryLevel
```

```text
MissingPluginException (No implementation found for method getBatteryLevel on channel com.example/battery)
```

## Related Errors

- [SocketException]({{< relref "/frameworks/flutter/network-error6" >}})
