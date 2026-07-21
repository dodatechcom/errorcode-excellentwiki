---
title: "Gradle Build Cache Error"
description: "Fix Gradle build cache corruption and performance issues"
languages: ["android"]
error-types: ["language-error"]
severities: ["error"]
---
Build cache errors cause unexpected build failures or stale outputs

## Common Causes

- Cache directory corrupted by failed build
- Cache key collision from non-deterministic tasks
- Custom task not annotated with cacheable
- Shared cache server misconfiguration

## Fixes

- Delete build-cache directory
- Mark custom tasks as @CacheableTask
- Use --no-build-cache to bypass temporarily
- Verify remote cache server connectivity

## Code Example

```kotlin
# Clear build cache
rm -rf .gradle/caches/build-cache-*
# Or disable cache for one build
./gradlew assembleDebug --no-build-cache
```

# For custom tasks, annotate with:
@CacheableTask
abstract class MyTask extends DefaultTask { ... }
