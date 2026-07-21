---
title: "[Solution] Flutter Drawer Open Close Error"
description: "Fix Flutter drawer open and close errors when the navigation drawer does not toggle or closes unexpectedly."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Drawer open/close error in Flutter occurs when `Scaffold.of(context).openDrawer()` fails because the context does not contain a `Scaffold`, or the drawer closes prematurely when navigation occurs.

## Common Causes

- `Scaffold.of(context)` called with a context above the `Scaffold`
- `Navigator.pop(context)` called inside drawer onTap closing both drawer and screen
- `DrawerController` not accessible for programmatic open/close
- Drawer opens but immediately closes due to rebuild
- `endDrawer` set but user expects left-side drawer

## How to Fix

1. Use the correct context for Scaffold operations:

```dart
Builder(
  builder: (context) {
    return ListTile(
      title: Text('Open Drawer'),
      onTap: () {
        Scaffold.of(context).openDrawer(); // Use Builder context
      },
    );
  },
);
```

2. Close drawer before navigation:

```dart
Drawer(
  child: ListView(
    children: [
      const DrawerHeader(child: Text('Menu')),
      ListTile(
        title: Text('Profile'),
        onTap: () {
          Navigator.pop(context); // Close drawer first
          Navigator.push(context, MaterialPageRoute(
            builder: (_) => ProfileScreen(),
          ));
        },
      ),
      ListTile(
        title: Text('Settings'),
        onTap: () {
          Navigator.pop(context);
          Navigator.push(context, MaterialPageRoute(
            builder: (_) => SettingsScreen(),
          ));
        },
      ),
    ],
  ),
);
```

3. Use GlobalKey to control drawer programmatically:

```dart
final _scaffoldKey = GlobalKey<ScaffoldState>();

Scaffold(
  key: _scaffoldKey,
  drawer: Drawer(child: DrawerContent()),
  body: ElevatedButton(
    onPressed: () => _scaffoldKey.currentState?.openDrawer(),
    child: Text('Open Menu'),
  ),
);
```

## Examples

```dart
// Bug: Scaffold.of(context) uses wrong context
ElevatedButton(
  onPressed: () {
    Scaffold.of(context).openDrawer(); // Error: no Scaffold ancestor
  },
  child: Text('Menu'),
);

// Fixed: wrap with Builder
Builder(
  builder: (context) => ElevatedButton(
    onPressed: () => Scaffold.of(context).openDrawer(),
    child: Text('Menu'),
  ),
);
```

```text
Scaffold.of() called with a context that does not include a Scaffold.
```
