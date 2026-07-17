---
title: "[Solution] Dart SocketException Connection Refused"
description: "Fix Dart SocketException when server refuses connection. Handle network errors, DNS failures, and port issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["socket", "connection", "refused", "network", "http", "dart"]
weight: 5
---

## What This Error Means

A `SocketException: Connection refused` error occurs when the client cannot establish a TCP connection to the server. The server may not be running, the port may be wrong, or a firewall may be blocking the connection.

## Common Causes

- Server not running or crashed
- Wrong host or port number
- Firewall blocking connection
- DNS resolution failure
- Too many concurrent connections

## How to Fix

```dart
// WRONG: No connection validation
var response = await http.get(Uri.parse('http://localhost:8080/api'));
// Error: Connection refused

// CORRECT: Validate connection first
try {
  var socket = await Socket.connect('localhost', 8080)
      .timeout(Duration(seconds: 5));
  socket.destroy();
  // Connection successful, proceed
  var response = await http.get(Uri.parse('http://localhost:8080/api'));
} on SocketException catch (e) {
  print('Cannot connect: ${e.message}');
}
```

```dart
// WRONG: Hardcoded port
var url = Uri.parse('http://localhost:8080/api');  // Wrong port

// CORRECT: Use configurable URL
var host = Platform.environment['API_HOST'] ?? 'localhost';
var port = Platform.environment['API_PORT'] ?? '8080';
var url = Uri.parse('http://$host:$port/api');
```

```dart
// WRONG: No retry logic
await fetchData();  // Fails once

// CORRECT: Exponential backoff retry
Future<T> withRetry<T>(
  Future<T> Function() fn, {
  int maxRetries = 3,
  Duration initialDelay = const Duration(seconds: 1),
}) async {
  for (int i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } on SocketException {
      if (i == maxRetries - 1) rethrow;
      await Future.delayed(initialDelay * (i + 1));
    }
  }
  throw StateError('Unreachable');
}
```

## Examples

```dart
import 'dart:io';
import 'package:http/http.dart' as http;

// Example 1: Check server availability
Future<bool> isServerAvailable(String host, int port) async {
  try {
    final socket = await Socket.connect(host, port)
        .timeout(Duration(seconds: 3));
    socket.destroy();
    return true;
  } on SocketException {
    return false;
  } on TimeoutException {
    return false;
  }
}

// Example 2: Health check before requests
Future<void> apiRequest() async {
  if (!await isServerAvailable('localhost', 8080)) {
    print('Server not available');
    return;
  }
  final response = await http.get(
    Uri.parse('http://localhost:8080/health'),
  );
}

// Example 3: Connection pooling with Dio
// import 'package:dio/dio.dart';
// final dio = Dio(BaseOptions(
//   baseUrl: 'http://localhost:8080',
//   connectTimeout: Duration(seconds: 5),
// ));
```

## Related Errors

- [dart-io-error]({{< relref "/languages/dart/dart-io-error" >}}) — connection closed
- [dart-async-error]({{< relref "/languages/dart/dart-async-error" >}}) — timeout exception
- [dart-http-error]({{< relref "/languages/dart/dart-http-error" >}}) — HTTP errors
