---
title: "Hilt Multibinding Error"
description: "Fix Hilt multibinding and set/map injection configuration errors"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Hilt cannot inject collections of implementations because multibinding is misconfigured

## Common Causes

- @IntoSet or @IntoMap not specified on providers
- Map key not defined for @IntoMap
- Set element type not matching injection site
- Multibinding module not installed in correct component

## Fixes

- Use @IntoSet for Set<T> injection
- Use @IntoMap with @MapKey for Map injection
- Ensure element type matches exactly
- Install multibinding module in correct Hilt component

## Code Example

```kotlin
// Set injection
@Module
@InstallIn(SingletonComponent::class)
object AnalyticsModule {
    @Provides
    @IntoSet
    fun provideTracker1(): Tracker = FirebaseTracker()

    @Provides
    @IntoSet
    fun provideTracker2(): Tracker = AmplitudeTracker()
}

// Inject:
class AnalyticsService @Inject constructor(
    private val trackers: Set<@JvmSuppressWildcards Tracker>
) {
    fun track(event: Event) {
        trackers.forEach { it.track(event) }
    }
}

// Map injection:
@StringKey("firebase")
@IntoMap
fun provideFirebaseAnalytics() = FirebaseAnalytics()
```

# @IntoSet: adds to Set<T>
# @IntoMap: adds to Map<Key, T>
# @StringKey, @ClassKey: map key types
