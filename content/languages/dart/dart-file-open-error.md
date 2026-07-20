---
title: "[Solution] Dart File Open Error — readAsString, readAsBytes, writeAsString, Mode"
description: "Fix Dart File open errors from readAsString, readAsBytes, writeAsString failures, and file mode issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 130
---

File open errors occur when files do not exist, permissions are insufficient, or file modes are used incorrectly.

## Common Causes

1. File does not exist at the specified path.
2. Insufficient file system permissions.
3. Using `File(mode: FileMode.write)` which truncates the file.
4. Reading a binary file as string or vice versa.
5. Path is relative and the working directory is unexpected.

## How to Fix It

**Solution 1: Check file existence before opening**

```dart
import 'dart:io';

void main() async {
  File file = File('data.txt');
  
  if (await file.exists()) {
    String contents = await file.readAsString();
    print(contents);
  } else {
    print('File not found: ${file.path}');
  }
}
```

**Solution 2: Use appropriate file modes**

```dart
import 'dart:io';

void main() async {
  File file = File('output.txt');
  
  // Append mode — preserves existing content
  await file.writeAsString('Hello\n', mode: FileMode.append);
  await file.writeAsString('World\n', mode: FileMode.append);
  
  String contents = await file.readAsString();
  print(contents); // Hello\nWorld\n
}
```

**Solution 3: Read bytes for binary files**

```dart
import 'dart:io';

void main() async {
  File file = File('image.png');
  
  if (await file.exists()) {
    List<int> bytes = await file.readAsBytes();
    print('File size: ${bytes.length} bytes');
  }
}
```

**Solution 4: Handle path resolution**

```dart
import 'dart:io';

void main() async {
  // Use absolute paths for reliability
  String currentDir = Directory.current.path;
  File file = File('$currentDir/data/config.json');
  
  print('Resolved path: ${file.path}');
  
  if (await file.exists()) {
    String contents = await file.readAsString();
    print(contents);
  }
}
```

**Solution 5: Use try-catch for I/O operations**

```dart
import 'dart:io';

void main() async {
  try {
    File file = File('missing.txt');
    String contents = await file.readAsString();
    print(contents);
  } on FileSystemException catch (e) {
    print('File system error: ${e.message}');
    print('Path: ${e.path}');
  } catch (e) {
    print('Unexpected error: $e');
  }
}
```

## Examples

`FileMode.write` truncates the file by default. Use `FileMode.writeOnlyAppend` or `FileMode.append` to add content without erasing existing data.

## Related Errors

- [Dart File Sync Error](/languages/dart/dart-file-sync-error/)
- [Dart Directory Error](/languages/dart/dart-directory-error/)
- [Dart IO Encoding Error](/languages/dart/dart-io-encoding-error/)
