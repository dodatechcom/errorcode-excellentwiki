---
title: "Compose Form Validation Error"
description: "Fix Compose form validation and input state management errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Form validation does not trigger correctly or shows wrong error messages

## Common Causes

- Validation not running on input change
- Error message not clearing when input becomes valid
- Form state not shared between fields
- Submit button not disabled during invalid state

## Fixes

- Run validation on value change with derivedStateOf
- Clear error when input becomes valid
- Use shared ViewModel for form state
- Disable submit button based on form validity

## Code Example

```kotlin
@Composable
fun RegistrationForm(viewModel: FormViewModel = hiltViewModel()) {
    var name by remember { mutableStateOf("") }
    var email by remember { mutableStateOf("") }
    var nameError by remember { mutableStateOf<String?>(null) }

    // Validation
    LaunchedEffect(name) {
        nameError = if (name.isBlank()) "Name required" else null
    }

    Column {
        OutlinedTextField(
            value = name,
            onValueChange = { name = it },
            isError = nameError != null,
            supportingText = { nameError?.let { Text(it) } }
        )
        Button(
            onClick = { viewModel.submit(name, email) },
            enabled = nameError == null && email.isNotBlank()
        ) {
            Text("Submit")
        }
    }
}
```

# Validate on input change
# Show/hide errors based on current state
# Disable submit during invalid state
