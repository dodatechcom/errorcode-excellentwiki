---
title: "[Solution] Dart Duration Error — Constructor, inDays, Comparison, Arithmetic"
description: "Fix Dart Duration errors from constructor misuse, unit conversion confusion, arithmetic operations, and comparison."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 113
---

Duration errors arise from misunderstanding how `Duration` stores time internally, misusing unit conversion getters, or performing invalid arithmetic.

## Common Causes

1. Assuming `inDays` returns fractional days — it truncates.
2. Using `Duration(hours: 25)` and expecting `inDays` to return 1.
3. Adding or subtracting `Duration` from `DateTime` incorrectly.
4. Comparing `Duration` objects with `==` when they have different internal representations.
5. Negative durations causing unexpected `inHours`/`inDays` results.

## How to Fix It

**Solution 1: Understand `Duration` storage and getters**

```dart
void main() {
  Duration d = Duration(hours: 25);
  
  print(d.inHours);  // 25 (total hours)
  print(d.inMinutes); // 1500 (total minutes)
  print(d.inSeconds); // 90000
  print(d.inDays);   // 1 (truncated, not 1.04)
  
  // For fractional values, calculate manually
  double daysFraction = d.inMinutes / (24 * 60);
  print(daysFraction.toStringAsFixed(2)); // 1.04
}
```

**Solution 2: Use `Duration` arithmetic correctly**

```dart
void main() {
  Duration a = Duration(hours: 2);
  Duration b = Duration(minutes: 30);
  
  Duration sum = a + b;
  print(sum); // 2:30:00.000000
  
  Duration diff = a - b;
  print(diff); // 1:30:00.000000
  
  Duration scaled = a * 3;
  print(scaled); // 6:00:00.000000
}
```

**Solution 3: Compare durations with `compareTo`**

```dart
void main() {
  Duration fast = Duration(seconds: 5);
  Duration slow = Duration(seconds: 10);
  
  // Use compareTo for ordering
  print(fast.compareTo(slow)); // -1 (fast < slow)
  
  // == works too since Duration overrides it
  print(fast == Duration(seconds: 5)); // true
  
  // For sorting
  List<Duration> times = [slow, fast, Duration(minutes: 1)];
  times.sort((a, b) => a.compareTo(b));
  print(times); // [0:00:05.000000, 0:00:10.000000, 0:01:00.000000]
}
```

**Solution 4: Apply Duration to DateTime correctly**

```dart
void main() {
  DateTime now = DateTime.now();
  
  DateTime later = now.add(Duration(hours: 2));
  DateTime earlier = now.subtract(Duration(minutes: 30));
  
  print('Now: $now');
  print('Later: $later');
  print('Earlier: $earlier');
  
  Duration elapsed = later.difference(earlier);
  print('Elapsed: ${elapsed.inMinutes} minutes'); // 150
}
```

**Solution 5: Use named constructors for clarity**

```dart
void main() {
  Duration ms = Duration(milliseconds: 500);
  Duration sec = Duration(seconds: 30);
  Duration min = Duration(minutes: 5);
  Duration hr = Duration(hours: 1);
  Duration days = Duration(days: 7);
  
  print('${ms.inMilliseconds}ms');
  print('${sec.inSeconds}s');
  print('${min.inMinutes}min');
  print('${hr.inHours}hr');
  print('${days.inDays}days');
}
```

## Examples

`Duration(days: -1).inHours` returns `-24`, not a negative fractional value. Always use `.abs()` if you need the magnitude of a duration.

## Related Errors

- [Dart Date Time Error](/languages/dart/dart-date-time-error/)
- [Dart Int Error](/languages/dart/dart-int-error/)
- [Dart Num Error](/languages/dart/dart-num-error/)
