---
title: "[Solution] Flutter Checkbox Group Error"
description: "Fix Flutter checkbox group errors when multiple checkboxes do not maintain correct selection state."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A checkbox group error in Flutter occurs when multiple `Checkbox` widgets do not correctly track their individual selection states, causing incorrect visual display or missing selections when the user interacts with the group.

## Common Causes

- Single boolean variable shared across all checkboxes
- `onChanged` callback does not update the correct item
- `value` property not derived from the selected items list
- State not rebuilt after checkbox toggle
- Checkbox widget does not use the `key` property for list items

## How to Fix

1. Use a list to track selected items:

```dart
class _CheckboxGroupState extends State<CheckboxGroup> {
  final List<String> _selectedItems = [];

  @override
  Widget build(BuildContext context) {
    final items = ['Read', 'Write', 'Execute', 'Admin'];

    return Column(
      children: items.map((item) {
        return CheckboxListTile(
          title: Text(item),
          value: _selectedItems.contains(item),
          onChanged: (bool? checked) {
            setState(() {
              if (checked == true) {
                _selectedItems.add(item);
              } else {
                _selectedItems.remove(item);
              }
            });
          },
        );
      }).toList(),
    );
  }
}
```

2. Use a `Set` for faster lookups:

```dart
final Set<String> _permissions = {};

CheckboxListTile(
  title: Text('Read'),
  value: _permissions.contains('read'),
  onChanged: (checked) {
    setState(() {
      if (checked == true) {
        _permissions.add('read');
      } else {
        _permissions.remove('read');
      }
    });
  },
);
```

3. Create a reusable checkbox group widget:

```dart
class CheckboxGroup extends StatefulWidget {
  final List<String> options;
  final List<String> initialSelected;
  final ValueChanged<List<String>> onChanged;

  const CheckboxGroup({
    required this.options,
    required this.initialSelected,
    required this.onChanged,
  });

  @override
  State<CheckboxGroup> createState() => _CheckboxGroupState();
}

class _CheckboxGroupState extends State<CheckboxGroup> {
  late Set<String> _selected;

  @override
  void initState() {
    super.initState();
    _selected = Set.from(widget.initialSelected);
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: widget.options.map((option) {
        return CheckboxListTile(
          title: Text(option),
          value: _selected.contains(option),
          onChanged: (checked) {
            setState(() {
              checked == true ? _selected.add(option) : _selected.remove(option);
            });
            widget.onChanged(_selected.toList());
          },
        );
      }).toList(),
    );
  }
}
```

## Examples

```dart
// Bug: single bool for all checkboxes
bool _selectAll = false;

Checkbox(value: _selectAll, onChanged: (v) => setState(() => _selectAll = v!));
Checkbox(value: _selectAll, onChanged: (v) => setState(() => _selectAll = v!));
// Both checkboxes always show the same value

// Fixed: track each item separately
final Map<String, bool> _checks = {'A': false, 'B': false};

Column(
  children: _checks.entries.map((entry) {
    return Checkbox(
      value: entry.value,
      onChanged: (v) => setState(() => _checks[entry.key] = v ?? false),
    );
  }).toList(),
);
```

```text
Checkbox value must be either true, false, or null
```
