---
title: "[Solution] Flutter Autocomplete Options Error"
description: "Fix Flutter Autocomplete errors when suggestion list does not appear or options are not filtered correctly."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

An Autocomplete option error in Flutter occurs when the `Autocomplete` widget does not show suggestions because the `optionsBuilder` returns an empty list, or the suggestions are not filtered based on the current text input.

## Common Causes

- `optionsBuilder` returns an empty iterable for all inputs
- Case-sensitive comparison does not match user input
- `displayStringForOption` returns an empty string
- Options list not populated when `Autocomplete` initializes
- `onSelected` not handling the chosen option

## How to Fix

1. Implement optionsBuilder with proper filtering:

```dart
Autocomplete<String>(
  optionsBuilder: (TextEditingValue textEditingValue) {
    if (textEditingValue.text.isEmpty) {
      return const Iterable.empty();
    }
    return _allItems.where((item) =>
      item.toLowerCase().contains(textEditingValue.text.toLowerCase())
    );
  },
  onSelected: (String selection) {
    setState(() => _selectedItem = selection);
  },
  fieldViewBuilder: (context, controller, focusNode, onSubmitted) {
    return TextField(
      controller: controller,
      focusNode: focusNode,
      decoration: const InputDecoration(
        labelText: 'Search',
        border: OutlineInputBorder(),
      ),
      onSubmitted: (_) => onSubmitted(),
    );
  },
);
```

2. Use custom display and filtering:

```dart
Autocomplete<User>(
  displayStringForOption: (user) => user.name,
  optionsBuilder: (TextEditingValue textEditingValue) {
    final query = textEditingValue.text.toLowerCase();
    return _users.where((user) =>
      user.name.toLowerCase().contains(query) ||
      user.email.toLowerCase().contains(query)
    );
  },
  onSelected: (User user) {
    _controller.text = user.name;
  },
);
```

3. Show all options when input is empty:

```dart
optionsBuilder: (TextEditingValue textEditingValue) {
  if (textEditingValue.text.isEmpty) {
    return _allSuggestions; // Show all when empty
  }
  return _allSuggestions.where((s) =>
    s.toLowerCase().startsWith(textEditingValue.text.toLowerCase())
  );
},
```

## Examples

```dart
// Bug: optionsBuilder always returns empty
Autocomplete<String>(
  optionsBuilder: (textEditingValue) {
    return []; // Always empty -- no suggestions ever shown
  },
  onSelected: (s) => print(s),
);

// Fixed: return filtered options
Autocomplete<String>(
  optionsBuilder: (textEditingValue) {
    if (textEditingValue.text.isEmpty) return [];
    return _items.where((i) => i.contains(textEditingValue.text));
  },
  onSelected: (s) => print(s),
);
```

```text
Autocomplete's options must not be empty when the field is focused
```
