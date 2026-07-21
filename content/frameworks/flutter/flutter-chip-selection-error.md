---
title: "[Solution] Flutter Chip Selected Error"
description: "Fix Flutter Chip selection errors when chips do not highlight or respond to tap events correctly."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Chip selected error in Flutter occurs when `FilterChip`, `ChoiceChip`, or `ActionChip` does not respond to taps or does not visually reflect the selected state because the `onSelected` or `onPressed` callback is missing or the `selected` property is not updated.

## Common Causes

- `FilterChip` missing `onSelected` callback
- `selected` property not tied to state variable
- `ChoiceChip` list uses the wrong index for `selected`
- `onPressed` on `ActionChip` set to null making it non-interactive
- Chip inside a parent widget that rebuilds and resets selection

## How to Fix

1. Track chip selection state:

```dart
class _ChipFilterState extends State<ChipFilter> {
  final List<String> _selectedTags = [];
  final List<String> _allTags = ['Flutter', 'Dart', 'Firebase', 'UI'];

  @override
  Widget build(BuildContext context) {
    return Wrap(
      spacing: 8,
      children: _allTags.map((tag) {
        return FilterChip(
          label: Text(tag),
          selected: _selectedTags.contains(tag),
          onSelected: (bool selected) {
            setState(() {
              if (selected) {
                _selectedTags.add(tag);
              } else {
                _selectedTags.remove(tag);
              }
            });
          },
        );
      }).toList(),
    );
  }
}
```

2. Use ChoiceChip for single selection:

```dart
int _selectedIndex = 0;
final List<String> _options = ['Small', 'Medium', 'Large'];

Wrap(
  spacing: 8,
  children: List.generate(_options.length, (index) {
    return ChoiceChip(
      label: Text(_options[index]),
      selected: _selectedIndex == index,
      onSelected: (bool selected) {
        if (selected) {
          setState(() => _selectedIndex = index);
        }
      },
    );
  }),
);
```

3. Disable chips when needed:

```dart
ActionChip(
  label: Text('Subscribe'),
  avatar: const Icon(Icons.notifications),
  onPressed: _isSubscribed ? null : () => subscribe(),
  backgroundColor: _isSubscribed ? Colors.grey.shade200 : null,
);
```

## Examples

```dart
// Bug: selected always true
FilterChip(
  label: Text('Tag'),
  selected: true, // Always selected regardless of state
  onSelected: (v) {},
);

// Fixed: tie to state
FilterChip(
  label: Text('Tag'),
  selected: _selectedTags.contains('Tag'),
  onSelected: (selected) {
    setState(() {
      selected ? _selectedTags.add('Tag') : _selectedTags.remove('Tag');
    });
  },
);
```

```text
FilterChip.onSelected must not be null when the chip is interactive
```
