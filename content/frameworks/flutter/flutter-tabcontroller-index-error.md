---
title: "[Solution] Flutter TabController Index Error"
description: "Fix Flutter TabController index errors when the TabBar and TabBarView display mismatched content."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A TabController index error in Flutter occurs when the `TabBar` and `TabBarView` are not synchronized, causing the selected tab indicator to show one tab while the content shows another.

## Common Causes

- `TabController` length does not match the number of `Tab` widgets
- `TabBarView` children count does not match `TabController.length`
- `initialIndex` set to an invalid value
- `TabController` not disposed in `dispose()`
- Using `DefaultTabController` without specifying `length`

## How to Fix

1. Match TabController length with tabs and views:

```dart
class _HomeScreenState extends State<HomeScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        bottom: TabBar(
          controller: _tabController,
          tabs: const [
            Tab(icon: Icon(Icons.home), text: 'Home'),
            Tab(icon: Icon(Icons.search), text: 'Search'),
            Tab(icon: Icon(Icons.person), text: 'Profile'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: const [
          HomeTab(),
          SearchTab(),
          ProfileTab(),
        ],
      ),
    );
  }
}
```

2. Listen for tab changes:

```dart
_tabController.addListener(() {
  if (!_tabController.indexIsChanging) {
    print('Tab changed to ${_tabController.index}');
  }
});
```

3. Use `DefaultTabController` for simple cases:

```dart
DefaultTabController(
  length: 3,
  child: Scaffold(
    appBar: AppBar(
      bottom: const TabBar(
        tabs: [
          Tab(text: 'First'),
          Tab(text: 'Second'),
          Tab(text: 'Third'),
        ],
      ),
    ),
    body: const TabBarView(
      children: [
        Center(child: Text('First tab')),
        Center(child: Text('Second tab')),
        Center(child: Text('Third tab')),
      ],
    ),
  ),
);
```

## Examples

```dart
// Bug: TabBarView has 2 children but TabController has 3 tabs
TabController(length: 3, vsync: this);
TabBarView(children: [WidgetA(), WidgetB()]); // Missing third view

// Fixed: match counts
TabBarView(children: [WidgetA(), WidgetB(), WidgetC()]);
```

```text
TabController.length (3) does not match TabBarView.children.length (2).
```
