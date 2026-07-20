---
title: "[Solution] Dart stdin Error — readLineSync, addListener, EOF, pipe"
description: "Fix Dart stdin errors from readLineSync issues, EOF handling, listener management, and pipe failures."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 136
---

stdin errors occur when reading from standard input fails, EOF is reached unexpectedly, or listeners are not properly managed.

## Common Causes

1. `readLineSync()` returning `null` at EOF.
2. Using `stdin.listen` without handling the `onDone` event.
3. Blocking reads in async contexts.
4. `pipe` failing when the destination stream is already closed.
5. Echo behavior interfering with input parsing.

## How to Fix It

**Solution 1: Handle EOF from readLineSync**

```dart
import 'dart:io';

void main() {
  print('Enter your name:');
  String? name = stdin.readLineSync();
  
  if (name != null) {
    print('Hello, $name!');
  } else {
    print('EOF reached — no input received');
  }
}
```

**Solution 2: Listen to stdin properly**

```dart
import 'dart:io';

void main() {
  stdin.listen(
    (List<int> data) {
      String text = String.fromCharCodes(data);
      print('Input: $text');
    },
    onDone: () => print('stdin closed'),
    onError: (error) => print('Error: $error'),
  );
}
```

**Solution 3: Read bytes from stdin**

```dart
import 'dart:io';

void main() async {
  print('Reading from stdin (Ctrl+D to end):');
  
  Stream<List<int>> byteStream = stdin.asBroadcastStream();
  
  await for (List<int> bytes in byteStream) {
    print('Received ${bytes.length} bytes');
    print('As text: ${String.fromCharCodes(bytes)}');
  }
}
```

**Solution 4: Pipe stdin to a file**

```dart
import 'dart:io';

void main() async {
  File outputFile = File('input_log.txt');
  IOSink sink = outputFile.openWrite();
  
  await stdin.pipe(sink);
  
  print('Input saved to ${outputFile.path}');
}
```

**Solution 5: Read specific bytes**

```dart
import 'dart:io';

void main() async {
  print('Press keys (Ctrl+D to exit):');
  
  stdin.echoMode = false;
  stdin.lineMode = false;
  
  await for (List<int> bytes in stdin) {
    for (int byte in bytes) {
      print('Byte: $byte (${String.fromCharCode(byte)})');
    }
  }
  
  stdin.echoMode = true;
  stdin.lineMode = true;
}
```

## Examples

`stdin.readLineSync()` returns `null` when the input stream ends (EOF). In non-interactive environments (CI/CD, pipes), stdin may be closed immediately.

## Related Errors

- [Dart IO Encoding Error](/languages/dart/dart-io-encoding-error/)
- [Dart Process Run Error](/languages/dart/dart-process-run-error/)
- [Dart Stream Subscription Error](/languages/dart/dart-stream-subscription-error/)
