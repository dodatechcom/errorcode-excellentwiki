---
title: "Flutter test - expectation failed"
description: "Flutter test fails when the test expectation does not match the actual widget behavior or output"
frameworks: ["flutter"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

A Flutter test expectation failure occurs when a `test()` or `testWidgets()` function encounters a mismatch between the expected and actual state. This is common when widget behavior changes but tests are not updated accordingly.

## Common Causes

- Widget output changed but test assertions not updated
- Async operations not properly awaited in tests
- Missing `pump` or `pumpAndSettle` after state changes
- Mock data does not match real data structure
- Widget tree rebuilds causing element count changes

## How to Fix

1. Use `pumpAndSettle` to wait for animations:

```dart
testWidgets('displays user name', (tester) async {
  await tester.pumpWidget(MaterialApp(home: UserProfile(name: 'John')));
  await tester.pumpAndSettle(); // wait for animations

  expect(find.text('John'), findsOneWidget);
});
```

2. Mock async operations properly:

```dart
testWidgets('loads data', (tester) async {
  when(mockApi.getData()).thenAnswer((_) async => {'name': 'Test'});

  await tester.pumpWidget(MaterialApp(home: DataScreen()));
  await tester.pumpAndSettle();

  expect(find.text('Test'), findsOneWidget);
});
```

3. Use proper matchers:

```dart
expect(find.byType(Text), findsNWidgets(3));
expect(find.textContaining('error'), findsNothing);
expect(find.byIcon(Icons.check), findsOneWidget);
```

4. Debug test failures with verbose output:

```bash
flutter test --reporter expanded
flutter test test/widget_test.dart --name "test name"
```

5. Check the full widget tree on failure:

```dart
testWidgets('debug test', (tester) async {
  await tester.pumpWidget(MaterialApp(home: MyWidget()));
  // Print widget tree for debugging
  debugDumpApp();
  expect(find.text('Expected'), findsOneWidget);
});
```

## Examples

```dart
// Error: Expected: exactly one matching node
// Found: zero matching nodes
testWidgets('counter increments', (tester) async {
  await tester.pumpWidget(MaterialApp(home: CounterScreen()));
  await tester.tap(find.byIcon(Icons.add));
  await tester.pump();
  expect(find.text('1'), findsOneWidget); // failed: still shows 0
});

// Fix: ensure state update
await tester.pump(); // re-render after state change
expect(find.text('1'), findsOneWidget);
```

## Related Errors

- [Testing Library error]({{< relref "/frameworks/react-native/rn-testing-library-error" >}})
- [Build error]({{< relref "/frameworks/flutter/flutter-build-error-v2" >}})
