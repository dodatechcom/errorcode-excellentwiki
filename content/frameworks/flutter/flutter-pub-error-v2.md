---
title: "pub get - version solving failed"
description: "Flutter pub get fails when it cannot resolve compatible versions for all dependencies in pubspec.yaml"
frameworks: ["flutter"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

The "version solving failed" error occurs when `flutter pub get` cannot find a set of dependency versions that are all mutually compatible. This typically happens when packages have conflicting SDK constraints or when a required version range does not overlap.

## Common Causes

- Two packages require incompatible versions of the same dependency
- Package SDK constraint does not match your Flutter/Dart SDK version
- Circular dependency chain with conflicting requirements
- Package not updated for latest Flutter SDK

## How to Fix

1. Check which dependency is causing the conflict:

```bash
flutter pub get --verbose
```

2. Update all dependencies to their latest compatible versions:

```bash
flutter pub upgrade
```

3. Use dependency overrides to force a version:

```yaml
# pubspec.yaml
dependency_overrides:
  http: ^1.0.0
```

4. Check version constraints of all dependencies:

```yaml
dependencies:
  provider: ^6.0.0        # uses ^ notation
  http: ">=0.13.0 <2.0.0" # uses range notation
  intl: any               # uses any (avoid this)
```

5. Run `dart pub deps` to see the full dependency tree:

```bash
dart pub deps
```

6. Clean and retry:

```bash
flutter clean
flutter pub get
```

## Examples

```bash
$ flutter pub get
Resolving dependencies... 
Because every version of flutter_test from sdk depends on
  collection >=1.17.0 <1.18.0 and older_text depends collection >=1.18.0,
  flutter_test from sdk is incompatible with older_text.
So, because myapp depends on both flutter_test from sdk and older_text,
  version solving failed.
```

```yaml
# Fix: update conflicting package or use override
dependency_overrides:
  collection: ^1.18.0
```

## Related Errors

- [Dependency error]({{< relref "/frameworks/flutter/flutter-dependency-error-v2" >}})
- [Build error]({{< relref "/frameworks/flutter/flutter-build-error-v2" >}})
