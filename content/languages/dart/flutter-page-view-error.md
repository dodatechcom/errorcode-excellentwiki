---
title: "[Solution] Flutter PageView Error — initialPage, viewportFraction, animateToPage"
description: "Fix Flutter PageView errors from PageController configuration, viewportFraction, animateToPage, and page tracking."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 174
---

PageView errors occur when `PageController` is misconfigured, `viewportFraction` causes layout issues, or page navigation methods are called incorrectly.

## Common Causes

1. `PageController` not being disposed.
2. `initialPage` out of range.
3. `viewportFraction` greater than 1 or negative.
4. `animateToPage` called without checking bounds.
5. Multiple `PageView` widgets sharing a controller.

## How to Fix It

**Solution 1: Basic PageView**

```dart
import 'package:flutter/material.dart';

class SimplePageView extends StatefulWidget {
  @override
  State<SimplePageView> createState() => _SimplePageViewState();
}

class _SimplePageViewState extends State<SimplePageView> {
  final PageController _controller = PageController();
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return PageView(
      controller: _controller,
      children: [
        Container(color: Colors.red, child: Center(child: Text('Page 1'))),
        Container(color: Colors.green, child: Center(child: Text('Page 2'))),
        Container(color: Colors.blue, child: Center(child: Text('Page 3'))),
      ],
    );
  }
}
```

**Solution 2: Use viewportFraction for peek effect**

```dart
import 'package:flutter/material.dart';

Widget build(BuildContext context) {
  return PageView(
    controller: PageController(viewportFraction: 0.8),
    children: List.generate(5, (index) {
      return Padding(
        padding: EdgeInsets.all(8),
        child: Card(
          child: Center(child: Text('Card ${index + 1}')),
        ),
      );
    }),
  );
}
```

**Solution 3: Track current page**

```dart
import 'package:flutter/material.dart';

class TrackedPageView extends StatefulWidget {
  @override
  State<TrackedPageView> createState() => _TrackedPageViewState();
}

class _TrackedPageViewState extends State<TrackedPageView> {
  final PageController _controller = PageController();
  int _currentPage = 0;
  
  @override
  void initState() {
    super.initState();
    _controller.addListener(() {
      int page = _controller.page?.round() ?? 0;
      if (page != _currentPage) {
        setState(() => _currentPage = page);
      }
    });
  }
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Expanded(
          child: PageView(
            controller: _controller,
            children: List.generate(5, (i) =>
              Center(child: Text('Page ${i + 1}'))
            ),
          ),
        ),
        Text('Current page: ${_currentPage + 1}'),
      ],
    );
  }
}
```

**Solution 4: Navigate programmatically**

```dart
import 'package:flutter/material.dart';

class NavigateablePageView extends StatefulWidget {
  @override
  State<NavigateablePageView> createState() => _NavigateablePageViewState();
}

class _NavigateablePageViewState extends State<NavigateablePageView> {
  final PageController _controller = PageController(initialPage: 0);
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Expanded(
          child: PageView(
            controller: _controller,
            children: List.generate(5, (i) =>
              Center(child: Text('Page ${i + 1}'))
            ),
          ),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () => _controller.previousPage(
                duration: Duration(milliseconds: 300),
                curve: Curves.easeInOut,
              ),
              child: Text('Previous'),
            ),
            SizedBox(width: 16),
            ElevatedButton(
              onPressed: () => _controller.nextPage(
                duration: Duration(milliseconds: 300),
                curve: Curves.easeInOut,
              ),
              child: Text('Next'),
            ),
          ],
        ),
      ],
    );
  }
}
```

**Solution 5: Page indicator dots**

```dart
import 'package:flutter/material.dart';

class PageIndicator extends StatefulWidget {
  @override
  State<PageIndicator> createState() => _PageIndicatorState();
}

class _PageIndicatorState extends State<PageIndicator> {
  final PageController _controller = PageController();
  int _count = 5;
  
  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Expanded(
          child: PageView.builder(
            controller: _controller,
            itemCount: _count,
            itemBuilder: (context, index) =>
              Center(child: Text('Page ${index + 1}')),
          ),
        ),
        ListenableBuilder(
          listenable: _controller,
          builder: (context, _) {
            int page = _controller.page?.round() ?? 0;
            return Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: List.generate(_count, (i) {
                return Container(
                  margin: EdgeInsets.all(4),
                  width: i == page ? 12 : 8,
                  height: i == page ? 12 : 8,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: i == page ? Colors.blue : Colors.grey,
                  ),
                );
              }),
            );
          },
        ),
      ],
    );
  }
}
```

## Examples

`PageController(viewportFraction: 0.8)` shows 80% of each page, allowing the adjacent pages to peek. `jumpTo` changes pages without animation; `animateToPage` provides smooth transitions.

## Related Errors

- [Flutter Tab Bar Error](/languages/dart/flutter-tab-bar-error/)
- [Flutter Scroll Controller Error](/languages/dart/flutter-scroll-controller-error/)
- [Flutter Animation Controller Error](/languages/dart/flutter-animation-controller-error/)
