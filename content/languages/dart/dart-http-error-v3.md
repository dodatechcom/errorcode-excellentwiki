---
title: "[Solution] Dart SocketException Connection Refused - Network Fix"
description: "Fix Dart SocketException connection refused in HTTP requests. Learn why connections fail, how to handle network errors, and retry strategies for Dart apps."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

A `SocketException: Connection refused` error occurs when the Dart HTTP client attempts to open a TCP connection to a server, but the server actively rejects the connection. The operating system returns an ECONNREFUSED signal, which Dart wraps in a `SocketException`.

## Why It Happens

The target server is not listening on the specified port. This happens when the server process is not running, the port number is wrong, the server is listening on a different network interface (localhost only), or a firewall is blocking the connection.

In mobile development, this error is common when the app tries to connect to a local development server. On Android, `localhost` refers to the device itself, not the development machine. You must use the machine's actual IP address or `10.0.2.2` for the Android emulator.

The error also appears when connecting to HTTPS endpoints that redirect to a different port, when DNS resolution succeeds but the server is unreachable, or when the server closes the connection immediately after accepting it due to misconfiguration.

## How to Fix It

Verify the server is running and listening on the expected port:

```bash
# Check if the port is in use
lsof -i :8080

# Test the connection manually
curl http://localhost:8080/health
```

For Android emulator, use the correct host address:

```dart
// Wrong - localhost refers to the device
final url = 'http://localhost:8080/api';

// Correct - 10.0.2.2 maps to host machine on Android emulator
final url = 'http://10.0.2.2:8080/api';

// For iOS simulator, localhost works
final url = 'http://localhost:8080/api';
```

Implement retry logic with exponential backoff:

```dart
import 'dart:io';
import 'dart:math';

Future<T> retryWithBackoff<T>(
  Future<T> Function() action, {
  int maxRetries = 3,
}) async {
  for (var attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await action();
    } on SocketException catch (e) {
      if (attempt == maxRetries) rethrow;
      final delay = Duration(seconds: pow(2, attempt).toInt());
      await Future.delayed(delay);
    }
  }
  throw StateError('Unreachable');
}
```

Handle the error gracefully in your UI:

```dart
try {
  final response = await http.get(Uri.parse(url));
  // Process response
} on SocketException catch (e) {
  print('Network error: ${e.message}');
  // Show offline message to user
}
```

Check firewall rules and ensure the server binds to `0.0.0.0` if accepting external connections.

## Common Mistakes

- Using `localhost` on Android emulator instead of `10.0.2.2`
- Not implementing retry logic for transient connection failures
- Forgetting to handle the SocketException in try-catch blocks
- Hardcoding the server address without environment-based configuration
- Assuming the server is always available without checking network connectivity first
- Not setting appropriate timeouts on HTTP requests

## Related Pages

- [Dart HTTP Error](/languages/dart/dart-http-error/)
- [Dart JSON Error](/languages/dart/dart-json-error-v2/)
- [Dart IO Error](/languages/dart/dart-io-error/)
- [Dart Null Check Error](/languages/dart/dart-null-check-error-v2/)
- [Dart Async Error](/languages/dart/dart-async-error-v2/)
