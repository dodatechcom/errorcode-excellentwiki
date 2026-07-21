---
title: "[Solution] Flutter Slider onChanged Error"
description: "Fix Flutter Slider errors when the slider value does not update or throws an assertion error on invalid values."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A Slider onChanged error in Flutter occurs when the `Slider` widget throws an assertion error because the `value` is outside the `min` and `max` range, or `onChanged` is null when the slider should be interactive.

## Common Causes

- `value` exceeds `max` or is below `min`
- `divisions` does not evenly divide the range between `min` and `max`
- `onChanged` set to `null` making the slider non-interactive
- `value` type is `double` but integer is passed
- `min` equals `max` creating a zero-range slider

## How to Fix

1. Clamp the value within the valid range:

```dart
double _value = 50;

Slider(
  value: _value.clamp(0.0, 100.0),
  min: 0,
  max: 100,
  divisions: 10,
  label: _value.round().toString(),
  onChanged: (double newValue) {
    setState(() => _value = newValue);
  },
);
```

2. Handle edge cases with min/max validation:

```dart
class _SliderScreenState extends State<SliderScreen> {
  double _value = 50;

  @override
  Widget build(BuildContext context) {
    final min = 0.0;
    final max = 100.0;

    // Ensure value is within bounds
    final safeValue = _value.clamp(min, max);

    return Slider(
      value: safeValue,
      min: min,
      max: max,
      divisions: 10,
      label: safeValue.round().toString(),
      onChanged: (v) => setState(() => _value = v),
    );
  }
}
```

3. Use `onChanged` and `onChangeEnd` for debounced updates:

```dart
Slider(
  value: _value,
  min: 0,
  max: 100,
  onChanged: (v) => setState(() => _value = v),
  onChangeEnd: (v) {
    // Save value when user stops dragging
    savePreference('brightness', v);
  },
);
```

## Examples

```dart
// Bug: value exceeds max
double _value = 150;

Slider(
  value: _value, // Error: value must be <= max
  min: 0,
  max: 100,
  onChanged: (v) => setState(() => _value = v),
);

// Fixed: clamp value
Slider(
  value: _value.clamp(0.0, 100.0),
  min: 0,
  max: 100,
  onChanged: (v) => setState(() => _value = v),
);
```

```text
'value' must not be greater than 'max'
```
