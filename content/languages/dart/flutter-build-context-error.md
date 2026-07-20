---
title: "[Solution] Flutter BuildContext Error — Use After Mount, mounted Check"
description: "Fix Flutter BuildContext errors from using context after dispose, missing mounted checks, and lifecycle issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 152
---

BuildContext errors occur when context is accessed after the widget is unmounted, or when async operations complete after disposal.

## Common Causes

1. Using `context` after `dispose()` in async callbacks.
2. Not checking `mounted` before calling `setState`.
3. Accessing `InheritedWidget` with a stale context.
4. Using `Navigator.of(context)` on a disposed widget.
5. `BuildContext` passed to `showDialog` from an inactive route.

## How to Fix It

**Solution 1: Check mounted before setState**

```dart
import 'package:flutter/material.dart';

class MyWidget extends StatefulWidget {
  @override
  State<MyWidget> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  String data = '';
  
  @override
  void initState() {
    super.initState();
    fetchData();
  }
  
  Future<void> fetchData() async {
    final result = await someAsyncOperation();
    
    if (!mounted) return; // Check before setState
    
    setState(() {
      data = result;
    });
  }
  
  Future<String> someAsyncOperation() async {
    await Future.delayed(Duration(seconds: 2));
    return 'Loaded data';
  }
  
  @override
  Widget build(BuildContext context) {
    return Text(data);
  }
}
```

**Solution 2: Store context safely for async operations**

```dart
import 'package:flutter/material.dart';

class MyWidget extends StatefulWidget {
  @override
  State<MyWidget> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () async {
        // Capture context reference
        final navigator = Navigator.of(context);
        final scaffold = ScaffoldMessenger.of(context);
        
        await Future.delayed(Duration(seconds: 2));
        
        // Verify mounted before using captured context
        if (!mounted) return;
        
        scaffold.showSnackBar(SnackBar(content: Text('Done!')));
        navigator.push(MaterialPageRoute(builder: (_) => NextPage()));
      },
      child: Text('Go'),
    );
  }
}

class NextPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(body: Text('Next'));
}
```

**Solution 3: Use Builder for late context access**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return Builder(
    builder: (BuildContext innerContext) {
      return ElevatedButton(
        onPressed: () {
          // innerContext is guaranteed to be valid here
          ScaffoldMessenger.of(innerContext).showSnackBar(
            SnackBar(content: Text('Hello!')),
          );
        },
        child: Text('Show SnackBar'),
      );
    },
  );
}
```

**Solution 4: Handle context in callbacks safely**

```dart
import 'package:flutter/material.dart';

class MyWidget extends StatefulWidget {
  @override
  State<MyWidget> createState() => _MyWidgetState();
}

class _MyWidgetState extends State<MyWidget> {
  @override
  Widget build(BuildContext context) {
    return StreamBuilder<int>(
      stream: _getStream(),
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Text('${snapshot.data}');
        }
        return CircularProgressIndicator();
      },
    );
  }
  
  Stream<int> _getStream() async* {
    for (int i = 0; i < 5; i++) {
      await Future.delayed(Duration(seconds: 1));
      yield i;
    }
  }
}
```

**Solution 5: Use context.read/watch for Provider safely**

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class MyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // read is safe in callbacks (not in build)
    return ElevatedButton(
      onPressed: () {
        final provider = context.read<MyData>();
        provider.update();
      },
      child: Text('Update'),
    );
  }
}
```

## Examples

A `BuildContext` is a reference to a widget's location in the tree. After a widget is disposed, its context is no longer valid. Always check `mounted` before using context in async callbacks.

## Related Errors

- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
- [Flutter Inherited Widget Error](/languages/dart/flutter-inherited-widget-error/)
- [Flutter Navigator Pop Error](/languages/dart/flutter-navigator-pop-error/)
