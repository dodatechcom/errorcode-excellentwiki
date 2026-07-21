---
title: "Compose Hilt Integration Error"
description: "Fix Compose and Hilt dependency injection integration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Hilt does not inject dependencies correctly in Compose screens

## Common Causes

- @AndroidEntryPoint not on Activity hosting Compose
- hiltViewModel() not providing correct ViewModel
- Compose dependency not resolving from Hilt graph
- ViewModel scope not matching expected lifecycle

## Fixes

- Add @AndroidEntryPoint to hosting Activity
- Use hiltViewModel() for Compose ViewModel
- Ensure dependency is in correct Hilt module
- Use correct ViewModel scope

## Code Example

```kotlin
@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MyScreen()
        }
    }
}

@Composable
fun MyScreen(viewModel: MyViewModel = hiltViewModel()) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    // Use uiState...
}
```

# @AndroidEntryPoint: enable Hilt for Activity
# hiltViewModel(): get ViewModel with Hilt injection
# hilt-work: Worker injection with Hilt
