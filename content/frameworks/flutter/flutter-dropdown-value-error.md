---
title: "[Solution] Flutter Dropdown Button Value Error"
description: "Fix Flutter DropdownButton errors when the selected value does not match any item or causes a render error."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A DropdownButton value error in Flutter occurs when the `value` property does not match any of the `DropdownMenuItem` values, causing a "RenderFlex" error or blank dropdown.

## Common Causes

- `value` is set to an item not in the items list
- Items list is empty when the dropdown renders
- `value` type does not match the items type
- `onChanged` callback does not update state with the new value
- Duplicate values in the items list

## How to Fix

1. Ensure value matches an item in the list:

```dart
String? _selectedValue;

DropdownButton<String>(
  value: _selectedValue,
  hint: const Text('Select an option'),
  items: const [
    DropdownMenuItem(value: 'option1', child: Text('Option 1')),
    DropdownMenuItem(value: 'option2', child: Text('Option 2')),
    DropdownMenuItem(value: 'option3', child: Text('Option 3')),
  ],
  onChanged: (newValue) {
    setState(() => _selectedValue = newValue);
  },
);
```

2. Use nullable value with a hint for unselected state:

```dart
String? _selectedCity;

DropdownButton<String>(
  value: _selectedCity,
  isExpanded: true,
  hint: const Text('Choose a city'),
  items: cities.map((city) => DropdownMenuItem(
    value: city,
    child: Text(city),
  )).toList(),
  onChanged: (value) {
    if (value != null) {
      setState(() => _selectedCity = value);
    }
  },
);
```

3. Validate before setting value:

```dart
void updateDropdown(String newValue) {
  if (availableOptions.contains(newValue)) {
    setState(() => _selectedValue = newValue);
  }
  // Ignore invalid values
}
```

## Examples

```dart
// Bug: value not in items list
String _selected = 'nonexistent';

DropdownButton<String>(
  value: _selected, // Error: value not in items
  items: [
    DropdownMenuItem(value: 'a', child: Text('A')),
    DropdownMenuItem(value: 'b', child: Text('B')),
  ],
  onChanged: (v) => setState(() => _selected = v!),
);

// Fixed: initialize with null or first item
String? _selected;

DropdownButton<String>(
  value: _selected,
  hint: Text('Select'),
  items: [...],
  onChanged: (v) => setState(() => _selected = v),
);
```

```text
There should be exactly one item with [DropdownButton]'s value
```
