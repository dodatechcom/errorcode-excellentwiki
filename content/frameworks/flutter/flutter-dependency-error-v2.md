---
title: "Dependency conflict in Flutter"
description: "Flutter throws a dependency conflict error when two or more packages require incompatible versions of a shared dependency"
frameworks: ["flutter"]
error-types: ["build-error"]
severities: ["error"]
weight: 5
---

A dependency conflict in Flutter occurs when two or more packages in your `pubspec.yaml` require incompatible versions of the same shared dependency. This is different from version solving failures, as it specifically refers to direct dependency conflicts.

## Common Causes

- Two packages depend on different major versions of the same library
- Package was recently updated with breaking changes
- Legacy packages not maintained or updated
- Using both `^` and explicit version constraints that conflict

## How to Fix

1. Identify the conflicting dependency:

```bash
flutter pub get 2>&1 | grep -A5 "conflict"
dart pub deps --no-dev
```

2. Update both conflicting packages to latest versions:

```bash
flutter pub upgrade --major-versions
```

3. Use dependency overrides as a temporary fix:

```yaml
# pubspec.yaml
dependency_overrides:
  path_provider: ^2.1.0
```

4. Find alternatives if a package is unmaintained:

```bash
# Search for alternative packages
dart pub search <function-name>
```

5. Pin to specific versions that are known to work together:

```yaml
dependencies:
  cached_network_image: 3.3.0
  image_picker: 1.0.4
```

## Examples

```yaml
# pubspec.yaml with conflict
dependencies:
  package_a: ^2.0.0  # requires dio ^5.0.0
  package_b: ^1.0.0  # requires dio ^4.0.0

# Fix: override dio
dependency_overrides:
  dio: ^5.3.0
```

```bash
$ flutter pub get
Because package_a >=2.0.0 depends on dio ^5.0.0 and 
  package_b >=1.0.0 depends on dio ^4.0.0, 
  package_a is incompatible with package_b.
```

## Related Errors

- [Pub error]({{< relref "/frameworks/flutter/flutter-pub-error-v2" >}})
- [Build error]({{< relref "/frameworks/flutter/flutter-build-error-v2" >}})
