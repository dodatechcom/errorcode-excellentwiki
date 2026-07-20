---
title: "[Solution] Dart Directory Error — list, delete, rename, recursive, followLinks"
description: "Fix Dart Directory errors from listing, deleting, renaming, recursive operations, and followLinks issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 132
---

Directory errors occur when operations fail due to missing directories, permission issues, or recursive/symlink configurations.

## Common Causes

1. `Directory.list()` on a non-existent directory.
2. `delete()` failing because the directory is not empty without `recursive: true`.
3. `rename()` failing because the target path already exists.
4. Not handling `followLinks` causing symlink loops.
5. `create(recursive: true)` not being called for nested paths.

## How to Fix It

**Solution 1: List directory contents safely**

```dart
import 'dart:io';

void main() async {
  Directory dir = Directory('test');
  
  if (await dir.exists()) {
    await for (FileSystemEntity entity in dir.list()) {
      print(entity.path);
    }
  } else {
    print('Directory does not exist');
  }
}
```

**Solution 2: Delete recursively when needed**

```dart
import 'dart:io';

void main() async {
  Directory dir = Directory('temp');
  
  // Create nested structure for demo
  await dir.create(recursive: true);
  await File('${dir.path}/sub/file.txt').create(recursive: true);
  
  // Delete recursively
  await dir.delete(recursive: true);
  print('Deleted');
}
```

**Solution 3: Rename with conflict handling**

```dart
import 'dart:io';

void main() async {
  Directory source = Directory('old_name');
  Directory target = Directory('new_name');
  
  if (await source.exists()) {
    if (await target.exists()) {
      await target.delete(recursive: true);
    }
    await source.rename(target.path);
    print('Renamed');
  }
}
```

**Solution 4: Create directories recursively**

```dart
import 'dart:io';

void main() async {
  Directory deep = Directory('a/b/c/d');
  
  await deep.create(recursive: true);
  print('Created: ${deep.path}');
  
  // Verify
  print('Exists: ${await deep.exists()}'); // true
}
```

**Solution 5: Handle symlink loops with followLinks**

```dart
import 'dart:io';

void main() async {
  Directory dir = Directory('test_dir');
  await dir.create();
  
  // List without following links (avoids infinite loops)
  await for (FileSystemEntity entity in dir.list(followLinks: false)) {
    print(entity.path);
  }
}
```

## Examples

`Directory.list()` is asynchronous and returns a `Stream<FileSystemEntity>`. Use `listSync()` for synchronous listing, but avoid it in production code due to event loop blocking.

## Related Errors

- [Dart File Open Error](/languages/dart/dart-file-open-error/)
- [Dart File Sync Error](/languages/dart/dart-file-sync-error/)
- [Dart Path Provider Error](/languages/dart/flutter-path-provider-error/)
