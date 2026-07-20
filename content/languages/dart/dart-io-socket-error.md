---
title: "[Solution] Dart IO Socket Error — connect, timeout, ServerSocket, address in use"
description: "Fix Dart Socket errors from connect failures, timeouts, ServerSocket bind issues, and address-in-use errors."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 133
---

Socket errors occur when connections fail, addresses are already in use, or timeouts are not properly configured.

## Common Causes

1. Connection refused when the server is not running.
2. `SocketException: Address already in use` when binding to a busy port.
3. Connection timeout not being set for unreachable hosts.
4. `ServerSocket` not being closed, causing port exhaustion.
5. DNS resolution failures for hostnames.

## How to Fix It

**Solution 1: Handle socket connection errors**

```dart
import 'dart:io';

void main() async {
  try {
    Socket socket = await Socket.connect('127.0.0.1', 8080,
      timeout: Duration(seconds: 5),
    );
    
    socket.listen(
      (data) => print('Received: ${String.fromCharCodes(data)}'),
      onError: (error) => print('Error: $error'),
      onDone: () => print('Connection closed'),
    );
    
    socket.write('Hello Server');
  } on SocketException catch (e) {
    print('Socket error: ${e.message}');
  } on TimeoutException {
    print('Connection timed out');
  }
}
```

**Solution 2: Avoid address-in-use errors**

```dart
import 'dart:io';

void main() async {
  ServerSocket? server;
  
  try {
    server = await ServerSocket.bind('127.0.0.1', 0); // Port 0 = auto-assign
    print('Listening on port ${server.port}');
    
    await for (Socket socket in server) {
      print('Client connected');
      socket.close();
    }
  } on SocketException catch (e) {
    print('Bind failed: ${e.message}');
  } finally {
    await server?.close();
  }
}
```

**Solution 3: Set connection timeout**

```dart
import 'dart:io';

void main() async {
  try {
    Socket socket = await Socket.connect(
      '192.168.1.100',
      3000,
      timeout: Duration(seconds: 3),
    );
    
    socket.done.then((_) => print('Socket closed'));
  } on TimeoutException {
    print('Connection timed out — server may be unreachable');
  } on SocketException catch (e) {
    print('Connection failed: ${e.message}');
  }
}
```

**Solution 4: Close ServerSocket properly**

```dart
import 'dart:io';

Future<void> startServer() async {
  ServerSocket server = await ServerSocket.bind('127.0.0.1', 8080);
  
  print('Server started on port ${server.port}');
  
  server.listen(
    (Socket socket) {
      print('Client connected');
      socket.listen(
        (data) => socket.add(data), // Echo back
      );
    },
    onError: (error) => print('Server error: $error'),
  );
  
  // Close after a timeout for demo
  await Future.delayed(Duration(seconds: 10));
  await server.close();
  print('Server closed');
}
```

**Solution 5: Handle DNS resolution**

```dart
import 'dart:io';

void main() async {
  try {
    List<InternetAddress> addresses = await InternetAddress.lookup('example.com');
    
    for (InternetAddress addr in addresses) {
      print('${addr.host} -> ${addr.address}');
    }
  } on SocketException catch (e) {
    print('DNS lookup failed: ${e.message}');
  }
}
```

## Examples

Port 0 lets the OS assign an available port, which is useful for tests. Always close sockets and servers in `finally` blocks to prevent resource leaks.

## Related Errors

- [Dart HTTP Server Error](/languages/dart/dart-http-server-error/)
- [Dart HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Dart WebSocket Error](/languages/dart/dart-web-socket-error/)
