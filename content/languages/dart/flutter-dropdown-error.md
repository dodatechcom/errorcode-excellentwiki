---
title: "[Solution] Flutter Dropdown Error — value, items, onChanged, hint"
description: "Fix Flutter DropdownButton errors from value/items mismatch, onChanged nullability, hint decoration, and item type issues."
languages: ["dart"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 169
---

Dropdown errors occur when the `value` is not in the `items` list, `onChanged` is null, or dropdown items have mismatched types.

## Common Causes

1. `value` parameter not matching any item in the list.
2. `onChanged` set to `null` making the dropdown non-interactive.
3. Items list being empty.
4. Using `DropdownButton<String>` with `null` values.
5. Not wrapping with `DropdownButtonHideUnderline` or handling decoration.

## How to Fix It

**Solution 1: Basic dropdown with validation**

```dart
import 'package:flutter/material.dart';

class SimpleDropdown extends StatefulWidget {
  @override
  State<SimpleDropdown> createState() => _SimpleDropdownState();
}

class _SimpleDropdownState extends State<SimpleDropdown> {
  String? _selectedItem;
  final List<String> _items = ['Apple', 'Banana', 'Cherry', 'Date'];
  
  @override
  Widget build(BuildContext context) {
    return DropdownButton<String>(
      value: _selectedItem,
      hint: Text('Select a fruit'),
      items: _items.map((item) {
        return DropdownMenuItem<String>(
          value: item,
          child: Text(item),
        );
      }).toList(),
      onChanged: (value) {
        setState(() {
          _selectedItem = value;
        });
      },
    );
  }
}
```

**Solution 2: Handle nullable value**

```dart
import 'package:flutter/material.dart';

class NullableDropdown extends StatefulWidget {
  @override
  State<NullableDropdown> createState() => _NullableDropdownState();
}

class _NullableDropdownState extends State<NullableDropdown> {
  String? _selectedItem;
  final List<String> _items = ['One', 'Two', 'Three'];
  
  @override
  Widget build(BuildContext context) {
    return DropdownButton<String>(
      value: _selectedItem,
      items: _items.map((item) {
        return DropdownMenuItem(
          value: item,
          child: Text(item),
        );
      }).toList(),
      onChanged: (value) {
        setState(() {
          _selectedItem = value;
        });
      },
    );
  }
}
```

**Solution 3: Searchable dropdown**

```dart
import 'package:flutter/material.dart';

class SearchableDropdown extends StatefulWidget {
  @override
  State<SearchableDropdown> createState() => _SearchableDropdownState();
}

class _SearchableDropdownState extends State<SearchableDropdown> {
  String? _selected;
  final List<String> _countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Argentina', 'Australia',
    'Brazil', 'Canada', 'China', 'Denmark', 'Egypt',
  ];
  
  @override
  Widget build(BuildContext context) {
    return DropdownButton<String>(
      value: _selected,
      isExpanded: true,
      hint: Text('Select country'),
      items: _countries.map((country) {
        return DropdownMenuItem(
          value: country,
          child: Text(country),
        );
      }).toList(),
      onChanged: (value) {
        setState(() => _selected = value);
      },
    );
  }
}
```

**Solution 4: Custom styled dropdown**

```dart
import 'package:flutter/material.dart';

Widget buildStyledDropdown(BuildContext context) {
  return Container(
    padding: EdgeInsets.symmetric(horizontal: 12),
    decoration: BoxDecoration(
      border: Border.all(color: Colors.grey),
      borderRadius: BorderRadius.circular(4),
    ),
    child: DropdownButtonHideUnderline(
      child: DropdownButton<int>(
        value: 1,
        items: [1, 2, 3].map((item) {
          return DropdownMenuItem(
            value: item,
            child: Text('Option $item'),
          );
        }).toList(),
        onChanged: (value) {},
      ),
    ),
  );
}
```

**Solution 5: DropdownButtonFormField for forms**

```dart
import 'package:flutter/material.dart';

Widget buildFormDropdown() {
  return DropdownButtonFormField<String>(
    decoration: InputDecoration(
      labelText: 'Category',
      border: OutlineInputBorder(),
    ),
    items: ['Tech', 'Science', 'Art'].map((category) {
      return DropdownMenuItem(
        value: category,
        child: Text(category),
      );
    }).toList(),
    onChanged: (value) {},
    validator: (value) {
      if (value == null) return 'Please select a category';
      return null;
    },
  );
}
```

## Examples

The `value` parameter must be one of the `items` values or `null` (if hint is shown). If `value` is set to a value not in `items`, Flutter throws an assertion error.

## Related Errors

- [Flutter Form Validation Error](/languages/dart/flutter-form-validation-error/)
- [Flutter List View Error](/languages/dart/flutter-list-view-error/)
- [Flutter Set State Error](/languages/dart/flutter-set-state-error/)
