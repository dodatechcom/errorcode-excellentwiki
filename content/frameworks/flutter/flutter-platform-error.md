---
title: "PlatformException - platform channel error"
description: "Flutter throws PlatformException when a platform channel call to native code fails"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["platform-channel", "native", "android", "ios", "method-channel"]
weight: 5
---

This error occurs when a method call from Dart to native platform code via a platform channel fails. It throws `PlatformException` with details from the native side.

## Common Causes

- Native method not implemented for the given method name
- Arguments passed to native code are null or wrong type
- Native code threw an exception
- Platform channel method name typo
- Missing platform-specific native code in `MainActivity`

## How to Fix

1. Verify the method channel names match on both sides:

```dart
// Dart side
const platform = MethodChannel('com.example/app');
final result = await platform.invokeMethod('getBatteryLevel');
```

```kotlin
// Android side — method name must match exactly
class MainActivity : FlutterActivity() {
    private val CHANNEL = "com.example/app"

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL)
            .setMethodCallHandler { call, result ->
                if (call.method == "getBatteryLevel") {
                    result.success(getBatteryLevel())
                } else {
                    result.notImplemented()
                }
            }
    }
}
```

2. Handle PlatformException in Dart:

```dart
try {
  final batteryLevel = await platform.invokeMethod<int>('getBatteryLevel');
} on PlatformException catch (e) {
  print('Platform error: ${e.message}');
  // Fallback behavior
}
```

3. Check argument types across the platform boundary:

```dart
// Sending arguments
await platform.invokeMethod('getUser', {'id': 42, 'name': 'Alice'});
```

## Examples

```dart
await platform.invokeMethod('getUnknownMethod');
// PlatformException: getUnknownMethod was not implemented
```

## Related Errors

- [Network error]({{< relref "/frameworks/flutter/network-error6" >}})
- [Widget error]({{< relref "/frameworks/flutter/widget-error" >}})
