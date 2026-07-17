---
title: "pub get failed"
description: "Flutter throws a pub get error when it cannot resolve or download package dependencies"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["pub", "packages", "dependency", "pubspec", "registry"]
weight: 5
---

This error occurs when `flutter pub get` or `dart pub get` fails to resolve or download packages. It can be caused by version conflicts, network issues, or pubspec.yaml errors.

## Common Causes

- Package version conflicts between dependencies
- Network connectivity issues downloading packages
- `pubspec.yaml` has syntax errors
- Package does not exist or has been discontinued
- Dart SDK version incompatible with the package

## How to Fix

1. Check for version conflicts:

```bash
dart pub deps
dart pub outdated
```

2. Resolve conflicts by updating versions in `pubspec.yaml`:

```yaml
dependencies:
  flutter:
    sdk: flutter
  http: ^1.1.0
  provider: ^6.1.1
```

3. Clear the pub cache and retry:

```bash
dart pub cache clean
flutter pub get
```

4. Use `dependency_overrides` as a temporary fix:

```yaml
dependency_overrides:
  http: ^1.1.0
```

## Examples

```yaml
# pubspec.yaml — version conflict
dependencies:
  http: ^0.13.0    # requires dart >=2.12
  dio: ^5.0.0      # requires dart >=3.0
# Error: Because dio >=5.0.0 requires Dart SDK >=3.0.0
```

## Related Errors

- [Dependency error]({{< relref "/frameworks/flutter/dependency-error" >}})
- [Build error]({{< relref "/frameworks/flutter/build-error6" >}})
