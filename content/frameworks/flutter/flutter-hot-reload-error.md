---
title: "Hot reload - incremental compilation error"
description: "Flutter hot reload fails when incremental compilation encounters code changes it cannot handle"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Flutter hot reload incremental compilation error occurs when changes to your code cannot be applied while the app is running. Hot reload works by recompiling only the changed libraries, but certain changes require a full restart.

## Common Causes

- Changes to main() or initialization code
- Modifying enum definitions
- Changing generic type parameters
- Updating native plugin code
- Modifying const constructors

## How to Fix

1. Identify which changes require a full restart:

```dart
// These changes require hot restart, not hot reload:
// - Changes to main()
// - Changes to enum values
// - Changes to native code
// - Adding/removing const constructors
```

2. Perform a hot restart instead of hot reload:

```bash
# In the terminal running flutter run
# Press 'R' (capital R) for hot restart instead of 'r' for hot reload
```

3. Use `reassemble` for specific widget rebuilds:

```dart
@override
void reassemble() {
  super.reassemble();
  // Re-initialize anything needed for hot reload
}
```

4. Check for hot reload errors in the terminal:

```bash
flutter run --verbose
# Look for "Cannot hot reload" messages
```

5. Reset with full restart when hot reload fails:

```bash
flutter run --no-hot
```

## Examples

```dart
// This will cause hot reload to fail
enum Status { active, inactive } // changed enum

// Hot reload error: Cannot hot reload because new type has been added to enum
// Fix: hot restart instead (press R)
```

```dart
// Changing const constructor also breaks hot reload
const MyWidget({Key? key}) : super(key: key);
// Changed to non-const
MyWidget({Key? key}) : super(key: key);
// Fix: hot restart needed
```

## Related Errors

- [Fast Refresh error]({{< relref "/frameworks/react-native/rn-fast-refresh-error" >}})
- [Build error]({{< relref "/frameworks/flutter/flutter-build-error-v2" >}})
