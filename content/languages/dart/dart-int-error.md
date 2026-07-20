---
title: "[Solution] Dart Integer Error — Overflow, Parse Radix, toInt Truncation"
description: "Fix Dart integer errors from overflow, parseInt radix issues, big integer conversion, and toInt truncation."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 105
---

Integer errors in Dart occur when numeric operations exceed `int` range, `parseInt` receives invalid radix values, or `toInt()` truncates unexpected values.

## Common Causes

1. `int` overflow on 32-bit platforms (max ~2.1 billion).
2. `int.parse` with radix outside 2–36 range.
3. `double.toInt()` truncating fractional parts unexpectedly.
4. `parseInt` failing on strings with unexpected characters.
5. Assuming `int` is 64-bit on all platforms (it's platform-dependent).

## How to Fix It

**Solution 1: Use `BigInt` for large numbers**

```dart
void main() {
  BigInt large = BigInt.parse('9007199254740993');
  BigInt result = large * BigInt.from(2);
  print(result); // 18014398509481986
  
  // int has limited range
  // int overflow = 9007199254740993; // may lose precision
}
```

**Solution 2: Validate radix in `int.parse`**

```dart
void main() {
  // Valid radix: 2 to 36
  int binary = int.parse('1010', radix: 2);
  print(binary); // 10
  
  int hex = int.parse('FF', radix: 16);
  print(hex); // 255
  
  try {
    int bad = int.parse('10', radix: 37); // RangeError
  } on RangeError catch (e) {
    print('Radix must be between 2 and 36: $e');
  }
}
```

**Solution 3: Handle `toInt()` truncation explicitly**

```dart
void main() {
  double pi = 3.14159;
  
  print(pi.toInt());    // 3 (truncates, does not round)
  print(pi.round());    // 3
  print(pi.ceil());     // 4
  print(pi.floor());    // 3
}
```

**Solution 4: Safe `int.parse` with fallback**

```dart
void main() {
  String input = 'abc';
  
  int? value = int.tryParse(input);
  if (value != null) {
    print('Parsed: $value');
  } else {
    print('Invalid integer: $input');
  }
}
```

**Solution 5: Be aware of platform-dependent int size**

```dart
void main() {
  // On web, int is always 64-bit
  // On native, int is 64-bit on 64-bit platforms
  print('Max int: ${9223372036854775807}'); // 2^63 - 1
  
  // Use double for very large numbers if BigInt is too heavy
  double largeDouble = 1e18;
  print(largeDouble); // 1e+18
}
```

## Examples

`int.parse('0x1A')` throws a `FormatException` because the `0x` prefix is not recognized. Use `int.parse('1A', radix: 16)` instead. Similarly, `int.parse('10', radix: 1)` throws a `RangeError`.

## Related Errors

- [Dart Double Error](/languages/dart/dart-double-error/)
- [Dart Num Error](/languages/dart/dart-num-error/)
- [Dart Type Error](/languages/dart/dart-type-error/)
