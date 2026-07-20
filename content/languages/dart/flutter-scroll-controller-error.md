---
title: "[Solution] Flutter ScrollController Error — jumpTo, animateTo, position"
description: "Fix Flutter ScrollController errors from jumpTo, animateTo, position access, and disposal issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 159
---

ScrollController errors occur when accessing scroll position before it is attached, calling methods after disposal, or using incompatible scroll controllers.

## Common Causes

1. Accessing `controller.position` when no scrollable is attached.
2. Calling `jumpTo` or `animateTo` after the controller is disposed.
3. Using the same `ScrollController` for multiple scrollables.
4. `animateTo` with duration `Duration.zero`.
5. Not handling `NotificationListener` for scroll events.

## How to Fix It

**Solution 1: Use ScrollController safely**

```dart
import 'package:flutter/material.dart';

class ScrollableList extends StatefulWidget {
  @override
  State<ScrollableList> createState() => _ScrollableListState();
}

class _ScrollableListState extends State<ScrollableList> {
  final ScrollController _controller = ScrollController();
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  void _scrollToTop() {
    if (_controller.hasClients) {
      _controller.jumpTo(0);
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ElevatedButton(
          onPressed: _scrollToTop,
          child: Text('Scroll to Top'),
        ),
        Expanded(
          child: ListView.builder(
            controller: _controller,
            itemCount: 100,
            itemBuilder: (context, index) => ListTile(
              title: Text('Item $index'),
            ),
          ),
        ),
      ],
    );
  }
}
```

**Solution 2: Animate to position**

```dart
import 'package:flutter/material.dart';

class AnimatedScroll extends StatefulWidget {
  @override
  State<AnimatedScroll> createState() => _AnimatedScrollState();
}

class _AnimatedScrollState extends State<AnimatedScroll> {
  final ScrollController _controller = ScrollController();
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  void _animateToBottom() {
    if (_controller.hasClients) {
      _controller.animateTo(
        _controller.position.maxScrollExtent,
        duration: Duration(milliseconds: 500),
        curve: Curves.easeOut,
      );
    }
  }
  
  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      controller: _controller,
      itemCount: 50,
      itemBuilder: (context, index) => ListTile(title: Text('$index')),
    );
  }
}
```

**Solution 3: Listen to scroll position**

```dart
import 'package:flutter/material.dart';

class ScrollListener extends StatefulWidget {
  @override
  State<ScrollListener> createState() => _ScrollListenerState();
}

class _ScrollListenerState extends State<ScrollListener> {
  final ScrollController _controller = ScrollController();
  
  @override
  void initState() {
    super.initState();
    _controller.addListener(_onScroll);
  }
  
  void _onScroll() {
    if (_controller.position.pixels >=
        _controller.position.maxScrollExtent - 200) {
      print('Near bottom — load more');
    }
  }
  
  @override
  void dispose() {
    _controller.removeListener(_onScroll);
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      controller: _controller,
      itemCount: 100,
      itemBuilder: (context, index) => ListTile(title: Text('$index')),
    );
  }
}
```

**Solution 4: Scroll to specific item**

```dart
import 'package:flutter/material.dart';

class ItemScroller extends StatefulWidget {
  @override
  State<ItemScroller> createState() => _ItemScrollerState();
}

class _ItemScrollerState extends State<ItemScroller> {
  final ScrollController _controller = ScrollController();
  
  void _scrollToItem(int index) {
    // Assuming fixed item height of 56
    double targetOffset = index * 56.0;
    
    if (_controller.hasClients) {
      _controller.animateTo(
        targetOffset,
        duration: Duration(milliseconds: 300),
        curve: Curves.easeInOut,
      );
    }
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      controller: _controller,
      itemCount: 100,
      itemBuilder: (context, index) => SizedBox(
        height: 56,
        child: ListTile(
          title: Text('Item $index'),
          onTap: () => _scrollToItem(index + 5),
        ),
      ),
    );
  }
}
```

**Solution 5: Keep scroll offset in state**

```dart
import 'package:flutter/material.dart';

class PersistentScroll extends StatefulWidget {
  @override
  State<PersistentScroll> createState() => _PersistentScrollState();
}

class _PersistentScrollState extends State<PersistentScroll> {
  final ScrollController _controller = ScrollController(
    initialScrollOffset: 0,
  );
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      controller: _controller,
      itemCount: 100,
      itemBuilder: (context, index) => ListTile(title: Text('$index')),
    );
  }
}
```

## Examples

`ScrollController.hasClients` returns `true` when at least one scrollable is attached. Always check this before accessing `position`. Multiple scrollables cannot share the same controller.

## Related Errors

- [Flutter List View Error](/languages/dart/flutter-list-view-error/)
- [Flutter Custom Scroll Error](/languages/dart/flutter-custom-scroll-error/)
- [Flutter Animation Controller Error](/languages/dart/flutter-animation-controller-error/)
