---
title: "[Solution] Dart FFI Native Error"
description: "Fix Dart FFI (Foreign Function Interface) errors including symbol lookup failures, memory access violations, and type mismatches."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["ffi", "native", "c", "interop", "memory", "dart"]
weight: 5
---

## What This Error Means

Dart FFI errors occur when the Foreign Function Interface fails to load native libraries, resolve symbols, or correctly marshal data between Dart and native code. These errors can crash the application.

## Common Causes

- Native library not found or wrong path
- Symbol name mismatch (C name mangling)
- Incorrect function signatures in Dart bindings
- Memory allocation/deallocation issues
- Platform-specific library formats (.so, .dylib, .dll)

## How to Fix

```dart
// WRONG: Hardcoded library path
final dylib = DynamicLibrary.open('libfoo.so');  // May fail on macOS

// CORRECT: Platform-aware library loading
import 'dart:io';
final dylib = DynamicLibrary.open(
  Platform.isWindows ? 'foo.dll' :
  Platform.isMacOS ? 'libfoo.dylib' :
  'libfoo.so'
);
```

```dart
// WRONG: Incorrect function signature
typedef HelloFunc = Void Function();  // Wrong: C function returns int
final hello = dylib.lookupFunction<HelloFunc, HelloFunc>('hello');

// CORRECT: Match C signature exactly
// C: int hello(const char* name);
typedef HelloCFunc = Int32 Function(Pointer<Utf8> name);
typedef HelloDartFunc = int Function(Pointer<Utf8> name);
final hello = dylib.lookupFunction<HelloCFunc, HelloDartFunc>('hello');
```

```dart
// WRONG: Not managing memory
Pointer<Utf8> str = 'hello'.toNativeUtf8();  // Memory leak

// CORRECT: Free native memory
final str = 'hello'.toNativeUtf8();
try {
  final result = hello(str);
} finally {
  calloc.free(str);  // Or str.cast<Char>().free()
}
```

## Examples

```dart
import 'dart:ffi';
import 'package:ffi/ffi.dart';
import 'dart:io';

// Example 1: Safe FFI loading
DynamicLibrary? loadLibrary(String name) {
  try {
    return DynamicLibrary.open(name);
  } catch (e) {
    print('Failed to load library: $e');
    return null;
  }
}

// Example 2: Complete FFI binding example
// C header:
// int add(int a, int b);
typedef AddNative = Int32 Function(Int32 a, Int32 b);
typedef AddDart = int Function(int a, int b);

void main() {
  final dylib = DynamicLibrary.open('libmath.so');
  final add = dylib.lookupFunction<AddNative, AddDart>('add');
  print(add(2, 3));  // 5
}

// Example 3: Struct example
final class MyStruct extends Struct {
  @Int32()
  external int value;
  
  @Pointer()
  external Pointer<Utf8> name;
}
```

## Related Errors

- [dart-io-error]({{< relref "/languages/dart/dart-io-error" >}}) — I/O errors
- [dart-type-error]({{< relref "/languages/dart/dart-type-error" >}}) — type mismatch
- [dart-null-error]({{< relref "/languages/dart/dart-null-error" >}}) — null check error
