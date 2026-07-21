---
title: "[Solution] Flutter PageView Controller Error"
description: "Fix Flutter PageView controller errors when page indicator does not match or pages cannot be navigated programmatically."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A PageView controller error in Flutter occurs when the `PageController` is not synchronized with the `PageView`, causing the page indicator to show the wrong page or `animateToPage` to navigate to an unexpected position.

## Common Causes

- `PageController` not attached to the `PageView`
- `initialPage` on controller does not match the displayed page
- `PageController` disposed before `PageView` finishes building
- `onPageChanged` not updating the page indicator state
- `viewportFraction` causing partial page display issues

## How to Fix

1. Attach PageController and listen for changes:

```dart
class _CarouselState extends State<Carousel> {
  final PageController _controller = PageController();
  int _currentPage = 0;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Expanded(
          child: PageView(
            controller: _controller,
            onPageChanged: (index) {
              setState(() => _currentPage = index);
            },
            children: pages.map((page) => page).toList(),
          ),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: List.generate(pages.length, (index) {
            return GestureDetector(
              onTap: () => _controller.animateToPage(
                index,
                duration: const Duration(milliseconds: 300),
                curve: Curves.easeInOut,
              ),
              child: Container(
                margin: const EdgeInsets.symmetric(horizontal: 4),
                width: _currentPage == index ? 12 : 8,
                height: 8,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: _currentPage == index ? Colors.blue : Colors.grey,
                ),
              ),
            );
          }),
        ),
      ],
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }
}
```

2. Set initialPage correctly:

```dart
PageController controller = PageController(initialPage: 2); // Start at page 3

PageView(
  controller: controller,
  children: [Page1(), Page2(), Page3(), Page4()],
);
```

3. Use viewportFraction for partial pages:

```dart
PageController controller = PageController(viewportFraction: 0.8);

PageView(
  controller: controller,
  children: [
    Card(child: Center(child: Text('Page 1'))),
    Card(child: Center(child: Text('Page 2'))),
    Card(child: Center(child: Text('Page 3'))),
  ],
);
```

## Examples

```dart
// Bug: PageController created inside build
Widget build(BuildContext context) {
  return PageView(
    controller: PageController(), // New controller every rebuild
    children: [Page1(), Page2()],
  );
}

// Fixed: create in state
final _controller = PageController();

Widget build(BuildContext context) {
  return PageView(controller: _controller, children: [...]);
}
```

```text
PageController cannot be used with multiple PageView widgets
```
