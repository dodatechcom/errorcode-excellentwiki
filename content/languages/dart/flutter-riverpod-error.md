---
title: "[Solution] Flutter Riverpod Error — ref.watch, ref.read, provider override, autoDispose"
description: "Fix Flutter Riverpod errors from ref.watch/ref.read misuse, provider override issues, and autoDispose lifecycle."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 182
---

Riverpod errors occur when providers are accessed incorrectly, overrides are misconfigured, or autoDispose providers are not handled properly.

## Common Causes

1. `ref.watch` used outside of `build()` or `Consumer` callback.
2. `ref.read` used where `ref.watch` is needed for reactivity.
3. Provider override not matching the provider type.
4. `autoDispose` provider cleaned up prematurely.
5. Missing `ProviderScope` at the app root.

## How to Fix It

**Solution 1: Use ref.watch and ref.read correctly**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final counterProvider = StateNotifierProvider<CounterNotifier, int>((ref) {
  return CounterNotifier();
});

class CounterNotifier extends StateNotifier<int> {
  CounterNotifier() : super(0);
  
  void increment() => state++;
  void decrement() => state--;
}

class CounterPage extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // watch — rebuilds when state changes
    int count = ref.watch(counterProvider);
    
    return Column(
      children: [
        Text('Count: $count'),
        ElevatedButton(
          onPressed: () {
            // read — one-time access
            ref.read(counterProvider.notifier).increment();
          },
          child: Text('+'),
        ),
      ],
    );
  }
}

void main() {
  runApp(ProviderScope(child: MyApp()));
}
```

**Solution 2: Use Consumer for scoped watches**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final nameProvider = StateProvider<String>((ref) => 'Guest');

class NameWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Consumer(
      builder: (context, ref, child) {
        String name = ref.watch(nameProvider);
        return Text('Hello, $name!');
      },
    );
  }
}
```

**Solution 3: Use autoDispose correctly**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final autoProvider = FutureProvider.autoDispose<String>((ref) async {
  ref.onDispose(() {
    print('Provider disposed');
  });
  
  await Future.delayed(Duration(seconds: 1));
  return 'Loaded data';
});

class AutoDisposeWidget extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    AsyncValue<String> data = ref.watch(autoProvider);
    
    return data.when(
      loading: () => CircularProgressIndicator(),
      error: (e, s) => Text('Error: $e'),
      data: (value) => Text(value),
    );
  }
}
```

**Solution 4: Override providers for testing**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final apiProvider = Provider<ApiClient>((ref) => ApiClient());

class ApiClient {
  Future<String> fetchData() async => 'Real data';
}

class MyWidget extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final api = ref.watch(apiProvider);
    return FutureBuilder(
      future: api.fetchData(),
      builder: (context, snapshot) => Text('${snapshot.data}'),
    );
  }
}

// In tests:
// ProviderScope(
//   overrides: [
//     apiProvider.overrideWithValue(MockApiClient()),
//   ],
//   child: MyWidget(),
// )
```

**Solution 5: Use state provider for simple state**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

final searchProvider = StateProvider<String>((ref) => '');

class SearchWidget extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    String query = ref.watch(searchProvider);
    
    return Column(
      children: [
        TextField(
          onChanged: (value) {
            ref.read(searchProvider.notifier).state = value;
          },
          decoration: InputDecoration(hintText: 'Search...'),
        ),
        Text('Searching for: $query'),
      ],
    );
  }
}
```

## Examples

`ref.watch` can only be called inside `build()` or `Consumer`'s builder. `ref.read` can be called anywhere but does not trigger rebuilds.

## Related Errors

- [Flutter Provider Error](/languages/dart/flutter-provider-error/)
- [Flutter Bloc Error](/languages/dart/flutter-bloc-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
