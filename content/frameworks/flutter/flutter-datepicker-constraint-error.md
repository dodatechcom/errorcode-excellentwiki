---
title: "[Solution] Flutter DatePicker Constraint Error"
description: "Fix Flutter DatePicker constraint errors when the date picker dialog does not display or crashes on invalid dates."
frameworks: ["flutter"]
error-types: ["framework-error"]
severities: ["error"]
---

A DatePicker constraint error in Flutter occurs when the date picker dialog fails to open because the initial date is outside the allowed range, or the `firstDate` is after the `lastDate`.

## Common Causes

- `initialDate` is before `firstDate` or after `lastDate`
- `firstDate` is set to a future date
- `lastDate` is set to a past date
- `initialDate` is `null` when the field is required
- Date formatting produces an unparseable string

## How to Fix

1. Set valid date constraints:

```dart
DateTime? _selectedDate;

Future<void> _pickDate(BuildContext context) async {
  final picked = await showDatePicker(
    context: context,
    initialDate: _selectedDate ?? DateTime.now(),
    firstDate: DateTime(2000),
    lastDate: DateTime(2100),
  );
  if (picked != null) {
    setState(() => _selectedDate = picked);
  }
}
```

2. Validate date range before showing picker:

```dart
Future<void> _pickDate(BuildContext context) async {
  final now = DateTime.now();
  final initial = _selectedDate?.isAfter(now) == true ? _selectedDate! : now;

  final picked = await showDatePicker(
    context: context,
    initialDate: initial,
    firstDate: DateTime(2020),
    lastDate: DateTime(2030),
    selectableDayPredicate: (date) {
      // Disable weekends
      return date.weekday != DateTime.saturday && date.weekday != DateTime.sunday;
    },
  );
  if (picked != null) {
    setState(() => _selectedDate = picked);
  }
}
```

3. Format and display the selected date:

```dart
Text(
  _selectedDate != null
    ? '${_selectedDate!.day}/${_selectedDate!.month}/${_selectedDate!.year}'
    : 'Select date',
);
```

## Examples

```dart
// Bug: firstDate after lastDate
showDatePicker(
  context: context,
  initialDate: DateTime(2023),
  firstDate: DateTime(2025), // Future
  lastDate: DateTime(2020),  // Past -- invalid range
);

// Fixed: valid range
showDatePicker(
  context: context,
  initialDate: DateTime.now(),
  firstDate: DateTime(2020),
  lastDate: DateTime(2030),
);
```

```text
'initialDate' must be between 'firstDate' and 'lastDate'
```
