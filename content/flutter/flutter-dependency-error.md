---
title: "Dependency resolution failed"
description: "Flutter throws a dependency resolution error when pub cannot find compatible package versions"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["dependency", "resolution", "version-conflict", "pubspec", "package"]
weight: 5
---

This error occurs when the Dart package resolver cannot find a set of compatible package versions that satisfy all version constraints in `pubspec.yaml` and their transitive dependencies.

## Common Causes

- Two packages require conflicting versions of the same transitive dependency
- A package was discontinued or removed from pub.dev
- Circular dependency between packages
- Lower bound of a dependency exceeds the version available
- Pre-release versions conflicting with stable constraints

## How to Fix

1. Run `dart pub deps` to inspect the dependency tree:

```bash
dart pub deps
```

2. Use `dart pub upgrade` to find the latest compatible versions:

```bash
dart pub upgrade --major-versions
```

3. Pin specific versions or use `dependency_overrides`:

```yaml
dependency_overrides:
  # Temporary override while waiting for upstream fix
  transitive_package: 2.1.0
```

4. Remove or replace incompatible packages:

```yaml
# Before — conflict
dependencies:
  package_a: ^1.0.0   # requires http ^0.12.0
  package_b: ^3.0.0   # requires http ^1.0.0

# After — find alternatives
dependencies:
  package_a: ^2.0.0   # updated — now compatible
  package_b: ^3.0.0
```

## Examples

```text
Because every version of package_a depends on http ^0.13.0 and package_b >=3.0.0
depends on http ^1.0.0, package_a is incompatible with package_b.
```

## Related Errors

- [Pub error]({{< relref "/frameworks/flutter/pub-error" >}})
- [Build error]({{< relref "/frameworks/flutter/build-error6" >}})
