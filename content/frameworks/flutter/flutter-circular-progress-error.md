---
title: "[Solution] Flutter CircularProgressIndicator Error"
description: "Fix Flutter CircularProgressIndicator errors when the loading indicator does not display or fills the entire screen."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A CircularProgressIndicator error in Flutter occurs when the loading indicator is not centered, expands to fill all available space, or does not appear because the Future completes synchronously before the widget renders.

## Common Causes

- `CircularProgressIndicator` without parent `Center` widget
- Indicator inside `Expanded` or `Flexible` taking all available space
- Future completes before first frame renders
- `isLoading` state not set to true before async operation
- `SizedBox` or `Container` wrapping indicator has zero dimensions

## How to Fix

1. Center the indicator properly:

```dart
if (_isLoading)
  const Center(
    child: Padding(
      padding: EdgeInsets.all(16),
      child: CircularProgressIndicator(),
    ),
  )
```

2. Constrain the indicator size:

```dart
const SizedBox(
  width: 48,
  height: 48,
  child: CircularProgressIndicator(strokeWidth: 4),
);
```

3. Show loading state correctly:

```dart
class _DataState extends State<DataScreen> {
  bool _isLoading = true;
  List<Item> _items = [];

  @override
  void initState() {
    super.initState();
    _loadData();
  }

  Future<void> _loadData() async {
    setState(() => _isLoading = true);
    try {
      final items = await api.fetchItems();
      setState(() {
        _items = items;
        _isLoading = false;
      });
    } catch (e) {
      setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const Scaffold(
        body: Center(child: CircularProgressIndicator()),
      );
    }

    return Scaffold(
      body: ListView.builder(
        itemCount: _items.length,
        itemBuilder: (context, index) => ListTile(title: Text(_items[index].name)),
      ),
    );
  }
}
```

## Examples

```dart
// Bug: CircularProgressIndicator without Center
Column(
  children: [
    CircularProgressIndicator(), // Expands to full width
  ],
);

// Fixed: center and constrain
Center(
  child: SizedBox(
    width: 48,
    height: 48,
    child: CircularProgressIndicator(),
  ),
);
```

```text
Incorrect use of ParentDataWidget: Expanded widgets must be placed inside Flex widgets
```
