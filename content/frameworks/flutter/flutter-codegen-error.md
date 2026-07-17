---
title: "Build runner - code generation error"
description: "Flutter build_runner fails to generate code due to source code errors or configuration issues"
frameworks: ["flutter"]
error-types: ["build-error"]
severities: ["error"]
tags: ["flutter", "build-runner", "code-generation", "json-serializable", "freezed"]
weight: 5
---

A build runner code generation error occurs when `flutter pub run build_runner build` fails to generate code from annotations like `json_serializable`, `freezed`, or `auto_route`. The generator cannot parse or process the annotated source code.

## Common Causes

- Syntax errors in annotated source files
- Missing or invalid annotations on model classes
- Circular imports between generated files
- Conflicting code generators producing duplicate code
- build_runner version incompatibility

## How to Fix

1. Clean generated files and rebuild:

```bash
flutter pub run build_runner build --delete-conflicting-outputs
```

2. Check for syntax errors in annotated files:

```dart
// Valid: proper annotation syntax
@JsonSerializable()
class User {
  final String name;
  final int age;

  User({required this.name, required this.age});

  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
  Map<String, dynamic> toJson() => _$UserToJson(this);
}
```

3. Ensure generated files are in the correct location:

```dart
// In your model file
part 'user.g.dart'; // must match filename

@JsonSerializable()
class User { ... }
```

4. Run in watch mode to catch errors early:

```bash
flutter pub run build_runner watch --delete-conflicting-outputs
```

5. Check for conflicting code generators:

```yaml
# pubspec.yaml - order matters
dev_dependencies:
  build_runner: ^2.4.0
  json_serializable: ^6.7.0
  freezed: ^2.4.0
  freezed_annotation: ^2.4.0
```

6. Handle import conflicts:

```dart
// Bad: circular import
// user.dart imports order.dart, order.dart imports user.dart

// Fix: use shared types file
// models.dart - shared types
// user.dart - imports models.dart
// order.dart - imports models.dart
```

## Examples

```bash
$ flutter pub run build_runner build
[INFO] Generating build files...
[SEVERE] lib/models/user.dart:10:8 - Error: Could not find generated counterpart for `_$UserFromJson`.

# Fix: ensure part directive is correct
part 'user.g.dart';  // must be 'user.g.dart' for 'user.dart'
```

## Related Errors

- [Build error]({{< relref "/frameworks/flutter/flutter-build-error-v2" >}})
- [FFI error]({{< relref "/frameworks/flutter/flutter-ffi-error" >}})
