---
title: "SocketException: Connection refused"
description: "Flutter throws a SocketException when a network connection is refused by the target server"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

This error occurs when a Dart `HttpClient` or `http` package attempt to connect to a server that is not listening on the specified port, or the connection is refused by the server.

## Common Causes

- Backend server is not running on the specified host/port
- Firewall blocking the connection
- Incorrect API base URL in configuration
- Using `localhost` on a physical device (should use machine IP)
- SSL certificate verification failure

## How to Fix

1. Verify the API base URL:

```dart
// For Android emulator, use 10.0.2.2 instead of localhost
const baseUrl = 'http://10.0.2.2:3000';

// For iOS simulator, use localhost
const baseUrl = 'http://localhost:3000';

// For physical device, use machine IP
const baseUrl = 'http://192.168.1.100:3000';
```

2. Add network security config for Android:

```xml
<!-- android/app/src/main/res/xml/network_security_config.xml -->
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">10.0.2.2</domain>
        <domain includeSubdomains="true">localhost</domain>
    </domain-config>
</network-security-config>
```

3. Handle network errors gracefully:

```dart
import 'dart:io';

try {
  final response = await http.get(Uri.parse('$baseUrl/api/data'));
  // Process response
} on SocketException catch (e) {
  print('Connection refused: ${e.message}');
  // Show user-friendly error
} on HttpException catch (e) {
  print('HTTP error: ${e.message}');
}
```

## Examples

```dart
// Trying to connect to localhost on a physical device
final response = await http.get(Uri.parse('http://localhost:3000/api'));
// SocketException: OS Error: Connection refused, errno = 111
```

## Related Errors

- [Network error (RN)]({{< relref "/frameworks/react-native/network-error5" >}})
- [Platform error]({{< relref "/frameworks/flutter/platform-error" >}})
