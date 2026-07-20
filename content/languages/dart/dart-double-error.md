---
title: "[Solution] Dart Double Error — Precision, NaN, Infinity, parse Issues"
description: "Fix Dart double precision errors, isNaN/isInfinite checks, double.parse failures, and toStringAsFixed rounding."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 106
---

Double errors involve floating-point precision issues, unexpected `NaN` or `Infinity` values, and formatting problems with `toStringAsFixed`.

## Common Causes

1. Floating-point arithmetic producing `NaN` (e.g., `0/0`).
2. Division by zero producing `Infinity` instead of throwing.
3. `double.parse` failing on locale-specific number formats.
4. `toStringAsFixed` producing unexpected rounding.
5. Comparing doubles with `==` instead of epsilon-based comparison.

## How to Fix It

**Solution 1: Check for `NaN` and `Infinity`**

```dart
void main() {
  double result = 0.0 / 0.0;
  print(result.isNaN);     // true
  print(result.isInfinite); // false
  
  double inf = 1.0 / 0.0;
  print(inf.isInfinite);   // true
  print(inf.isNaN);        // false
  
  if (result.isNaN || result.isInfinite) {
    print('Invalid result');
  }
}
```

**Solution 2: Compare doubles with epsilon**

```dart
void main() {
  double a = 0.1 + 0.2;
  print(a == 0.3); // false!
  
  const double epsilon = 1e-10;
  bool isEqual = (a - 0.3).abs() < epsilon;
  print(isEqual); // true
}
```

**Solution 3: Use `toStringAsFixed` with rounding awareness**

```dart
void main() {
  double price = 1.005;
  
  // May not round as expected due to floating-point representation
  print(price.toStringAsFixed(2)); // "1.00" or "1.01" depending on platform
  
  // Safer approach using round
  double rounded = (price * 100).round() / 100;
  print(rounded.toStringAsFixed(2)); // "1.01"
}
```

**Solution 4: Parse doubles safely**

```dart
void main() {
  String input = '3.14';
  
  double? value = double.tryParse(input);
  if (value != null) {
    print('Parsed: $value');
  } else {
    print('Invalid double: $input');
  }
  
  // Note: double.parse('3,14') throws FormatException in some locales
}
```

**Solution 5: Use `remainder` and `truncateToDouble` for precision control**

```dart
void main() {
  double value = 7.89;
  
  print(value.truncateToDouble()); // 7.0
  print(value.remainder(1.0));     // 0.8900000000000001
  
  // Better precision with integer math
  int cents = (value * 100).round();
  print(cents); // 789
}
```

## Examples

`double.infinity / double.infinity` yields `NaN`, not `Infinity`. `double.parse('NaN')` returns `NaN` successfully. Always validate double values before using them in financial calculations.

## Related Errors

- [Dart Int Error](/languages/dart/dart-int-error/)
- [Dart Num Error](/languages/dart/dart-num-error/)
- [Dart String Concat Error](/languages/dart/dart-string-concat-error/)
