---
title: "Import error"
description: "An import error occurs when Dart cannot find or load a specified library or file."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["import", "library", "not-found", "dart"]
weight: 5
---

## What This Error Means

An import error occurs when the Dart compiler or runtime cannot locate or load a specified library. This can happen with missing files, incorrect paths, or missing package dependencies.

## Common Causes

- File doesn't exist at import path
- Typo in import path
- Package not in pubspec.yaml
- Wrong relative path

## How to Fix

```dart
// WRONG: Importing non-existent file
import 'package:my_app/nonexistent.dart';  // Error

// CORRECT: Verify file exists
import 'package:my_app/models/user.dart';
```

```dart
// WRONG: Wrong relative path
import '../wrong/path/file.dart';  // Error

// CORRECT: Use correct relative path
import 'models/user.dart';
```

## Examples

```dart
// Example 1: Typo in path
import 'package:my_app/modles/user.dart';  // Error

// Example 2: Missing package
import 'package:nonexistent_package/nonexistent.dart';  // Error

// Example 3: Wrong relative path
import 'src/wrong_file.dart';  // Error if file doesn't exist
```

## Related Errors

- [type cast error](/languages/dart/type-cast-error)
- [FormatException: Invalid format](/languages/dart/format-error)
