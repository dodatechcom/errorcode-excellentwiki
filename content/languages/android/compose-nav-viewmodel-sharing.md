---
title: "Navigation ViewModel Sharing Error"
description: "Fix ViewModel sharing across Compose navigation destinations"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
ViewModel instances not shared correctly between navigation destinations

## Common Causes

- Different ViewModel instances for same destination
- ViewModel scoped to wrong navigation graph
- SharedViewModel not accessible in child destination
- ViewModel lost after navigation pop

## Fixes

- Use navGraphViewModels for graph-scoped ViewModel
- Share ViewModel with parent using activityViewModels()
- Scope ViewModel to navController graph
- Use correct ViewModel store owner

## Code Example

```kotlin
// ViewModel shared within nav graph
@Composable
fun NavGraph(navController: NavHostController) {
    navController.navDestination("home") {
        val sharedViewModel: SharedViewModel = hiltViewModel()

        HomeScreen(
            onNext = { navController.navigate("detail") }
        )
    }

    navController.navDestination("detail") {
        // Same ViewModel instance within same nav graph
        val sharedViewModel: SharedViewModel = hiltViewModel()
        DetailScreen(sharedViewModel)
    }
}

// Share with Activity:
val activityViewModel: ActivityViewModel = activityViewModels()
```

# hiltViewModel(): scoped to nav destination
# activityViewModels(): shared with Activity
# navGraphViewModels(): shared within nav graph
# ViewModel store owner determines scope
