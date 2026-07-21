---
title: "[Solution] Flutter FocusNode Error"
description: "Fix Flutter FocusNode errors when text fields do not receive focus or lose focus unexpectedly."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A FocusNode error in Flutter occurs when a `TextField` or other focusable widget does not receive or maintain keyboard focus properly, preventing text input or causing unexpected focus changes.

## Common Causes

- `FocusNode` not created or disposed properly
- Multiple `FocusNode` instances competing for focus
- `FocusScope.of(context).unfocus()` called at the wrong time
- `autoFocus: true` on multiple widgets
- `FocusNode` not passed to the `TextField` constructor

## How to Fix

1. Create and dispose FocusNodes correctly:

```dart
class _MyFormState extends State<MyForm> {
  final _nameFocus = FocusNode();
  final _emailFocus = FocusNode();

  @override
  void dispose() {
    _nameFocus.dispose();
    _emailFocus.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TextField(
          focusNode: _nameFocus,
          decoration: const InputDecoration(labelText: 'Name'),
          textInputAction: TextInputAction.next,
          onSubmitted: (_) => _emailFocus.requestFocus(),
        ),
        TextField(
          focusNode: _emailFocus,
          decoration: const InputDecoration(labelText: 'Email'),
        ),
      ],
    );
  }
}
```

2. Request focus programmatically:

```dart
class _SearchScreenState extends State<SearchScreen> {
  final _searchFocus = FocusNode();

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _searchFocus.requestFocus();
    });
  }

  @override
  Widget build(BuildContext context) {
    return TextField(
      focusNode: _searchFocus,
      decoration: const InputDecoration(hintText: 'Search...'),
    );
  }
}
```

3. Handle focus traversal between fields:

```dart
TextField(
  textInputAction: TextInputAction.next,
  onSubmitted: (_) => FocusScope.of(context).nextFocus(),
);

TextField(
  textInputAction: TextInputAction.done,
  onSubmitted: (_) => FocusScope.of(context).unfocus(),
);
```

## Examples

```dart
// Bug: FocusNode created in build method -- recreated every rebuild
Widget build(BuildContext context) {
  return TextField(
    focusNode: FocusNode(), // New instance every rebuild
    decoration: InputDecoration(labelText: 'Name'),
  );
}

// Fixed: create in state
final _focusNode = FocusNode();

Widget build(BuildContext context) {
  return TextField(
    focusNode: _focusNode, // Same instance
    decoration: InputDecoration(labelText: 'Name'),
  );
}
```

```text
A FocusNode was used after being disposed.
```
