---
title: "[Solution] Flutter Switch ListTile Error"
description: "Fix Flutter Switch ListTile errors when the switch does not toggle or displays incorrect state."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Switch ListTile error in Flutter occurs when the `SwitchListTile` widget does not toggle its value when tapped, or the visual state does not match the underlying boolean because `onChanged` does not call `setState`.

## Common Causes

- `onChanged` callback does not update the state variable
- `value` property reads from the wrong variable
- `SwitchListTile` inside a parent that rebuilds and resets state
- `enabled: false` set without visual indication
- `activeColor` or `activeTrackColor` not defined for visibility

## How to Fix

1. Update state in onChanged:

```dart
class _SettingsState extends State<Settings> {
  bool _notificationsEnabled = true;
  bool _darkMode = false;

  @override
  Widget build(BuildContext context) {
    return ListView(
      children: [
        SwitchListTile(
          title: const Text('Enable Notifications'),
          subtitle: const Text('Receive push notifications'),
          value: _notificationsEnabled,
          onChanged: (bool value) {
            setState(() => _notificationsEnabled = value);
          },
        ),
        SwitchListTile(
          title: const Text('Dark Mode'),
          value: _darkMode,
          secondary: const Icon(Icons.dark_mode),
          onChanged: (bool value) {
            setState(() => _darkMode = value);
          },
        ),
      ],
    );
  }
}
```

2. Use a separate state management approach:

```dart
SwitchListTile(
  title: Text('Airplane Mode'),
  value: settings.airplaneMode,
  onChanged: (value) {
    settings.setAirplaneMode(value); // Provider/Bloc updates state
  },
);
```

3. Handle disabled state with visual feedback:

```dart
SwitchListTile(
  title: Text('Sync Data'),
  subtitle: Text(isOnline ? 'Connected' : 'Offline -- disabled'),
  value: _syncEnabled && isOnline,
  onChanged: isOnline
    ? (value) => setState(() => _syncEnabled = value)
    : null, // Disables the switch
);
```

## Examples

```dart
// Bug: onChanged does not update state
bool _enabled = false;

SwitchListTile(
  value: _enabled,
  onChanged: (value) {
    // Missing setState -- switch visually never changes
    _enabled = value;
  },
);

// Fixed
SwitchListTile(
  value: _enabled,
  onChanged: (value) {
    setState(() => _enabled = value);
  },
);
```

```text
setState() or markNeedsBuild() called during build
```
