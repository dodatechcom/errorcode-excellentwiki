---
title: "[Solution] Flutter Keyboard Dismiss Error"
description: "Fix Flutter keyboard dismiss errors when tapping outside a TextField does not close the on-screen keyboard."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A keyboard dismiss error in Flutter occurs when the on-screen keyboard does not close after the user taps outside a `TextField` or `TextFormField`. This is common when widgets lack a `GestureDetector` to handle tap events.

## Common Causes

- No `GestureDetector` wrapping the Scaffold body
- `FocusScope.of(context).unfocus()` not called on tap
- `TextField` is inside a scrollable widget that absorbs taps
- `AlwaysKeepFocus` or `autofocus: true` keeps the keyboard open
- Modal bottom sheet prevents tap events from reaching the scaffold

## How to Fix

1. Wrap the Scaffold body with a GestureDetector:

```dart
GestureDetector(
  onTap: () => FocusScope.of(context).unfocus(),
  child: Scaffold(
    appBar: AppBar(title: const Text('Form')),
    body: Column(
      children: [
        TextField(decoration: InputDecoration(labelText: 'Name')),
        TextField(decoration: InputDecoration(labelText: 'Email')),
      ],
    ),
  ),
);
```

2. Use `FocusManager` to dismiss keyboard globally:

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => FocusManager.instance.primaryFocus?.unfocus(),
      child: MaterialApp(home: HomeScreen()),
    );
  }
}
```

3. Dismiss keyboard when navigating:

```dart
void navigateToNext() {
  FocusScope.of(context).unfocus();
  Navigator.push(context, MaterialPageRoute(builder: (_) => NextScreen()));
}
```

## Examples

```dart
// Bug: keyboard stays open when tapping outside
Scaffold(
  body: ListView(
    children: [
      TextField(decoration: InputDecoration(labelText: 'Search')),
      // Tapping on list items does not dismiss keyboard
    ],
  ),
);

// Fixed: dismiss on tap outside
Scaffold(
  body: GestureDetector(
    onTap: () => FocusScope.of(context).unfocus(),
    child: ListView(
      children: [
        TextField(decoration: InputDecoration(labelText: 'Search')),
      ],
    ),
  ),
);
```

```text
System channels may not be available while the keyboard is open
```
