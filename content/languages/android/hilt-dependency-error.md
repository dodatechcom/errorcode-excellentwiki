---
title: "Hilt Dependency Error"
description: "Fix Hilt dependency injection errors and module configuration"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Hilt cannot provide required dependencies because of module configuration issues

## Common Causes

- @HiltAndroidApp missing on Application class
- @AndroidEntryPoint missing on Activity/Fragment
- @Module with @InstallIn not properly scoped
- Circular dependency between injected classes

## Fixes

- Add @HiltAndroidApp to Application class
- Add @AndroidEntryPoint to all injected components
- Use correct component scope in @InstallIn
- Break circular dependencies with @Lazy injection

## Code Example

```kotlin
@HiltAndroidApp
class MyApplication : Application()

@AndroidEntryPoint
class MainActivity : AppCompatActivity() {
    @Inject lateinit var repository: Repository
}

@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
    @Provides
    @Singleton
    fun provideApiService(): ApiService {
        return Retrofit.Builder()
            .baseUrl("https://api.example.com/")
            .build()
            .create(ApiService::class.java)
    }
}
```

# Hilt components:
# SingletonComponent: Application scope
# ActivityComponent: Activity scope
# FragmentComponent: Fragment scope
# ViewModelComponent: ViewModel scope
