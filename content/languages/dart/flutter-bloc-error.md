---
title: "[Solution] Flutter Bloc Error — add/emit, close, BlocProvider, BlocBuilder"
description: "Fix Flutter Bloc errors from event handling, state emission, disposal, and BlocProvider/BlocBuilder misuse."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 183
---

Bloc errors occur when events are added to a closed bloc, states are emitted incorrectly, or `BlocProvider` is misconfigured.

## Common Causes

1. Adding events to a bloc after `close()` has been called.
2. Not emitting states in the correct order.
3. `BlocProvider` not disposing the bloc.
4. `BlocBuilder` rebuilding on every state change without condition.
5. Missing `super.initial` in initial state.

## How to Fix It

**Solution 1: Create a proper Bloc**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

// Events
abstract class CounterEvent {}
class Increment extends CounterEvent {}
class Decrement extends CounterEvent {}

// Bloc
class CounterBloc extends Bloc<CounterEvent, int> {
  CounterBloc() : super(0) {
    on<Increment>((event, emit) => emit(state + 1));
    on<Decrement>((event, emit) => emit(state - 1));
  }
}

// Widget
class CounterPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (_) => CounterBloc(),
      child: Builder(
        builder: (context) {
          return Column(
            children: [
              BlocBuilder<CounterBloc, int>(
                builder: (context, count) {
                  return Text('Count: $count');
                },
              ),
              ElevatedButton(
                onPressed: () => context.read<CounterBloc>().add(Increment()),
                child: Text('+'),
              ),
              ElevatedButton(
                onPressed: () => context.read<CounterBloc>().add(Decrement()),
                child: Text('-'),
              ),
            ],
          );
        },
      ),
    );
  }
}
```

**Solution 2: Use BlocListener for side effects**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class MyBloc extends Bloc<String, String> {
  MyBloc() : super('initial') {
    on<String>((event, emit) => emit(event));
  }
}

class MyPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (_) => MyBloc(),
      child: BlocListener<MyBloc, String>(
        listener: (context, state) {
          if (state == 'error') {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Error occurred')),
            );
          }
        },
        child: Builder(
          builder: (context) {
            return ElevatedButton(
              onPressed: () => context.read<MyBloc>().add('error'),
              child: Text('Trigger Error'),
            );
          },
        ),
      ),
    );
  }
}
```

**Solution 3: Use conditional BlocBuilder**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class DataBloc extends Bloc<void, AsyncData> {
  DataBloc() : super(AsyncData.initial()) {
    on<void>((event, emit) async {
      emit(AsyncData.loading());
      try {
        final data = await fetchData();
        emit(AsyncData.loaded(data));
      } catch (e) {
        emit(AsyncData.error(e.toString()));
      }
    });
  }
  
  Future<String> fetchData() async {
    await Future.delayed(Duration(seconds: 1));
    return 'Loaded data';
  }
}

class AsyncData {
  final String status;
  final String? data;
  final String? error;
  
  AsyncData._({required this.status, this.data, this.error});
  
  factory AsyncData.initial() => AsyncData._(status: 'initial');
  factory AsyncData.loading() => AsyncData._(status: 'loading');
  factory AsyncData.loaded(String data) => AsyncData._(status: 'loaded', data: data);
  factory AsyncData.error(String error) => AsyncData._(status: 'error', error: error);
}

class DataWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocBuilder<DataBloc, AsyncData>(
      buildWhen: (prev, curr) => prev.status != curr.status,
      builder: (context, state) {
        switch (state.status) {
          case 'loading':
            return CircularProgressIndicator();
          case 'loaded':
            return Text(state.data ?? '');
          case 'error':
            return Text('Error: ${state.error}');
          default:
            return Text('Initial');
        }
      },
    );
  }
}
```

**Solution 4: Handle close properly**

```dart
import 'dart:async';
import 'package:flutter_bloc/flutter_bloc.dart';

class StreamBloc extends Bloc<String, String> {
  StreamSubscription? _subscription;
  
  StreamBloc() : super('') {
    on<String>((event, emit) {
      _subscription?.cancel();
      _subscription = Stream.periodic(Duration(seconds: 1), (i) => 'Tick $i')
          .listen((tick) => emit(tick));
    });
  }
  
  @override
  Future<void> close() {
    _subscription?.cancel();
    return super.close();
  }
}
```

**Solution 5: MultiBlocProvider for multiple blocs**

```dart
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

Widget build(BuildContext context) {
  return MultiBlocProvider(
    providers: [
      BlocProvider(create: (_) => CounterBloc()),
      BlocProvider(create: (_) => DataBloc()),
    ],
    child: MyApp(),
  );
}
```

## Examples

Add `flutter_bloc: ^8.1.0` to your `pubspec.yaml`. Blocs extend `Bloc<Event, State>` and use `on<Event>` to register handlers. Always close subscriptions in `close()`.

## Related Errors

- [Flutter Provider Error](/languages/dart/flutter-provider-error/)
- [Flutter Riverpod Error](/languages/dart/flutter-riverpod-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
