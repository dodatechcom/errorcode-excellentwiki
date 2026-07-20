---
title: "[Solution] Dart IO Encoding Error — UTF-8, Latin1, ASCII, Encoder/Decoder"
description: "Fix Dart IO encoding errors from UTF-8, Latin1, ASCII codec issues, and encoder/decoder misuse."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 137
---

Encoding errors occur when text is decoded using the wrong codec, or when byte sequences are invalid for the specified encoding.

## Common Causes

1. Decoding UTF-8 bytes with `latin1` codec, producing garbled text.
2. Invalid UTF-8 byte sequences causing `FormatException`.
3. Mixing `SystemEncoding` with UTF-8 content.
4. Using `ascii` codec for non-ASCII characters.
5. Not handling BOM (Byte Order Mark) in files.

## How to Fix It

**Solution 1: Use the correct encoding**

```dart
import 'dart:convert';
import 'dart:io';

void main() async {
  // UTF-8 is the default for most modern systems
  File file = File('data.txt');
  
  // Explicit UTF-8
  String contents = await file.readAsString(encoding: utf8);
  print(contents);
}
```

**Solution 2: Handle encoding errors gracefully**

```dart
import 'dart:convert';

void main() {
  List<int> invalidUtf8 = [0xC0, 0xAF]; // Invalid UTF-8 sequence
  
  try {
    String decoded = utf8.decoder.convert(invalidUtf8);
    print(decoded);
  } on FormatException catch (e) {
    print('Invalid UTF-8: $e');
    
    // Use allowMalformed to skip invalid bytes
    String decoded = utf8.decoder.fuse(utf8).convert(
      invalidUtf8,
      // For streaming: allowMalformed: true
    );
  }
}
```

**Solution 3: Convert between encodings**

```dart
import 'dart:convert';

void main() {
  String text = 'Hello, World! café';
  
  // Encode to UTF-8 bytes
  List<int> utf8Bytes = utf8.encode(text);
  print('UTF-8 bytes: $utf8Bytes');
  
  // Decode from UTF-8
  String decoded = utf8.decode(utf8Bytes);
  print('Decoded: $decoded');
  
  // Latin1 encoding (only works for characters <= U+00FF)
  List<int> latin1Bytes = latin1.encode(text);
  print('Latin1 bytes: $latin1Bytes');
}
```

**Solution 4: Stream with proper encoding**

```dart
import 'dart:convert';
import 'dart:io';

void main() async {
  File file = File('output.txt');
  IOSink sink = file.openWrite(encoding: utf8);
  
  sink.writeln('Hello, UTF-8!');
  sink.writeln('Special chars: ñ, ü, 日本語');
  await sink.close();
  
  String contents = await file.readAsString(encoding: utf8);
  print(contents);
}
```

**Solution 5: Handle BOM in files**

```dart
import 'dart:convert';
import 'dart:io';

void main() async {
  File file = File('data_bom.txt');
  List<int> bytes = await file.readAsBytes();
  
  // Check for UTF-8 BOM
  if (bytes.length >= 3 &&
      bytes[0] == 0xEF &&
      bytes[1] == 0xBB &&
      bytes[2] == 0xBF) {
    // Skip BOM
    String contents = utf8.decode(bytes.sublist(3));
    print(contents);
  } else {
    String contents = utf8.decode(bytes);
    print(contents);
  }
}
```

## Examples

`SystemEncoding` uses the system's default encoding, which varies by platform. Always use explicit `utf8` codec when cross-platform compatibility is needed.

## Related Errors

- [Dart File Open Error](/languages/dart/dart-file-open-error/)
- [Dart String Concat Error](/languages/dart/dart-string-concat-error/)
- [Dart URI Encode Error](/languages/dart/dart-uri-encode-error/)
