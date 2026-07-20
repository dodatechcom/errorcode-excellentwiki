---
title: "[Solution] Dart Isolate.exit/Isolate.run Error — Heavy Computation"
description: "Fix Dart Isolate.exit and Isolate.run errors from unsendable return values, computation failures, and resource limits."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 127
---

Isolate compute errors happen when `Isolate.run` or `Isolate.exit` receive values that cannot be sent between isolates, or when computations fail silently.

## Common Causes

1. Returning non-sendable objects from `Isolate.run`.
2. `Isolate.exit` called with a value that cannot be serialized.
3. Computation taking too long without cancellation support.
4. Memory pressure from spawning many isolates simultaneously.
5. Exceptions thrown inside isolates not being caught on the main side.

## How to Fix It

**Solution 1: Return sendable values from `Isolate.run`**

```dart
import 'dart:isolate';

void main() async {
  // Return primitive types or simple objects
  int result = await Isolate.run(() {
    return 42 * 42;
  });
  print(result); // 1764
  
  // Returns a Map — also sendable
  Map<String, int> stats = await Isolate.run(() {
    return {'min': 1, 'max': 100, 'avg': 50};
  });
  print(stats);
}
```

**Solution 2: Catch errors from isolate computation**

```dart
import 'dart:isolate';

void main() async {
  try {
    int result = await Isolate.run(() {
      throw Exception('Computation failed');
    });
  } catch (e) {
    print('Isolate error: $e');
  }
}
```

**Solution 3: Use `compute` from `package:flutter/foundation.dart` for Flutter**

```dart
import 'package:flutter/foundation.dart';

// Flutter's compute function wraps Isolate.run
int heavyComputation(int n) {
  int sum = 0;
  for (int i = 0; i < n; i++) {
    sum += i;
  }
  return sum;
}

// In Flutter:
// int result = await compute(heavyComputation, 1000000);
```

**Solution 4: Limit concurrent isolate usage**

```dart
import 'dart:isolate';

Future<List<int>> processInIsolates(List<int> data) async {
  // Process in batches to avoid memory pressure
  int batchSize = 10;
  List<int> results = [];
  
  for (int i = 0; i < data.length; i += batchSize) {
    List<int> batch = data.sublist(
      i,
      (i + batchSize).clamp(0, data.length),
    );
    
    List<int> batchResults = await Future.wait(
      batch.map((item) => Isolate.run(() => item * 2)),
    );
    
    results.addAll(batchResults);
  }
  
  return results;
}

void main() async {
  List<int> data = List.generate(100, (i) => i);
  List<int> results = await processInIsolates(data);
  print('Processed ${results.length} items');
}
```

**Solution 5: Send only serializable data**

```dart
import 'dart:isolate';
import 'dart:typed_data';

void main() async {
  // TypedData is sendable
  Uint8List result = await Isolate.run(() {
    return Uint8List.fromList([1, 2, 3, 4, 5]);
  });
  print(result); // [1, 2, 3, 4, 5]
}
```

## Examples

`Isolate.run` creates a new isolate, runs the computation, sends the result back, and terminates the isolate. It is designed for one-shot computations. For ongoing work, use `Isolate.spawn` with persistent communication.

## Related Errors

- [Dart Isolate Spawn Error](/languages/dart/dart-isolate-spawn-error/)
- [Dart Zone Error](/languages/dart/dart-zone-error/)
- [Dart FFI Error](/languages/dart/dart-ffi-error/)
