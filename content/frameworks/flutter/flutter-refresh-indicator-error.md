---
title: "[Solution] Flutter RefreshIndicator Error"
description: "Fix Flutter RefreshIndicator errors when pull-to-refresh does not trigger or throws scroll errors."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A RefreshIndicator error in Flutter occurs when the pull-to-refresh gesture does not work or throws an error because the scrollable child does not have sufficient scroll distance or the refresh callback does not complete properly.

## Common Causes

- Scrollable child does not have enough content to scroll
- `RefreshIndicator` wrapped around a non-scrollable widget
- `onRefresh` Future does not complete
- `notificationPredicate` filters out scroll notifications
- `RefreshIndicator` used with `NeverScrollableScrollPhysics`

## How to Fix

1. Ensure the scrollable child has enough content:

```dart
RefreshIndicator(
  onRefresh: () async {
    await fetchData();
    setState(() {});
  },
  child: ListView.builder(
    itemCount: items.length,
    itemBuilder: (context, index) => ListTile(title: Text(items[index].name)),
  ),
);
```

2. Use `AlwaysScrollableScrollPhysics` to allow pull even with few items:

```dart
RefreshIndicator(
  onRefresh: fetchItems,
  child: ListView(
    physics: const AlwaysScrollableScrollPhysics(),
    children: items.isEmpty
      ? [const Center(child: Text('No items'))]
      : items.map((item) => ListTile(title: Text(item.name))).toList(),
  ),
);
```

3. Complete the Future properly:

```dart
Future<void> _refreshData() async {
  try {
    final newData = await api.fetchItems();
    setState(() {
      items = newData;
    });
  } catch (e) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text('Refresh failed: $e')),
    );
  }
  // Future must complete -- do not return early without completing
}
```

## Examples

```dart
// Bug: RefreshIndicator around non-scrollable Column
RefreshIndicator(
  onRefresh: _refresh,
  child: Column( // Not scrollable -- pull gesture ignored
    children: [Text('Hello'), Text('World')],
  ),
);

// Fixed: use ListView
RefreshIndicator(
  onRefresh: _refresh,
  child: ListView(
    children: [Text('Hello'), Text('World')],
  ),
);
```

```text
RefreshIndicator requires a scrollable child widget.
```
