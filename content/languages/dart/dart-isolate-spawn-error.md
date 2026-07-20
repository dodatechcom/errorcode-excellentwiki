---
title: "[Solution] Dart Isolate.spawn Error — SendPort, ReceivePort, Close"
description: "Fix Dart Isolate.spawn errors from SendPort/ReceivePort misuse, message passing failures, and resource cleanup."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 126
---

Isolate spawn errors occur when isolates fail to start, messages cannot be sent through ports, or ports are not properly closed.

## Common Causes

1. Passing non-sendable objects through `SendPort`.
2. `ReceivePort` not being closed, causing isolate leaks.
3. `Isolate.spawn` failing due to unhandled errors in the isolate entry point.
4. Trying to send a `SendPort` from the main isolate before the child isolate provides one.
5. Sending large objects that exceed memory limits.

## How to Fix It

**Solution 1: Spawn an isolate with proper communication**

```dart
import 'dart:isolate';

void main() async {
  ReceivePort receivePort = ReceivePort();
  
  await Isolate.spawn(
    _isolateEntry,
    receivePort.sendPort,
  );
  
  SendPort replyPort = await receivePort.first;
  print('Got reply port from isolate');
  
  // Send a message
  replyPort.send('Hello from main');
  
  receivePort.close();
}

void _isolateEntry(SendPort mainSendPort) {
  ReceivePort isolateReceivePort = ReceivePort();
  mainSendPort.send(isolateReceivePort.sendPort);
  
  isolateReceivePort.listen((message) {
    print('Isolate received: $message');
    mainSendPort.send('Echo: $message');
  });
}
```

**Solution 2: Handle isolate spawn errors**

```dart
import 'dart:isolate';

void main() async {
  ReceivePort receivePort = ReceivePort();
  
  try {
    Isolate isolate = await Isolate.spawn(
      _failingEntry,
      receivePort.sendPort,
      onError: receivePort.sendPort,
      onExit: receivePort.sendPort,
    );
  } catch (e) {
    print('Failed to spawn isolate: $e');
  }
}

void _failingEntry(SendPort sendPort) {
  throw Exception('Isolate failed');
}
```

**Solution 3: Close ReceivePort to signal completion**

```dart
import 'dart:isolate';

void main() async {
  ReceivePort port = ReceivePort();
  
  await Isolate.spawn(_worker, port.sendPort);
  
  await for (var message in port) {
    print('Received: $message');
    if (message == 'done') break;
  }
  
  port.close();
}

void _worker(SendPort sendPort) {
  for (int i = 0; i < 5; i++) {
    sendPort.send('Message $i');
  }
  sendPort.send('done');
}
```

**Solution 4: Use `Isolate.run` for simple tasks**

```dart
import 'dart:isolate';

void main() async {
  int result = await Isolate.run(() {
    // Heavy computation
    int sum = 0;
    for (int i = 0; i < 1000000; i++) {
      sum += i;
    }
    return sum;
  });
  
  print('Result: $result');
}
```

**Solution 5: Pass only sendable types**

```dart
import 'dart:isolate';

// Only primitive types, SendPort, and their combinations are sendable
void main() async {
  ReceivePort port = ReceivePort();
  
  await Isolate.spawn(_worker, {
    'port': port.sendPort,
    'data': [1, 2, 3], // List<int> is sendable
  });
  
  print(await port.first);
  port.close();
}

void _worker(Map<String, dynamic> message) {
  SendPort replyPort = message['port'];
  List<int> data = List<int>.from(message['data']);
  replyPort.send(data.map((e) => e * 2).toList());
}
```

## Examples

Isolates do not share memory. All communication happens through message passing. Messages are serialized, so only certain types can be sent between isolates.

## Related Errors

- [Dart Isolate Compute Error](/languages/dart/dart-isolate-compute-error/)
- [Dart Zone Error](/languages/dart/dart-zone-error/)
- [Dart Stream Controller Error](/languages/dart/dart-stream-controller-error/)
