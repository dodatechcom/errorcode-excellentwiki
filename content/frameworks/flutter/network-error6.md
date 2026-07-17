---
title: "SocketException"
description: "Dart throws a SocketException when a network connection cannot be established"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when Dart's HTTP client cannot establish a network connection to the target host, typically due to connectivity issues or host unavailability.

## Common Causes

- Device has no internet connection
- Server hostname or IP is unreachable
- Firewall or proxy blocking the connection
- `http` package not configured for the platform

## How to Fix

1. Handle network errors gracefully:

```dart
import 'dart:io';

Future<Map<String, dynamic>?> fetchData() async {
  try {
    final response = await http.get(Uri.parse('https://api.example.com/data'));
    if (response.statusCode == 200) {
      return json.decode(response.body);
    }
    return null;
  } on SocketException {
    print('No internet connection');
    return null;
  }
}
```

2. Add internet permission for Android:

```xml
<!-- android/app/src/main/AndroidManifest.xml -->
<uses-permission android:name="android.permission.INTERNET" />
```

3. Check connectivity before making requests:

```dart
import 'package:connectivity_plus/connectivity_plus.dart';

Future<void> makeRequest() async {
  final connectivity = await Connectivity().checkConnectivity();
  if (connectivity == ConnectivityResult.none) {
    print('No network connection');
    return;
  }
  // Proceed with request
}
```

4. Set appropriate timeouts:

```dart
final client = http.Client();
try {
  final response = await client.get(
    Uri.parse('https://api.example.com/data'),
  ).timeout(Duration(seconds: 10));
} on SocketException {
  print('Connection failed');
} on TimeoutException {
  print('Request timed out');
}
```

## Examples

```dart
// Server is down or unreachable
final response = await http.get(Uri.parse('https://192.168.1.999:8080/data'));
// SocketException: Connection refused (OS Error: Connection refused, errno = 111)
```

```text
SocketException: SocketException: OS Error: Connection refused, errno = 111,
address = 192.168.1.999, port = 8080
```

## Related Errors

- [Platform channel error]({{< relref "/frameworks/flutter/platform-error" >}})
