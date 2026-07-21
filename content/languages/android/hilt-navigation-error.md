---
title: "Hilt Navigation Error"
description: "Fix Hilt navigation integration errors with Navigation component"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Hilt does not inject dependencies correctly in Navigation destinations

## Common Causes

- @AndroidEntryPoint missing on navigation target Fragment
- Hilt nav dependency not added
- ViewModel not scoped to navigation graph
- NavBackStackEntry not providing correct scope

## Fixes

- Add @AndroidEntryPoint to all navigation Fragments
- Add hilt-navigation-fragment dependency
- Use hiltViewModel() delegate in Compose
- Scope ViewModel to navGraphViewModels()

## Code Example

```kotlin
dependencies {
    implementation "androidx.hilt:hilt-navigation-fragment:1.1.0"
}

// In Fragment with Navigation:
@AndroidEntryPoint
class DetailFragment : Fragment() {
    // ViewModel scoped to nav graph
    val viewModel: DetailViewModel by navGraphViewModels(R.id.detail_graph)

    // Or regular ViewModel:
    val viewModel: DetailViewModel by viewModels()
}

// In Compose with Navigation:
@AndroidEntryPoint
class NavHostActivity : AppCompatActivity() {
    @Composable
    fun NavGraph() {
        navController.navDestination("detail/{id}") {
            val viewModel: DetailViewModel = hiltViewModel()
        }
    }
}
```

# hilt-viewmodel: @HiltViewModel support
# hilt-navigation: navGraphViewModels()
# hilt-navigation-compose: hiltViewModel()
