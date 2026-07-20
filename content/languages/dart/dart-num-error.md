---
title: "[Solution] Dart num Error — Type Check, int/double Coercion, compareTo"
description: "Fix Dart num type errors from int/double coercion, type checks, and compareTo misuse."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 107
---

`num` errors occur when code assumes a `num` is specifically an `int` or `double` without checking, or when `compareTo` is used incorrectly.

## Common Causes

1. Treating a `num` variable as `int` when it might be `double`.
2. JSON deserialization returning `double` where `int` is expected.
3. Using `==` instead of `compareTo` for sorting comparisons.
4. `num.parse` failing on scientific notation or unexpected formats.
5. Implicit `int` to `double` coercion causing precision loss.

## How to Fix It

**Solution 1: Check the runtime type of `num`**

```dart
void main() {
  num value = 3.14;
  
  if (value is int) {
    print('Integer: $value');
  } else if (value is double) {
    print('Double: $value');
  }
}
```

**Solution 2: Handle JSON number types**

```dart
import 'dart:convert';

void main() {
  String json = '{"count": 42, "price": 9.99}';
  Map<String, dynamic> data = jsonDecode(json);
  
  int count = (data['count'] as num).toInt();
  double price = (data['price'] as num).toDouble();
  
  print('Count: $count, Price: $price');
}
```

**Solution 3: Use `compareTo` for comparisons**

```dart
void main() {
  num a = 5;
  num b = 3.5;
  
  // Correct way to compare
  if (a.compareTo(b) > 0) {
    print('$a is greater than $b');
  }
  
  List<num> values = [3.14, 2, 5.0, 1];
  values.sort((a, b) => a.compareTo(b));
  print(values); // [1, 2, 3.14, 5.0]
}
```

**Solution 4: Convert safely between int and double**

```dart
void main() {
  num value = 7.9;
  
  // toInt truncates
  int asInt = value.toInt();
  print(asInt); // 7
  
  // round for nearest
  int rounded = value.round();
  print(rounded); // 8
  
  // To double is safe
  int intValue = 42;
  double asDouble = intValue.toDouble();
  print(asDouble); // 42.0
}
```

**Solution 5: Use `num.parse` with error handling**

```dart
void main() {
  List<String> inputs = ['42', '3.14', '1e10', '0xFF', 'abc'];
  
  for (String input in inputs) {
    num? value = num.tryParse(input);
    print('$input -> $value');
  }
}
```

## Examples

`num.parse('0xFF')` returns `255` as an `int`. `num.parse('1e10')` returns `10000000000.0` as a `double`. The runtime type of the `num` depends on the input format.

## Related Errors

- [Dart Int Error](/languages/dart/dart-int-error/)
- [Dart Double Error](/languages/dart/dart-double-error/)
- [Dart Type Error](/languages/dart/dart-type-error/)
