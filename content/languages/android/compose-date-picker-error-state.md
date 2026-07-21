---
title: "DatePicker Selection Error"
description: "Fix Material 3 DatePicker selection state and validation errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
DatePicker does not properly track selected date or validate ranges

## Common Causes

- Selected date not updating
- Date range validation not working
- DatePicker not highlighting selected date
- Initial date not set correctly

## Fixes

- Use DatePickerState for selection tracking
- Validate dates before confirming
- Set initialSelectedDateMillis for default
- Use selectableDates for date restrictions

## Code Example

```kotlin
val datePickerState = rememberDatePickerState(
    initialSelectedDateMillis = System.currentTimeMillis()
)

DatePicker(
    state = datePickerState,
    title = { Text("Select Date") },
    headline = {
        Text(
            datePickerState.selectedDateMillis?.let {
                SimpleDateFormat("MMM dd, yyyy").format(Date(it))
            } ?: "No date selected"
        )
    },
    showModeToggle = true
)

// Get selected date:
val selectedDate = datePickerState.selectedDateMillis?.let {
    SimpleDateFormat("yyyy-MM-dd").format(Date(it))
}
```

# DatePickerState: manages selection
# initialSelectedDateMillis: default date
# selectedDateMillis: currently selected date
# selectableDates: restrict available dates
