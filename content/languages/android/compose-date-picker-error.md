---
title: "DatePicker Configuration Error"
description: "Fix Material 3 DatePicker and TimePicker configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DatePicker or TimePicker does not display correctly or handle selection

## Common Causes

- DatePickerDialog not showing when triggered
- Selected date not properly formatted
- TimePicker 24-hour vs 12-hour mode incorrect
- Date range validation not working

## Fixes

- Use DatePickerDialog composable
- Format selected date with LocalDate
- Set timeFormat for 12/24 hour mode
- Validate date ranges in onConfirm

## Code Example

```kotlin
var showDatePicker by remember { mutableStateOf(false) }
var selectedDate by remember { mutableStateOf(LocalDate.now()) }

if (showDatePicker) {
    DatePickerDialog(
        onDismissRequest = { showDatePicker = false },
        confirmButton = {
            TextButton(onClick = {
                showDatePicker = false
            }) {
                Text("OK")
            }
        },
        dismissButton = {
            TextButton(onClick = { showDatePicker = false }) {
                Text("Cancel")
            }
        }
    ) {
        DatePicker(
            state = rememberDatePickerState(
                initialSelectedDateMillis = selectedDate.toEpochDay() * 86400000L
            )
        )
    }
}
```

# DatePickerDialog: modal date selection
# DatePicker: inline date selection
# TimePicker: time selection
# DatePickerState: manages selection state
