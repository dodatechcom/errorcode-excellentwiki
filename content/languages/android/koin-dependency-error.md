---
title: "Koin Module Error"
description: "Fix Koin dependency injection configuration and module errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Koin cannot provide required dependencies because of module misconfiguration

## Common Causes

- Koin module not declared with module {}
- Single, factory, or viewModel scope incorrect
- Module not loaded in Application class
- Injecting dependency not defined in any module

## Fixes

- Define all dependencies in Koin modules
- Use correct scope: single for singletons, viewModel for ViewModels
- Load modules in Application with startKoin
- Use inject() or get() to resolve dependencies

## Code Example

```kotlin
// Define module
val appModule = module {
    single { ApiService(get()) }
    single { Repository(get()) }
    viewModel { MyViewModel(get()) }
}

// In Application:
class MyApp : Application() {
    override fun onCreate() {
        super.onCreate()
        startKoin {
            androidContext(this@MyApp)
            modules(appModule)
        }
    }
}

// In Activity/Fragment:
class MyActivity : AppCompatActivity() {
    private val viewModel: MyViewModel by viewModel()
    private val repository: Repository by inject()
}
```

# single: one instance (singleton)
# factory: new instance each time
# viewModel: ViewModel scope
# Use get() to resolve dependencies
