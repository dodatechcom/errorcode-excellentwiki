---
title: "State Migration Error"
description: "Fix migration from XML/LiveData to Compose/StateFlow architecture"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Migrating from LiveData to StateFlow causes state inconsistencies

## Common Causes

- LiveData not properly converted to StateFlow
- Observer pattern not matching Compose collection
- Configuration change behavior different
- Backward compatibility with existing XML views

## Fixes

- Convert LiveData to StateFlow in ViewModel
- Use collectAsStateWithLifecycle in Compose
- Test configuration change behavior
- Use ComposeView for gradual migration

## Code Example

```kotlin
// Old: LiveData
val _items = MutableLiveData<List<Item>>()
val items: LiveData<List<Item>> = _items

// New: StateFlow
private val _items = MutableStateFlow<List<Item>>(emptyList())
val items: StateFlow<List<Item>> = _items.asStateFlow()

// In Compose:
val items by viewModel.items.collectAsStateWithLifecycle()

// Gradual migration:
class MyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Gradually move screens to Compose
        findViewById<ComposeView>(R.id.compose_container).setContent {
            MyComposeScreen()
        }
    }
}
```

# LiveData -> StateFlow migration
# collectAsStateWithLifecycle for Compose
# ComposeView for gradual migration
# Test both architectures during migration
