---
title: "DateRangePicker Error"
description: "Fix Material 3 DateRangePicker configuration and selection errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DateRangePicker does not allow range selection or displays incorrectly

## Common Causes

- Range start and end dates not properly tracked
- Selected range not highlighting correctly
- DateRangePicker not showing in dialog
- Range validation not working

## Fixes

- Use DateRangePickerState for range tracking
- Use DatePickerState for range mode
- Wrap in DatePickerDialog for modal display
- Validate date ranges in selection callback

## Code Example

```kotlin
var showRangePicker by remember { mutableStateOf(false) }
var startDate by remember { mutableStateOf<LocalDate?>(null) }
var endDate by remember { mutableStateOf<LocalDate?>(null) }

if (showRangePicker) {
    DatePickerDialog(
        onDismissRequest = { showRangePicker = false },
        confirmButton = {
            TextButton(onClick = { showRangePicker = false }) {
                Text("OK")
            }
        }
    ) {
        DatePicker(
            state = rememberDatePickerState(),
            title = { Text("Select date range") }
        )
    }
}
```

# DateRangePicker: select date range
# DatePickerState: manages selection
# Wrap in DatePickerDialog for modal
# Validate ranges before confirming
