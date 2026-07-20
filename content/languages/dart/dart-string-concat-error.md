---
title: "[Solution] Dart String Concatenation Error — Buffer, Plus, writeAll Issues"
description: "Fix Dart string concatenation errors with StringBuffer, plus operator, writeAll, and writeCharCode performance."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 109
---

String concatenation errors range from performance issues with `+` in loops to incorrect `StringBuffer` usage and encoding problems with `writeCharCode`.

## Common Causes

1. Using `+` operator in loops — creates unnecessary intermediate strings.
2. `StringBuffer` not being flushed with `.toString()`.
3. `writeCharCode` with invalid Unicode values.
4. `writeAll` separator argument used incorrectly.
5. Interpolation in long strings causing performance issues.

## How to Fix It

**Solution 1: Use `StringBuffer` for multiple concatenations**

```dart
void main() {
  StringBuffer buffer = StringBuffer();
  
  for (int i = 0; i < 1000; i++) {
    buffer.write('item $i, ');
  }
  
  String result = buffer.toString();
  print(result.substring(0, 50));
}
```

**Solution 2: Use string interpolation instead of `+`**

```dart
void main() {
  String name = 'Alice';
  int age = 30;
  
  // Preferred: interpolation
  String greeting = 'My name is $name and I am $age years old.';
  
  // Avoid: concatenation
  String alsoGreeting = 'My name is ' + name + ' and I am ' + age.toString() + ' years old.';
  
  print(greeting);
}
```

**Solution 3: Use `writeAll` with proper separator**

```dart
void main() {
  StringBuffer buffer = StringBuffer();
  List<String> words = ['hello', 'world', 'dart'];
  
  buffer.writeAll(words, ' ');
  print(buffer.toString()); // "hello world dart"
  
  // Without separator — joins directly
  StringBuffer noSep = StringBuffer();
  noSep.writeAll(words);
  print(noSep.toString()); // "helloworlddart"
}
```

**Solution 4: Validate Unicode code points in `writeCharCode`**

```dart
void main() {
  StringBuffer buffer = StringBuffer();
  
  buffer.writeCharCode(72);  // H
  buffer.writeCharCode(105); // i
  print(buffer.toString()); // "Hi"
  
  // Supplementary plane characters need two calls
  buffer.writeCharCode(0x1F600); // 😀
  print(buffer.toString());
}
```

**Solution 5: Pre-allocate capacity for large strings**

```dart
void main() {
  // For very large concatenations, consider List<String>.join
  List<String> parts = List.generate(10000, (i) => 'item$i');
  
  String result = parts.join(', ');
  print('Length: ${result.length}');
}
```

## Examples

In Dart, strings are immutable. Each `+` operation creates a new `String` object. For building strings in loops with many iterations, always use `StringBuffer` or `List.join`.

## Related Errors

- [Dart Rune Error](/languages/dart/dart-rune-error/)
- [Dart RegExp Error](/languages/dart/dart-regexp-error/)
- [Dart IO Encoding Error](/languages/dart/dart-io-encoding-error/)
