---
title: "[Solution] Dart WebSocket Error — connect, message, close, ping/pong"
description: "Fix Dart WebSocket errors from connection failures, message handling, close codes, and ping/pong timeouts."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 145
---

WebSocket errors occur when connections fail, messages are sent on closed sockets, or ping/pong keepalive is misconfigured.

## Common Causes

1. WebSocket URL using `http://` instead of `ws://` or `wss://`.
2. Sending messages after the socket is closed.
3. Server rejecting the WebSocket handshake (403 Forbidden).
4. Ping/pong timeouts causing disconnection.
5. Not handling the `onDone` event for server-initiated close.

## How to Fix It

**Solution 1: Connect to a WebSocket server**

```dart
import 'dart:io';

void main() async {
  try {
    WebSocket socket = await WebSocket.connect('ws://echo.websocket.org');
    
    socket.listen(
      (message) => print('Received: $message'),
      onDone: () => print('Connection closed: ${socket.closeCode}'),
      onError: (error) => print('Error: $error'),
    );
    
    socket.add('Hello WebSocket!');
  } on WebSocketException catch (e) {
    print('WebSocket error: ${e.message}');
  }
}
```

**Solution 2: Handle close codes**

```dart
import 'dart:io';

void main() async {
  WebSocket socket = await WebSocket.connect('ws://echo.websocket.org');
  
  socket.listen(
    (message) => print('Message: $message'),
    onDone: () {
      int? closeCode = socket.closeCode;
      String? closeReason = socket.closeReason;
      print('Closed: code=$closeCode reason=$closeReason');
    },
  );
  
  // Close gracefully
  await socket.close(1000, 'Normal closure');
}
```

**Solution 3: Send different message types**

```dart
import 'dart:io';
import 'dart:typed_data';

void main() async {
  WebSocket socket = await WebSocket.connect('ws://echo.websocket.org');
  
  // Text message
  socket.add('Hello!');
  
  // Binary message
  socket.add(Uint8List.fromList([1, 2, 3, 4]));
  
  // JSON message
  socket.add('{"type": "greeting", "text": "Hi"}');
  
  socket.listen((message) {
    if (message is String) {
      print('Text: $message');
    } else if (message is Uint8List) {
      print('Binary: ${message.length} bytes');
    }
  });
  
  await Future.delayed(Duration(seconds: 2));
  await socket.close();
}
```

**Solution 4: Implement ping/pong keepalive**

```dart
import 'dart:async';
import 'dart:io';

void main() async {
  WebSocket socket = await WebSocket.connect('ws://echo.websocket.org');
  Timer? pingTimer;
  
  socket.listen(
    (message) => print('Received: $message'),
    onDone: () {
      pingTimer?.cancel();
      print('Disconnected');
    },
  );
  
  // Send periodic pings
  pingTimer = Timer.periodic(Duration(seconds: 30), (_) {
    if (socket.readyState == WebSocket.open) {
      socket.add('ping');
    }
  });
  
  await Future.delayed(Duration(minutes: 1));
  await socket.close();
  pingTimer.cancel();
}
```

**Solution 5: Connect with headers**

```dart
import 'dart:io';

void main() async {
  Map<String, String> headers = {
    'Authorization': 'Bearer token123',
    'X-Custom': 'value',
  };
  
  WebSocket socket = await WebSocket.connect(
    'wss://echo.websocket.org',
    headers: headers,
  );
  
  socket.listen(
    (message) => print('Received: $message'),
    onDone: () => print('Done'),
  );
  
  socket.add('Hello with headers!');
  
  await Future.delayed(Duration(seconds: 2));
  await socket.close();
}
```

## Examples

WebSocket connections use the `ws://` scheme for non-secure or `wss://` for TLS. The `readyState` property indicates the connection state: `connectinging` (0), `open` (1), `closing` (2), or `closed` (3).

## Related Errors

- [Dart HTTP Request Error](/languages/dart/dart-http-request-error/)
- [Dart IO Socket Error](/languages/dart/dart-io-socket-error/)
- [Dart HTTP Server Error](/languages/dart/dart-http-server-error/)
