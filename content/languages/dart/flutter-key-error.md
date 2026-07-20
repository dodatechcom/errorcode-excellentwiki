---
title: "[Solution] Flutter Key Error — GlobalKey, UniqueKey, ValueKey, ObjectKey"
description: "Fix Flutter widget key errors from GlobalKey misuse, duplicate keys, ValueKey collisions, and key type selection."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 151
---

Key errors occur when widgets have duplicate keys, GlobalKey is used incorrectly, or the wrong key type is chosen for the use case.

## Common Causes

1. Duplicate `ValueKey` values within the same parent widget.
2. `GlobalKey` used without registering or with incorrect type.
3. Using `ObjectKey` with non-unique objects.
4. Keys not being stable across rebuilds.
5. Removing `UniqueKey` causing the widget to be recreated unnecessarily.

## How to Fix It

**Solution 1: Use UniqueKey for unique widget identity**

```dart
import 'package:flutter/material.dart';

class DynamicList extends StatefulWidget {
  @override
  State<DynamicList> createState() => _DynamicListState();
}

class _DynamicListState extends State<DynamicList> {
  List<String> items = ['A', 'B', 'C'];
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: items.map((item) => ListTile(
        key: UniqueKey(),
        title: Text(item),
      )).toList(),
    );
  }
}
```

**Solution 2: Use ValueKey for keyed items**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  List<Map<String, String>> users = [
    {'id': '1', 'name': 'Alice'},
    {'id': '2', 'name': 'Bob'},
    {'id': '3', 'name': 'Charlie'},
  ];
  
  return ListView.builder(
    itemCount: users.length,
    itemBuilder: (context, index) => ListTile(
      key: ValueKey(users[index]['id']),
      title: Text(users[index]['name']!),
    ),
  );
}
```

**Solution 3: Avoid duplicate keys**

```dart
import 'package:flutter/material.dart';

// Wrong: duplicate keys
Widget wrongKeys() {
  return Column(
    children: [
      Text('Item 1', key: ValueKey('same')),
      Text('Item 2', key: ValueKey('same')), // Error: duplicate key
    ],
  );
}

// Correct: unique keys
Widget correctKeys() {
  return Column(
    children: [
      Text('Item 1', key: ValueKey('item-1')),
      Text('Item 2', key: ValueKey('item-2')),
    ],
  );
}
```

**Solution 4: Use GlobalKey for cross-widget access**

```dart
import 'package:flutter/material.dart';

class ParentWidget extends StatefulWidget {
  @override
  State<ParentWidget> createState() => _ParentWidgetState();
}

class _ParentWidgetState extends State<ParentWidget> {
  final GlobalKey<ChildWidgetState> childKey = GlobalKey<ChildWidgetState>();
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ChildWidget(key: childKey),
        ElevatedButton(
          onPressed: () {
            childKey.currentState?.doSomething();
          },
          child: Text('Call Child'),
        ),
      ],
    );
  }
}

class ChildWidget extends StatefulWidget {
  const ChildWidget({super.key});
  
  @override
  State<ChildWidget> createState() => ChildWidgetState();
}

class ChildWidgetState extends State<ChildWidget> {
  void doSomething() {
    print('Child was called!');
  }
  
  @override
  Widget build(BuildContext context) => Text('Child');
}
```

**Solution 5: Choose the right key type**

```dart
import 'package:flutter/material.dart';

// ValueKey — for items with unique IDs
// ValueKey('user-123')

// UniqueKey — for temporary unique identity
// UniqueKey()

// ObjectKey — for objects with identity semantics
// ObjectKey(myObject)

// GlobalKey — for accessing state across the tree
// GlobalKey<SomeState>()
```

## Examples

Keys help Flutter identify which widgets have changed, been added, or removed. Without keys in lists, Flutter may reuse the wrong widget state during reordering.

## Related Errors

- [Flutter Widget Const Error](/languages/dart/flutter-widget-const-error/)
- [Flutter Build Context Error](/languages/dart/flutter-build-context-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
