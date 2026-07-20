---
title: "[Solution] Dart FileSync Error — FileSystemEntity Type, existsSync, statSync"
description: "Fix Dart synchronous file system errors from FileSystemEntity type checks, existsSync, and statSync."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 131
---

FileSync errors occur when using synchronous file operations on paths that don't exist, or when misidentifying the type of a file system entity.

## Common Causes

1. `existsSync()` returning false but code proceeds to read.
2. `statSync()` on a non-existent path throwing `FileSystemException`.
3. Treating a directory as a file or vice versa.
4. `FileSystemEntity.typeSync` returning `FileSystemEntityType.notFound`.
5. Symlink resolution issues with `followLinks` parameter.

## How to Fix It

**Solution 1: Check type before operations**

```dart
import 'dart:io';

void main() {
  String path = 'example.txt';
  
  FileSystemEntityType type = FileSystemEntity.typeSync(path);
  
  switch (type) {
    case FileSystemEntityType.file:
      print('It is a file');
      break;
    case FileSystemEntityType.directory:
      print('It is a directory');
      break;
    case FileSystemEntityType.link:
      print('It is a symlink');
      break;
    case FileSystemEntityType.notFound:
      print('Path not found');
      break;
  }
}
```

**Solution 2: Use `statSync` safely**

```dart
import 'dart:io';

void main() {
  FileStat stat;
  
  try {
    stat = FileStat.statSync('data.txt');
    print('Type: ${stat.type}');
    print('Size: ${stat.size}');
    print('Modified: ${stat.modified}');
  } on FileSystemException catch (e) {
    print('Cannot stat file: ${e.message}');
  }
}
```

**Solution 3: Verify existsSync before reading**

```dart
import 'dart:io';

void main() {
  File file = File('config.json');
  
  if (file.existsSync()) {
    String contents = file.readAsStringSync();
    print(contents);
  } else {
    print('File does not exist');
  }
}
```

**Solution 4: Handle symlinks**

```dart
import 'dart:io';

void main() {
  String path = 'link_to_file';
  
  FileSystemEntity entity = FileSystemEntity.isLinkSync(path)
      ? Link(path)
      : File(path);
  
  print('Entity: ${entity.path}');
  print('Is link: ${FileSystemEntity.isLinkSync(path)}');
}
```

**Solution 5: Use `listSync` for directory enumeration**

```dart
import 'dart:io';

void main() {
  Directory dir = Directory.current;
  
  List<FileSystemEntity> entities = dir.listSync();
  
  for (FileSystemEntity entity in entities) {
    String type = entity is File ? 'FILE' :
                  entity is Directory ? 'DIR' : 'OTHER';
    print('$type: ${entity.path}');
  }
}
```

## Examples

Synchronous file operations (`readAsStringSync`, `existsSync`) block the event loop. Use them only during initialization or in isolates where async is not available.

## Related Errors

- [Dart File Open Error](/languages/dart/dart-file-open-error/)
- [Dart Directory Error](/languages/dart/dart-directory-error/)
- [Dart Path Error](/languages/dart/dart-path-error/)
