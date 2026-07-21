---
title: "Compose Form State Error"
description: "Fix Compose form state management and multi-field coordination errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Form fields do not coordinate state changes or reset properly

## Common Causes

- Field values not accessible to other fields
- Form reset not clearing all fields
- Dependent field validation not triggering
- Form state not persisted across recomposition

## Fixes

- Use ViewModel for form state management
- Reset all fields in ViewModel reset method
- Validate dependent fields when dependencies change
- Use rememberSaveable for form fields

## Code Example

```kotlin
@Composable
fun LoginForm(viewModel: LoginViewModel = hiltViewModel()) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    Column {
        OutlinedTextField(
            value = uiState.email,
            onValueChange = { viewModel.updateEmail(it) },
            label = { Text("Email") },
            isError = uiState.emailError != null,
            supportingText = { uiState.emailError?.let { Text(it) } }
        )
        OutlinedTextField(
            value = uiState.password,
            onValueChange = { viewModel.updatePassword(it) },
            label = { Text("Password") },
            isError = uiState.passwordError != null,
            visualTransformation = PasswordVisualTransformation()
        )
        Button(
            onClick = { viewModel.login() },
            enabled = uiState.isFormValid
        ) {
            Text("Login")
        }
    }
}
```

# ViewModel manages all form state
# updateField methods trigger validation
# isFormValid derived from field states
