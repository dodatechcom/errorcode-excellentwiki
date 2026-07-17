---
title: "SocketException - connection refused"
description: "Flutter throws SocketException when attempting to connect to a server that is not accepting connections"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A SocketException "connection refused" error in Flutter occurs when the Dart HTTP client cannot establish a connection to the target server. This is typically caused by the server not running, incorrect URL, or network restrictions.

## Common Causes

- Target server is not running or not listening on the expected port
- Incorrect host or port in the API URL
- Firewall blocking the connection
- Android cleartext HTTP traffic blocked
- DNS resolution failure for the hostname

## How to Fix

1. Add error handling for network requests:

```dart
import 'dart:io';

Future<Map<String, dynamic>?> fetchData(String url) async {
  try {
    final response = await HttpClient()
      .getUrl(Uri.parse(url))
      .then((request) => request.close())
      .then((response) => response.transform(utf8.decoder).join());
    return jsonDecode(response);
  } on SocketException catch (e) {
    print('Connection refused: ${e.message}');
    return null;
  }
}
```

2. Enable cleartext traffic on Android in `android/app/src/main/AndroidManifest.xml`:

```xml
<application
  android:usesCleartextTraffic="true"
  android:networkSecurityConfig="@xml/network_security_config"
  ... >
```

3. Create network security config for Android:

```xml
<!-- android/app/src/main/res/xml/network_security_config.xml -->
<network-security-config>
  <domain-config cleartextTrafficPermitted="true">
    <domain includeSubdomains="true">10.0.2.2</domain>
    <domain includeSubdomains="true">localhost</domain>
  </domain-config>
</network-security-config>
```

4. Use proper error handling with Dio:

```dart
import 'package:dio/dio.dart';

final dio = Dio();
try {
  final response = await dio.get('https://api.example.com/data');
} on DioException catch (e) {
  if (e.type == DioExceptionType.connectionRefused) {
    print('Server is not running');
  }
}
```

5. Verify the server is accessible:

```bash
curl -v http://localhost:8080/health
```

## Examples

```dart
// Error: SocketException: Connection refused
final response = await http.get(Uri.parse('http://localhost:8080/api'));
// SocketException: OS Error: Connection refused, errno = 111

// Fix: use try-catch and check server
try {
  final response = await http.get(Uri.parse('http://localhost:8080/api'));
} on SocketException {
  // Server is not running
}
```

## Related Errors

- [Network error]({{< relref "/frameworks/react-native/rn-network-error" >}})
- [Platform error]({{< relref "/frameworks/flutter/flutter-platform-error-v2" >}})
