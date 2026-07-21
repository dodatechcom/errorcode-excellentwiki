---
title: "[Solution] Flutter BottomNavigationBar Index Error"
description: "Fix Flutter BottomNavigationBar index errors when the selected tab does not match the displayed screen."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A BottomNavigationBar index error in Flutter occurs when the selected tab highlight does not match the displayed body content, or tapping a tab does not switch the screen because the index is not updated in state.

## Common Causes

- `currentIndex` not updated in `onTap` callback
- Multiple `Scaffold` instances instead of switching body content
- `_selectedIndex` initialized to wrong value
- `BottomNavigationBarItem` count does not match body pages
- `type` property set incorrectly for 4+ items

## How to Fix

1. Use IndexedStack for persistent page state:

```dart
class _HomeState extends State<Home> {
  int _selectedIndex = 0;

  final List<Widget> _pages = [
    HomePage(),
    SearchPage(),
    ProfilePage(),
    SettingsPage(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IndexedStack(
        index: _selectedIndex,
        children: _pages,
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        type: BottomNavigationBarType.fixed,
        onTap: (index) {
          setState(() => _selectedIndex = index);
        },
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
          BottomNavigationBarItem(icon: Icon(Icons.search), label: 'Search'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profile'),
          BottomNavigationBarItem(icon: Icon(Icons.settings), label: 'Settings'),
        ],
      ),
    );
  }
}
```

2. Use separate page switching for memory efficiency:

```dart
Widget _getCurrentPage() {
  switch (_selectedIndex) {
    case 0: return HomePage();
    case 1: return SearchPage();
    case 2: return ProfilePage();
    case 3: return SettingsPage();
    default: return HomePage();
  }
}

Scaffold(
  body: _getCurrentPage(),
  bottomNavigationBar: BottomNavigationBar(...),
);
```

3. Set correct type for 4+ items:

```dart
BottomNavigationBar(
  type: BottomNavigationBarType.fixed, // Required for 4+ items
  currentIndex: _selectedIndex,
  items: [...],
);
```

## Examples

```dart
// Bug: currentIndex hardcoded
BottomNavigationBar(
  currentIndex: 0, // Always highlights first tab
  onTap: (index) => print(index), // Does not update UI
);

// Fixed: update state
BottomNavigationBar(
  currentIndex: _selectedIndex,
  onTap: (index) => setState(() => _selectedIndex = index),
);
```

```text
BottomNavigationBarType.fixed is required when there are more than 3 items
```
