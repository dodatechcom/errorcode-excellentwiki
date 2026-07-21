---
title: "Two-Way Binding Error"
description: "Fix two-way data binding errors with双向 binding expressions in Android"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Two-way binding with @={ } does not sync UI and data correctly

## Common Causes

- Two-way binding expression has incorrect syntax
- Binding variable not mutable (val instead of var)
- EditText input not properly bound to variable
- InverseBindingAdapter missing for custom view

## Fixes

- Use @={variable} syntax for two-way binding
- Ensure binding variable is mutable (MutableLiveData or var)
- Use @InverseBindingAdapter for custom view attributes
- Handle null values in binding expressions

## Code Example

```kotlin
<!-- One-way binding: @{ } -->
<TextView android:text="@{viewModel.name}" />

<!-- Two-way binding: @={ } -->
<EditText
    android:text="@={viewModel.name}"
    android:hint="Enter name" />

<!-- Custom two-way binding: -->
@BindingAdapter("app:myValue")
@JvmStatic
fun setMyValue(view: MyView, value: String?) {
    view.setValue(value)
}

@InverseBindingAdapter("app:myValue")
@JvmStatic
fun getMyValue(view: MyView): String? = view.getValue()
```

# Two-way binding: @={expression}
# One-way binding: @{expression}
# @InverseBindingAdapter for custom views
